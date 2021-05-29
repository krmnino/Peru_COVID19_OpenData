class Config:
    def __init__(self, path):
        self.contents = {}
        self.entries = len(self.contents)
        with open(path) as file:
            for line in file:
                line_split = line.split('=')
                self.contents[line_split[0]] = line_split[1].replace('\n', '')
                self.entries += 1
        self.inited = True
    
    def list_keys(self):
        return [i for i in self.contents.keys()]

    def get_value(self, key):
        return self.contents[key]

    def add_entry(self, key, value):
        if(key not in self.contents.keys()):
            self.contents[key] = value