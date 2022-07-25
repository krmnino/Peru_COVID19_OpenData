import numpy as np
import sys
import copy
import enum

class TL_ErrorCodes(enum.Enum):
    OK = 0,
    INVALID_ROW_LEGNTH = 1,
    FIELD_NOT_FOUND = 2,
    INVALID_ROW_INDEX = 3,
    INVALID_COLUMN_INDEX = 4,
    DUPLICATE_FIELD = 5,
    UNEVEN_TABLES = 6,
    UNEVEN_NEW_HEADER = 7,

class TL_Error(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.err_code = error_code

class TL_ErrorWrapper:
    def __init__(self, error_code):
        self.error_code = error_code
        if(self.error_code == TL_ErrorCodes.OK):
            self.message = ''
        if(self.error_code == TL_ErrorCodes.INVALID_ROW_LEGNTH):
            self.message = 'Input row length does not match table row length.'
        if(self.error_code == TL_ErrorCodes.FIELD_NOT_FOUND):
            self.message = 'Field name does not exist in table instance.'
        if(self.error_code == TL_ErrorCodes.INVALID_ROW_INDEX):
            self.message = 'Input row index is out of bounds.'
        if(self.error_code == TL_ErrorCodes.INVALID_COLUMN_INDEX):
            self.message = 'Input column index is out of bounds.'
        if(self.error_code == TL_ErrorCodes.DUPLICATE_FIELD):
            self.message = 'Field name passed already exist in table instance.'
        if(self.error_code == TL_ErrorCodes.UNEVEN_TABLES):
            self.message = 'Column count between two tables is not the same.'
        if(self.error_code == TL_ErrorCodes.UNEVEN_NEW_HEADER):
            self.message = 'The size of the new header does not match the current table header length.'
        else:
            self.message = 'Undefinded error.'

class Table:
    def __init__(self, *args, **kwargs):
        self.rows = 0
        self.columns = 0
        self.delimiter = ','
        self.filename = ''
        self.header_index = []
        self.contents = {}
        header_exists = True
        if(len(args) == 0):
            pass
        elif(args[0] == 'l'):
            self.filename = kwargs['filename']
            if('delimiter' in kwargs):
                self.delimiter = kwargs['delimiter']
            with open(self.filename, 'r') as file:
                for line in file:
                    if header_exists:
                        header_split = line.split(self.delimiter)
                        for i, elem in enumerate(header_split):
                            self.header_index.append(elem.replace('\n', ''))
                            self.contents[self.header_index[i]] = np.array([], dtype='int64')
                            self.columns += 1
                        header_exists = False
                        continue
                    line_split = line.split(self.delimiter)
                    for i, elem in enumerate(line_split):
                        elem = elem.replace('\n', '')
                        try:
                            if(elem.find('.') == -1):
                                convert_elem = int(elem)
                            else:
                                convert_elem = float(elem)
                        except:
                            convert_elem = str(elem)
                            pass
                        self.contents[self.header_index[i]] = np.append(self.contents[self.header_index[i]], convert_elem)
                    self.rows += 1
        elif(args[0] == 'c'):
            self.filename = kwargs['table'].filename
            self.header_index = copy.deepcopy(kwargs['table'].header_index)
            self.contents = copy.deepcopy(kwargs['table'].contents)
            self.rows = kwargs['table'].rows
            self.columns = kwargs['table'].columns
            self.delimiter = kwargs['table'].delimiter
        elif(args[0] == 'n'):
            if('delimiter' in kwargs):
                self.delimiter = kwargs['delimiter']
            if('header_index' in kwargs):
                self.header_index = kwargs['header_index']
                self.columns = len(self.header_index)
                self.rows = 0
                for i in range(0, self.columns):
                    self.contents[self.header_index[i]] = np.array([])
            elif('columns' in kwargs and 'rows' in kwargs):
                self.columns = kwargs['columns']
                self.rows = kwargs['rows']
                for i in range(0, self.columns):
                    self.header_index.append('X' + str(i))
                for i in range(0, self.columns):
                    self.contents[self.header_index[i]] = np.array([])
                    for j in range(0, self.rows):
                        self.contents[self.header_index[i]] = np.append(self.contents[self.header_index[i]], 0)
            else:
                self.columns = 0
                self.rows = 0

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_delimiter(self):
        return self.delimiter

    def get_header(self):
        return self.header_index

    def get_filename(self):
        return self.filename

    def get_column_data(self, field):
        out = None
        if(type(field) is int):
            if(0 > field or field >= self.columns):
                ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                raise TL_Error(ex.message, ex.error_code)
            out = self.contents[self.header_index[field]]
        elif(type(field) is str):     
            if(field not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
            out = self.contents[field]
        return out

    def get_row_data(self, idx):
        if(0 > idx or idx >= self.rows):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_INDEX)
            raise TL_Error(ex.message, ex.error_code)
        out = []
        for i in range(0, len(self.header_index)):
            out.append(self.contents[self.header_index[i]][idx])
        return out

    def get_begin_row(self):
        out = []
        if(self.rows == 0):
            return out
        for i in self.header_index:
            out.append(self.contents[i][0])
        return out

    def get_end_row(self):
        out = []
        if(self.rows == 0):
            return out
        for i in self.header_index:
            out.append(self.contents[i][self.rows-1])
        return out

    def get_cell_data(self, col, row):
        out = None
        if(0 > row or row >= self.rows):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_INDEX)
            raise TL_Error(ex.message, ex.error_code)
        if(type(col) == int):
            if(0 > col or col >= self.columns):
                ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                raise TL_Error(ex.message, ex.error_code)
            out = self.contents[self.header_index[col]][row]
        elif(type(col) == str):
            if(col not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
            out = self.contents[col][row]
        return out

    def set_filename(self, filename):
        self.filename = filename

    def set_delimiter(self, delim):
        self.delimiter = delim

    def set_header(self, new_header_index):
        if(len(new_header_index) != len(self.header_index)):
            ex = TL_ErrorWrapper(TL_ErrorCodes.UNEVEN_NEW_HEADER)
            raise TL_Error(ex.message, ex.error_code)
        for i in range(0, len(new_header_index)):
            if(new_header_index[i] in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.DUPLICATE_FIELD)
                raise TL_Error(ex.message, ex.error_code)
            col = self.contents[self.header_index[i]]
            del self.contents[self.header_index[i]]
            self.header_index[i] = new_header_index[i]
            self.contents[new_header_index[i]] = col

    def append_begin_row(self, data):
        if(len(data) != self.columns):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_LEGNTH)
            raise TL_Error(ex.message, ex.error_code)
        for i, elem in enumerate(self.contents):
            self.contents[elem] = np.insert(self.contents[elem], 0, data[i])
        self.rows += 1

    def append_end_row(self, data):
        if(len(data) != self.columns):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_LEGNTH)
            raise TL_Error(ex.message, ex.error_code)
        for i, elem in enumerate(self.contents):
            self.contents[elem] = np.append(self.contents[elem], data[i])
        self.rows += 1
        
    def update_cell_data(self, col, row, data):
        if(0 > row or row >= self.rows):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_INDEX)
            raise TL_Error(ex.message, ex.error_code)
        if(type(col) == int):
            if(0 > col or col >= self.columns):
                ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                raise TL_Error(ex.message, ex.error_code)
            self.contents[self.header_index[col]][row] = data
        elif(type(col) == str):
            if(col not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
            self.contents[col][row] = data

    def save_as_csv(self, path):
        with open(path, 'w') as file:
            out = ''
            for i in range(0, self.columns):
                file.write(self.header_index[i])
                if(i != self.columns - 1):
                    file.write(self.delimiter)
                else:
                    file.write('\n')
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    file.write(str(self.contents[self.header_index[j]][i]))
                    if(j != self.columns - 1):
                        file.write(self.delimiter)
                    else:
                        file.write('\n')

    def compute_new_column(self, new_col_key, cols, function):
        if(new_col_key in self.contents):
            ex = TL_ErrorWrapper(TL_ErrorCodes.DUPLICATE_FIELD)
            raise TL_Error(ex.message, ex.error_code)
        for i in range(0, len(cols)):
            if(type(cols[i]) is str):
                if(cols[i] not in self.contents):
                    ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                    raise TL_Error(ex.message, ex.error_code)
            elif(type(cols[i]) is int):
                if(0 > cols[i] or cols[i] >= self.columns):
                    ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                    raise TL_Error(ex.message, ex.error_code)
        table_columns = []
        for i in range(0, len(cols)):
            if(type(cols[i]) is str):
                table_columns.append(self.contents[cols[i]])
            elif(type(cols[i]) is int):
                table_columns.append(self.contents[self.header_index[cols[i]]])
        new_column = np.array([])
        for i in range(0, self.rows):
            new_column = np.append(new_column, function(i, table_columns))
        self.header_index.append(new_col_key)
        self.contents[new_col_key] = new_column
        self.columns += 1

    def compute_update_column(self, col_key, cols, function):
        if(type(col_key) is str):
            if(col_key not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
        elif(type(col_key) is int):
            if(0 > col_key or col_key >= self.columns):
                ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                raise TL_Error(ex.message, ex.error_code)
            col_key = self.header_index[col_key]
        for i in range(0, len(cols)):
            if(type(cols[i]) is str):
                if(cols[i] not in self.contents):
                    ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                    raise TL_Error(ex.message, ex.error_code)
            elif(type(cols[i]) is int):
                if(0 > cols[i] or cols[i] >= self.columns):
                    ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                    raise TL_Error(ex.message, ex.error_code)
                cols[i] = self.header_index[cols[i]]
        table_columns = []
        for i in range(0, len(cols)):
            table_columns.append(self.contents[cols[i]])
        for i in range(0, self.rows):
            self.contents[col_key][i] = function(i, table_columns)        

    def join_tables(self, table):
        if(self.columns != table.get_columns()):
            ex = TL_ErrorWrapper(TL_ErrorCodes.UNEVEN_TABLES)
            raise TL_Error(ex.message, ex.error_code)
        for i in range(0, table.get_rows()):
            row_data = table.get_row_data(i)
            for j in range(0, len(row_data)):
                self.contents[self.header_index[j]] = np.append(self.contents[self.header_index[j]], row_data[j])
            self.rows += 1

    def remove_column(self, field):
        if(type(field) is str):
            if(field not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
        elif(type(field) is int):
            if(0 > field or field >= self.columns):
                ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_COLUMN_INDEX)
                raise TL_Error(ex.message, ex.error_code)
            field = self.header_index[field]
        del self.contents[field]
        self.header_index.remove(field)
        self.columns -= 1
        
    def remove_row(self, idx):
        if(0 > idx or idx >= self.columns):
            ex = TL_ErrorWrapper(TL_ErrorCodes.INVALID_ROW_INDEX)
            raise TL_Error(ex.message, ex.error_code)
        for i in range(0, self.columns):
            self.contents[self.header_index[i]] = np.delete(self.contents[self.header_index[i]], idx)
        self.rows -= 1
    
    def rearrange_header(self, new_header_index):
        if(len(new_header_index) != len(self.header_index)):
            ex = TL_ErrorWrapper(TL_ErrorCodes.UNEVEN_NEW_HEADER)
            raise TL_Error(ex.message, ex.error_code)
        for i in range(0, len(new_header_index)):
            if(new_header_index[i] not in self.contents):
                ex = TL_ErrorWrapper(TL_ErrorCodes.FIELD_NOT_FOUND)
                raise TL_Error(ex.message, ex.error_code)
            self.header_index[i] = new_header_index[i]