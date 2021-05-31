import numpy as np
import sys
import copy

class Table:
    def __init__(self, *args, **kwargs):
        self.filename = ''
        self.header_index = {}
        self.contents = {}
        self.rows = 0
        self.columns = 0
        self.header = True
        if(len(args) == 0):
            pass
        elif(args[0] == 'l'):
            self.filename = kwargs['filename']
            with open(self.filename, 'r') as file:
                for line in file:
                    if self.header:
                        header_split = line.split(',')
                        for i, elem in enumerate(header_split):
                            self.header_index[i] = elem.replace('\n', '')
                            self.columns += 1
                        self.header = False
                        continue
                    line_split = line.split(',')
                    for i, elem in enumerate(line_split):
                        try:
                            if(elem.find('.') == -1):
                                convert_elem = int(elem)
                            else:
                                convert_elem = float(elem)
                        except:
                            convert_elem = str(elem).replace('\n', '')
                            pass
                        if self.header_index[i] not in self.contents.keys():
                            self.contents[self.header_index[i]] = np.array([convert_elem])
                        else:
                            self.contents[self.header_index[i]] = np.append(self.contents[self.header_index[i]], convert_elem)
                    self.rows += 1
        elif(args[0] == 'c'):
            self.filename = kwargs['table'].filename
            self.header_index = copy.deepcopy(kwargs['table'].header_index)
            self.contents = copy.deepcopy(kwargs['table'].contents)
            self.rows = kwargs['table'].rows
            self.columns = kwargs['table'].columns
            self.header = kwargs['table'].header

    def get_fields(self):
        return [i for i in self.contents]

    def get_column(self, field):
        return self.contents[field]

    def get_latest_entry(self):
        out = {}
        for i in self.contents:
            out[i] = self.contents[i][self.rows-1]
        return out

    def set_header_index(self, new_header_index):
        self.header_index = new_header_index
        self.columns = len(self.header_index)
        for i in self.header_index.keys():
            self.contents[i] = np.array([])
    
    def append_entry(self, data):
        if(len(self.header_index) == 0):
            sys.exit('The header is empty. Set a header first before adding entry.')
        for i in self.contents:
            self.contents[i] = np.append(self.contents[i], data[i])
        self.rows += 1

    def save_as_csv(self, path):
        with open(path, 'w') as file:
            out = ''
            for i in range(0, self.columns):
                file.write(self.header_index[i])
                if(i != self.columns - 1):
                    file.write(',')
                else:
                    file.write('\n')
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    file.write(str(self.contents[self.header_index[j]][i]))
                    if(j != self.columns - 1):
                        file.write(',')
                    else:
                        file.write('\n')

    def compute_add_column(self, col_idx, function, key):
        new_column = np.array([])
        for i in range(0, self.rows):
            pack_columns = []
            for j in range(0, len(col_idx)):
                pack_columns.append(self.contents[col_idx[j]])
            new_column = np.append(new_column, function(i, pack_columns))
        self.contents[key] = new_column
        self.header_index[self.columns] = key
        self.columns += 1

    def rearrange_header_index(self, new_header_index):
        if(len(new_header_index) != len(self.header_index)):
            sys.exit('The length new header index is not equal to the length of the current header index.')
        for i in new_header_index:
            if(i >= self.columns):
                sys.exit('The index ' + str(i) + 'is greater than the number of colums (' + str(self.columns) + ' cols).')
        for i in new_header_index.values():
            if(i not in self.header_index.values()):
                sys.exit('The field ' + str(i) + 'does not exist.')
        self.header_index = new_header_index

    def col_row_query(self, col, row):
        return self.contents[col][row]
