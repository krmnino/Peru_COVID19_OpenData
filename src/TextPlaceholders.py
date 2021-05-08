import sys
class Text:
    def __init__(self, path):
        self.text = ''
        self.placeholder_indexes = {} 
        self.entries = len(self.placeholder_indexes)
        with open(path) as file:
            for line in file:
                self.text += line
                self.entries += 1
            for i in range(0, len(self.text)):
                if(self.text[i] == '$'):
                    self.placeholder_indexes[i] = ''
        self.inited = True
    
    def get_placeholder_indexes(self):
        return [i for i in self.placeholder_indexes.keys()]

    def get_surroundings(self, index):
        if(index < 0):
            sys.exit('Passed index cannot be negative.')
        if(index not in self.placeholder_indexes.keys()):
            sys.exit('Passed index does not correspond to a placeholder.')
        lower_bound = index - 10
        while(lower_bound < 0):
            lower_bound += 1
        upper_bound = index + 10
        while(lower_bound > len(self.text)):
            lower_bound -= 1
        print(self.text[lower_bound:upper_bound])

    def set_placeholder_value(self, index, value):
        if(index < 0):
            sys.exit('Passed index cannot be negative.')
        if(index not in self.placeholder_indexes.keys()):
            sys.exit('Passed index does not correspond to a placeholder.')
        if(type(value) != type('')):
            sys.exit('Value must be of type string')
        self.placeholder_indexes[index] = value

    def process_text(self):
        out = ''
        for i in range(0, len(self.text)):
            if(i in self.placeholder_indexes.keys()):
                if(self.placeholder_indexes[i] == ''):
                    out += '$'
                else:
                    out += self.placeholder_indexes[i]
            else:
                out += self.text[i]
        return out
