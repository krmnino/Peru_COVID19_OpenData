import numpy as np
import sys
import copy

class Table:
    def __init__(self, *args, **kwargs):
        self.filename = ''
        self.header_index = []
        self.contents = {}
        self.rows = 0
        self.columns = 0
        self.header = True
        self.delimiter = ','
        if(len(args) == 0):
            pass
        elif(args[0] == 'l'):
            self.filename = kwargs['filename']
            self.delimiter = kwargs['delimiter']
            with open(self.filename, 'r') as file:
                for line in file:
                    if self.header:
                        header_split = line.split(self.delimiter)
                        for i, elem in enumerate(header_split):
                            self.header_index.append(elem.replace('\n', ''))
                            self.contents[self.header_index[i]] = np.array([], dtype='int64')
                            self.columns += 1
                        self.header = False
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
            self.header = kwargs['table'].header
            self.delimiter = kwargs['table'].delimiter
        elif(args[0] == 'n'):
            self.filename = kwargs['filename']
            self.header_index = copy.deepcopy(kwargs['header_index'])
            self.columns = len(self.header_index)
            self.header = True
            self.delimiter = kwargs['delimiter']
            for i in range(0, self.columns):
                self.contents[self.header_index[i]] = np.array([])

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_fields(self):
        return self.header_index

    def get_column_data(self, field):
        return self.contents[field]

    def get_row_data(self, idx):
        out = {}
        for i in self.contents:
            out[i] = self.contents[i][idx]
        return out

    def get_end_row(self):
        out = {}
        for i in self.contents:
            out[i] = self.contents[i][self.rows-1]
        return out

    def get_cell_data(self, col, row):
        return self.contents[col][row]

    def set_header_index(self, new_header_index):
        self.header_index = new_header_index
        self.columns = len(self.header_index)
        for i in self.header_index.keys():
            self.contents[i] = np.array([])

    def set_filename(self, filename):
        self.filename = filename
    
    def set_delimiter(self, delim):
        self.delimiter = delim

    def append_begin_row(self, data):
        if(len(self.header_index) == 0):
            sys.exit('The header is empty. Set a header first before adding entry.')
        for i, elem in enumerate(self.contents):
            self.contents[elem] = np.insert(self.contents[elem], 0, data[i])
        self.rows += 1
    
    def append_end_row(self, data):
        if(len(self.header_index) == 0):
            sys.exit('The header is empty. Set a header first before adding entry.')
        for i, elem in enumerate(self.contents):
            self.contents[elem] = np.append(self.contents[elem], data[i])
        self.rows += 1

    def update_cell_data(self, col, row, data):
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

    def compute_new_column(self, new_col_key, cols_names, function):
        table_columns = []
        for i in cols_names:
            table_columns.append(self.contents[i])
        new_column = np.array([])
        for i in range(0, self.rows):
            new_column = np.append(new_column, function(i, table_columns))
        self.header_index.append(new_col_key)
        self.contents[new_col_key] = new_column
        self.columns += 1

    def compute_update_column(self, col_key, cols_names, function):
        table_columns = []
        for i in cols_names:
            table_columns.append(self.contents[i])
        for i in range(0, self.rows):
            self.contents[col_key][i] = function(i, table_columns)        

    def rearrange_header_index(self, input_header_index):
        if(len(input_header_index) != len(self.header_index)):
            sys.exit('The length new header index is not equal to the length of the current header index.')
        for i in input_header_index:
            if(i not in self.header_index):
                sys.exit('The field ' + str(i) + 'does not exist.')
        self.header_index = input_header_index