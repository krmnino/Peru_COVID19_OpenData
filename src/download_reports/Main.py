import sys

import PDFDownload as gf
from PDFDownload import check_convert_date

sys.path.insert(0, '../utilities')

import ConfigUtility as cu

def main():
    main_config = cu.Config('./config/PDFDownload.cl')
    
    # from date to date exclusive
    start_date = main_config.get_value('StartDate')
    end_date = main_config.get_value('EndDate')
    start_date = check_convert_date(start_date)
    end_date = check_convert_date(end_date)

    handler = gf.PDF_Downloader(start_date, end_date, main_config)

    while(handler.current_date.timestamp() < handler.finish_date.timestamp()):
        handler.generate_filename()
        handler.generate_url()
        handler.download_pdf()
        handler.next_day()

    return 0

main()