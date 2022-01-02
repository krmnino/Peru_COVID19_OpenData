class Config:
    def __init__(self, path):
        self.contents = {}
        self.entries = 0
        buffer = ''
        with open(path) as file:
            for line in file:
                if(line[0] == '#'):
                    continue
                buffer += line
        buffer = buffer.replace('\n', '')
        buffer = buffer.replace('\t', '')
        split_buffer = buffer.split(';')
        for entry in split_buffer:
            if(len(entry) == 0):
                continue
            key_val = entry.split('=')
            key = self.__remove_side_spaces(key_val[0])
            value = self.__process_value(key_val[1])
            self.contents[key] = value
            self.entries += 1
        self.inited = True    

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
                    split_list[i] = raw_string
            return split_list
        else:
            raw_string = self.__remove_side_spaces(raw_string)
            try:
                to_float = float(raw_string)
                return to_float
            except:
                return raw_string


    def list_keys(self):
        return [i for i in self.contents.keys()]

    def get_value(self, key):
        return self.contents[key]

    def get_n_entries(self):
        return self.entries

