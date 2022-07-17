import sys

import PDFDownload as gf
from PDFDownload import check_convert_date

sys.path.insert(0, '../utilities/ConfigLoader')

import ConfigLoader as cl

def main():
    main_config = cl.Config('./config/PDFDownload.cl')
        
    # from date to date exclusive
    start_date = main_config.get_value('StartDate')
    end_date = main_config.get_value('EndDate')
    start_date = check_convert_date(start_date)
    end_date = check_convert_date(end_date)

    handler = gf.PDF_Downloader(start_date, end_date, main_config)
    out_filename = main_config.get_value('GetNamesFilename') 

    while(handler.current_date.timestamp() < handler.finish_date.timestamp()):
        handler.generate_filename()
        handler.append_name()
        handler.next_day()

    handler.save_out_filenames(out_filename)

    return 0

main()