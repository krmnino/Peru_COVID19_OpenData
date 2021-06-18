import sys
import wget
import os

from datetime import datetime, timedelta

sys.path.insert(0, '../utilities')

import ConfigUtility as cu

class PDF_Downloader:
    def __init__(self, sdate, fdate):
        self.start_date = sdate
        self.finish_date = fdate
        self.current_date = self.start_date
        self.current_url = ''
        self.current_filename = ''
        self.config = cu.Config('./PDFDownload.dat')
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
        try:
            wget.download(self.current_url, out=os.path.abspath(self.config.get_value('PDF_Path')) + '/' + self.current_filename)
        except:
            print('Could not download PDF from url')
            pass

    def append_name(self):
        self.out_filenames.append(self.current_filename)

    def save_out_filenames(self, list_filename):
        with open(list_filename, 'w') as file:
            for i in range(0, len(self.out_filenames)):
                file.write(self.out_filenames[i] + '\n')

