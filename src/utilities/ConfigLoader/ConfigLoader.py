import enum
import os.path

class CL_ErrorCodes(enum.Enum):
    OK = 0
    SEMICOLON = 1
    EQUALS_SIGN = 2
    KEY_NOT_FOUND = 3
    ADD_KEY_REPEAT = 4
    FAILED_2_OPEN = 5

class CL_Error(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.err_code = error_code

class CL_ErrorWrapper:
    def __init__(self, error_code):
        self.error_code = error_code
        if(self.error_code == CL_ErrorCodes.OK):
            self.message = ''
        elif(self.error_code == CL_ErrorCodes.SEMICOLON):
            self.message = 'Missing semicolon in config file.'
        elif(self.error_code == CL_ErrorCodes.EQUALS_SIGN):
            self.message = 'Missing equals sign at an entry in config file.'
        elif(self.error_code == CL_ErrorCodes.KEY_NOT_FOUND):
            self.message = 'Key not found in config file.'
        elif(self.error_code == CL_ErrorCodes.ADD_KEY_REPEAT):
            self.message = 'Key already exists in config file.'
        elif(self.error_code == CL_ErrorCodes.FAILED_2_OPEN):
            self.message = 'Could not open/find specified config file.'
        else:
            self.message = 'Undefinded error.'

class Config:        
    def __init__(self, path=''):
        if(path == ''):
            self.contents = {}
            self.entries = 0
        else:
            self.contents = {}
            self.entries = 0
            buffer = ''
            if(not os.path.isfile(path)):
                ex = CL_ErrorWrapper(CL_ErrorCodes.FAILED_2_OPEN)
                raise CL_Error(ex.message, ex.error_code)
            with open(path) as file:
                for line in file:
                    line = line.replace('\n', '')
                    if(len(line) == 0):
                        continue
                    if(line[0] == '#'):
                        continue
                    if(line[len(line) - 1] != ';'):
                        if(line[len(line) - 1] == ','):
                            buffer += line
                            continue
                        else:
                            ex = CL_ErrorWrapper(CL_ErrorCodes.SEMICOLON)
                            raise CL_Error(ex.message, ex.error_code)
                    buffer += line
            buffer = buffer.replace('\t', '')
            split_buffer = buffer.split(';')
            for entry in split_buffer:
                if(len(entry) == 0):
                    continue
                key_val = entry.split('=')
                if(len(key_val) != 2):
                    ex = CL_ErrorWrapper(CL_ErrorCodes.EQUALS_SIGN)
                    raise CL_Error(ex.message, ex.error_code)
                key = self.__remove_side_spaces(key_val[0])
                value = self.__process_value(key_val[1])
                if(key in self.contents):
                    self.contents[key] = value
                else:    
                    self.contents[key] = value
                    self.entries += 1

    def __remove_side_spaces(self, raw_string):
        left_idx = 0
        right_idx = 0
        for i in range(0, len(raw_string)):
            if(raw_string[i] != ' '):
                left_idx = i
                break
        raw_string = raw_string[left_idx:]
        for i in range(len(raw_string) - 1, -1, -1):
            if(raw_string[i] != ' '):
                if(i == len(raw_string) - 1):
                    right_idx = len(raw_string)
                else:
                    right_idx = i + 1
                break
        raw_string = raw_string[:right_idx]
        return raw_string

    def __process_value(self, raw_string):
        raw_string = self.__remove_side_spaces(raw_string)
        if(raw_string[0] == '[' and raw_string[len(raw_string) - 1] == ']'):
            raw_string = raw_string[1:len(raw_string)-1]
            split_list = raw_string.split(',')
            for i in range(0, len(split_list)):
                split_list[i] = self.__remove_side_spaces(split_list[i])
                try:
                    to_float = float(split_list[i])
                    split_list[i] = to_float
                except:
                    continue
            return split_list
        else:
            raw_string = self.__remove_side_spaces(raw_string)
            try:
                to_float = float(raw_string)
                return to_float
            except:
                return raw_string

    def get_n_entries(self):
        return self.entries

    def get_all_keys(self):
        return [i for i in self.contents.keys()]

    def get_value(self, key):
        if(key not in self.contents):
            ex = CL_ErrorWrapper(CL_ErrorCodes.KEY_NOT_FOUND)
            raise CL_Error(ex.message, ex.error_code)
        return self.contents[key]

    def get_all_key_values(self):
        key_vals = []
        keys = [i for i in self.contents.keys()]
        for i in range(0, self.entries):
            key_vals.append((keys[i], self.get_value(keys[i])))
        return key_vals

    def add_entry(self, key, value):
        if(key in self.contents):
            ex = CL_ErrorWrapper(CL_ErrorCodes.ADD_KEY_REPEAT)
            raise CL_Error(ex.message, ex.error_code)
        self.contents[key] = value
        self.entries += 1

    def edit_value(self, key, value):
        if(key not in self.contents):
            ex = CL_ErrorWrapper(CL_ErrorCodes.KEY_NOT_FOUND)
            raise CL_Error(ex.message, ex.error_code)
        self.contents[key] = value

    def save_config(self, path):
        with open(path, 'w') as file:
            keys = [i for i in self.contents.keys()]
            for i in range(0, self.entries):
                file.write(keys[i] + ' = ')
                file.write(str(self.contents[keys[i]]) + ';\n')
