import PDFDownload as gf
from datetime import datetime, timedelta, date

# from date to date exclusive
start = datetime(2021, 5, 1)
end = datetime(2021, 5, 10)

handler = gf.PDF_Downloader(start, end)

while(handler.current_date.timestamp() < handler.finish_date.timestamp()):
    handler.generate_filename()
    handler.generate_url()
    handler.download_pdf()
    handler.next_day()