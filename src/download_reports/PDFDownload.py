import sys
import wget

from datetime import datetime, timedelta

class PDF_Downloader:
    def __init__(self, sdate, fdate, main_config):
        self.start_date = sdate
        self.finish_date = fdate
        self.current_date = self.start_date
        self.current_url = ''
        self.current_filename = ''
        self.config = main_config
        self.out_filenames = []

    def generate_filename(self):
        base_file = self.config.get_value('PDF_NameBase')
        y = self.current_date.strftime('%y')
        m = self.current_date.strftime('%m')
        d = self.current_date.strftime('%d')
        self.current_filename = base_file + d + m + y + '.pdf'

    def next_day(self):
        if(not self.current_date >= self.finish_date):
            self.current_date += timedelta(days=1) 

    def generate_url(self):
        base_url = self.config.get_value('PDF_URL_Base')
        self.current_url = base_url + self.current_filename

    def download_pdf(self):
        print('\nDownloading:', self.current_filename)
        # Get top level directory based on platform
        top_level_directory = ''
        if(sys.platform == 'win32'):
            top_level_directory = self.config.get_value('WindowsTopLevel')
        else:
            top_level_directory = self.config.get_value('LinuxTopLevel')
        try:
            abs_path = top_level_directory + \
                       self.config.get_value('PDF_Path') + \
                       self.current_filename
            wget.download(self.current_url, out=abs_path)
        except Exception as e:
            print('Could not download PDF from url')
            print(str(e))
            pass

    def append_name(self):
        self.out_filenames.append(self.current_filename)

    def save_out_filenames(self, list_filename):
        # Get top level directory based on platform
        top_level_directory = ''
        if(sys.platform == 'win32'):
            top_level_directory = self.config.get_value('WindowsTopLevel')
        else:
            top_level_directory = self.config.get_value('LinuxTopLevel')
        abs_path = top_level_directory + \
                    self.config.get_value('PDF_Path') + \
                    list_filename
        with open(abs_path, 'w') as file:
            for i in range(0, len(self.out_filenames)):
                file.write(self.out_filenames[i] + '\n')

def check_convert_date(input_date):
    try:
        date_conv = datetime.strptime(input_date, '%Y-%m-%d').date()
        date_ret = datetime(date_conv.year, date_conv.month, date_conv.day)
    except:
        sys.exit('Invalid input date. Exiting...')
    return date_ret