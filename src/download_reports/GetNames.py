import PDFDownload as gf
from datetime import datetime, timedelta, date

# from date to date exclusive
start = datetime(2021, 5, 1)
end = datetime(2021, 5, 10)

handler = gf.PDF_Downloader(start, end)
out_filename = 'test.dat' 

while(handler.current_date.timestamp() <= handler.finish_date.timestamp()):
    handler.generate_filename()
    handler.append_name()
    handler.next_day()

handler.save_out_filenames(out_filename)