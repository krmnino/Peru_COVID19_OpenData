import sys

from numpy.lib.function_base import place

class Text:
    def __init__(self, path):
        self.text = ''
        self.placeholder_position = {}
        self.placeholder_indexes = {} 
        self.entries = 0
        with open(path) as file:
            for line in file:
                self.text += line
            for i in range(0, len(self.text)):
                if(self.text[i] == '$'):
                    self.placeholder_position[self.entries] = i
                    self.placeholder_indexes[i] = ''
                    self.entries += 1
        self.inited = True
    
    def get_placeholder_indexes(self):
        return [i for i in self.placeholder_indexes.keys()]

    def get_surroundings_by_position(self, position):
        if(position < 0):
            sys.exit('Passed index cannot be negative.')
        if(position not in self.placeholder_position.keys()):
            sys.exit('Passed index does not correspond to a placeholder.')
        index = self.placeholder_position[position]
        lower_bound = index - 10
        while(lower_bound < 0):
            lower_bound += 1
        upper_bound = index + 10
        while(lower_bound > len(self.text)):
            lower_bound -= 1
        print(self.text[lower_bound:upper_bound])

    def get_surroundings_by_index(self, index):
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

    def remove_placeholder_by_position(self, position):
        index = self.placeholder_position[position]
        del self.placeholder_position[position]
        del self.placeholder_indexes[index]
        self.entries -= 1

    def remove_placeholder_by_index(self, index):
        position = 0
        for i in self.placeholder_indexes.keys():
            if(index == i):
                break
            position += 1
        del self.placeholder_position[position]
        del self.placeholder_indexes[index]
        self.entries -= 1

    # Set placeholder value by position
    def set_ph_value_by_position(self, position, value):
        if(position < 0):
            sys.exit('Passed position cannot be negative.')
        if(position not in self.placeholder_position.keys()):
            sys.exit('Passed position does not correspond to a placeholder.')
        if(type(value) != type('')):
            sys.exit('Value must be of type string')
        self.placeholder_indexes[self.placeholder_position[position]] = value

    # Set placeholder value by index
    def set_ph_value_by_index(self, index, value):
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