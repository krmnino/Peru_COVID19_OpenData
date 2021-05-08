import numpy as np
import sys

class Table:
    def __init__(self, path):
        self.filename = path
        self.header_index = {}
        self.contents = {}
        self.rows = 0
        self.columns = 0
        header = True
        with open(self.filename, 'r') as file:
            for line in file:
                if header:
                    header_split = line.split(',')
                    for i, elem in enumerate(header_split):
                        self.header_index[i] = elem.replace('\n', '')
                        self.columns += 1
                    header = False
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

    def get_fields(self):
        return [i for i in self.contents]

    def get_column(self, field):
        return self.contents[field]

    def get_latest_entry(self):
        out = {}
        for i in self.contents:
            out[i] = self.contents[i][self.rows-1]
        return out
    
    def append_entry(self, data):
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
            return -1
        for i in new_header_index:
            if(i >= self.columns):
                sys.exit('The index ' + str(i) + 'is greater than the number of colums (' + str(self.columns) + ' cols).')
                return -1
        for i in new_header_index.values():
            if(i not in self.header_index.values()):
                sys.exit('The field ' + str(i) + 'does not exist.')
                return -1
        self.header_index = new_header_index


        
