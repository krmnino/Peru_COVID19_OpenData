import PDFDownload as gf
from datetime import datetime, timedelta

end = datetime.now() - timedelta(days=10)
start = end - timedelta(days=15)

handler = gf.PDF_Downloader(start, end)

while(handler.current_date <= handler.finish_date):
    handler.generate_filename()
    handler.generate_url()
    handler.download_pdf()
    handler.next_day()