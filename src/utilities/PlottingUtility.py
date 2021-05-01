import sys

class Plot:
    def __init__(self, num_sp, colors_sp, titles_sp, enable_rolling_avg_sp, type_sp, x_label_sp, y_label_sp, x_data, y_data):
        self.num_subplots = num_sp
        
        if(self.num_subplots != len(colors_sp)):
            sys.exit('num_sublots does not equal colors_sp')
        else:
            self.colors_subplots = colors_sp
        
        if(self.num_subplots != len(titles_sp)):
            sys.exit('num_sublots does not equal titles_sp')
        else:
            self.titles_subplots = titles_sp

        if(self.num_subplots != len(enable_rolling_avg_sp)):
            sys.exit('num_sublots does not equal enable_rolling_avg_sp')
        else:
            self.enable_rolling_avg_subplots = enable_rolling_avg_sp

        if(self.num_subplots != len(type_sp)):
            sys.exit('num_sublots does not equal type_sp')
        else:
            self.type_subplots = type_sp

        if(self.num_subplots != len(x_label_sp)):
            sys.exit('num_sublots does not equal x_label_sp')
        else:
            self.x_label_subplots = x_label_sp

        if(self.num_subplots != len(y_label_sp)):
            sys.exit('num_sublots does not equal y_label_sp')
        else:
            self.y_label_subplots = y_label_sp

        if(self.num_subplots != len(x_data)):
            sys.exit('num_sublots does not equal x_data')
        else:
            self.x_data = x_data

        if(self.num_subplots != len(y_data)):
            sys.exit('num_sublots does not equal y_data')
        else:
            self.y_data = y_data

        print(self.num_subplots)
        print(self.colors_subplots)
        print(self.titles_subplots)
        print(self.enable_rolling_avg_subplots)
        print(self.type_subplots)
        print(self.x_label_subplots)
        print(self.y_label_subplots)
        #print(self.x_data)
        #print(self.y_data)

