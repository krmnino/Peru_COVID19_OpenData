import sys
from pdf2image import convert_from_path
import numpy as np
import cv2
from PIL import Image
from PIL import ImageOps 
from PIL import ImageEnhance
import pytesseract

sys.path.insert(0, '../utilities')

import ConfigUtility as cu
import DataUtility as du

if(sys.platform == 'win32'):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#####################################################################################################

def print_data_table(data):
    print('\n=====================================================')
    idx = 0
    keys = list(data.keys())
    for i, val in enumerate(data):
        if(data[val]):
            print('%2s'%(idx), '%15s'%(keys[i] + ':'), '%10s'%('Y'))
        else:
            print('%2s'%(idx), '%15s'%(keys[i] + ':'), '%10s'%('N'))
        idx += 1
    print('=====================================================')
    return 0

#####################################################################################################

def select_read_tables_menu(data):
    while(True):
        print_data_table(data)
        user = input('Edit numbers by entering index [0-' + str(len(data) - 1) +']. Proceed? [Y/N]: ')
        if(user == 'N' or user == 'n'):
            sys.exit('Exiting...')
        elif(user == 'Y' or user == 'y'):
            break
        elif(user.isnumeric()):
            num_user = int(user)
            if(num_user < 0 or num_user > len(data)):
                print('Wrong index. Index must be [0-' + str(len(data) - 1) +'].')
                continue
            data_keys = list(data.keys())
            new_data = input(data_keys[num_user] + ': ')        
            if(new_data == 'Y' or new_data == 'y'):
                data[data_keys[num_user]] = True
                continue
            elif(new_data == 'N' or new_data == 'n'):
                data[data_keys[num_user]] = False
                continue
            else:
                print('Wrong selection. Must be Y/N.')
                continue
        else:
            print('Wrong input. Try Again.')
            continue
    return data

#####################################################################################################

def process_pa_depto(main_config, pdf_path, showimg=False):
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = main_config.get_value('WindowsTopLevel')
    else:
        top_level_directory = main_config.get_value('LinuxTopLevel')
    # Extract page from PDF file
    pdf_image = convert_from_path(pdf_path,
                                 first_page=int(main_config.get_value('PADepto_PDFPage')),
                                 last_page=int(main_config.get_value('PADepto_PDFPage')),
                                 dpi=200)[0]
    # Apply postprocessing to image
    pdf_image = ImageOps.invert(pdf_image)
    pdf_image = ImageOps.grayscale(pdf_image)
    enhancer = ImageEnhance.Contrast(pdf_image)
    pdf_image = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_pdf_image = np.array(pdf_image)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_pdf_image = cv2.resize(cv2_pdf_image, (w_width, w_height))

    # Get department names index
    dept_index = cu.Config(top_level_directory + main_config.get_value('DepartmentsIndex'))
    
    # Parse data in image column by column 
    n_cols = int(main_config.get_value('PADepto_RTCols'))
    col_names = main_config.get_value('PADepto_RTHdr')
    parsed_columns = []
    for i in range(0, n_cols):
        # Append department names columns
        if(i == 0):
            pdf_image_data = []
            n_rows = int(main_config.get_value('PADepto_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(dept_index.get_value(str(j)))
            parsed_columns.append(pdf_image_data)
            continue
        # Append department total placeholder values
        if(i == 4):
            pdf_image_data = []
            n_rows = int(main_config.get_value('PADepto_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(0)
            parsed_columns.append(pdf_image_data)
            continue
        # Select area and crop image
        print('PADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols))
        bounds_pdf_image = cv2.selectROI('PADepto', cv2_pdf_image, False, False)
        cv2.destroyWindow('PADepto')
        col_pdf_image = cv2_pdf_image[int(bounds_pdf_image[1]):int(bounds_pdf_image[1]+bounds_pdf_image[3]),
                                      int(bounds_pdf_image[0]):int(bounds_pdf_image[0]+bounds_pdf_image[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'PADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols)
            cv2.imshow(window_name, col_pdf_image)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        pil_pdf_image = Image.fromarray(col_pdf_image)
        # Perform OCR in PIL image with pytesseract
        pdf_image_data = pytesseract.image_to_string(pil_pdf_image)
        pdf_image_data = pdf_image_data.split('\n')
        parsed_columns.append(pdf_image_data)
    
    # Find column with most elements
    max_col_len = 0
    for i in range(0, len(parsed_columns)):
        if(max_col_len < len(parsed_columns[i])):
            max_col_len = len(parsed_columns[i])

    # Create new Table and add each row of data
    raw_table_abs_path = top_level_directory + main_config.get_value('PADepto_RT')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names,
        delimiter=';'
    )

    # Fill table with data
    for i in range(0, max_col_len):
        new_row = []
        for j in range(0, len(col_names)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(raw_table_abs_path)
    print('PADepto - Done.')
    return 0

#####################################################################################################

def process_ca_depto(main_config, pdf_path, showimg=False):
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = main_config.get_value('WindowsTopLevel')
    else:
        top_level_directory = main_config.get_value('LinuxTopLevel')
    # Extract page from PDF file
    pdf_image = convert_from_path(pdf_path,
                                 first_page=int(main_config.get_value('CADepto_PDFPage')),
                                 last_page=int(main_config.get_value('CADepto_PDFPage')),
                                 dpi=200)[0]
    # Apply postprocessing to image
    pdf_image = ImageOps.invert(pdf_image)
    pdf_image = ImageOps.grayscale(pdf_image)
    enhancer = ImageEnhance.Contrast(pdf_image)
    pdf_image = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_pdf_image = np.array(pdf_image)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_pdf_image = cv2.resize(cv2_pdf_image, (w_width, w_height))

    # Get department names index
    dept_index = cu.Config(top_level_directory + main_config.get_value('DepartmentsIndex'))

    # Parse data in image column by column 
    n_cols = int(main_config.get_value('CADepto_RTCols'))
    col_names = main_config.get_value('CADepto_RTHdr')
    parsed_columns = []
    for i in range(0, n_cols):
        # Append department names columns
        if(i == 0):
            pdf_image_data = []
            n_rows = int(main_config.get_value('CADepto_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(dept_index.get_value(str(j)))
            parsed_columns.append(pdf_image_data)
            continue
        # Append department total placeholder values
        if(i == 4):
            pdf_image_data = []
            n_rows = int(main_config.get_value('CADepto_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(0)
            parsed_columns.append(pdf_image_data)
            continue
        # Select area and crop image
        print('CADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols))
        bounds_pdf_image = cv2.selectROI('CADepto', cv2_pdf_image, False, False)
        cv2.destroyWindow('CADepto')
        col_pdf_image = cv2_pdf_image[int(bounds_pdf_image[1]):int(bounds_pdf_image[1]+bounds_pdf_image[3]),
                                    int(bounds_pdf_image[0]):int(bounds_pdf_image[0]+bounds_pdf_image[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols)
            cv2.imshow(window_name, col_pdf_image)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        pil_pdf_image = Image.fromarray(col_pdf_image)
        # Perform OCR in PIL image with pytesseract and append column
        pdf_image_data = pytesseract.image_to_string(pil_pdf_image)
        pdf_image_data = pdf_image_data.split('\n')
        parsed_columns.append(pdf_image_data)

    # Find column with most elements
    max_col_len = 0
    for i in range(0, len(parsed_columns)):
        if(max_col_len < len(parsed_columns[i])):
            max_col_len = len(parsed_columns[i])

    # Create new Table and add each row of data
    raw_table_abs_path = top_level_directory + main_config.get_value('CADepto_RT')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names,
        delimiter=';'
    )

    # Fill table with data
    for i in range(0, max_col_len):
        new_row = []
        for j in range(0, len(col_names)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(raw_table_abs_path)
    print('CADepto done.')
    return 0

#####################################################################################################

def process_cp_edades(main_config, pdf_path, showimg=False):
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = main_config.get_value('WindowsTopLevel')
    else:
        top_level_directory = main_config.get_value('LinuxTopLevel')
    # Extract page from PDF file
    pdf_image = convert_from_path(pdf_path,
                                 first_page=int(main_config.get_value('CPEdades_PDFPage')),
                                 last_page=int(main_config.get_value('CPEdades_PDFPage')),
                                 dpi=200)[0]
    # Apply postprocessing to image
    pdf_image = ImageOps.invert(pdf_image)
    pdf_image = ImageOps.grayscale(pdf_image)
    enhancer = ImageEnhance.Contrast(pdf_image)
    pdf_image = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_pdf_image = np.array(pdf_image)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_pdf_image = cv2.resize(cv2_pdf_image, (w_width, w_height))

    # Get age group names index
    age_group_index = cu.Config(top_level_directory + main_config.get_value('AgeGroupsIndex'))

    # Parse data in image column by column 
    n_cols = int(main_config.get_value('CPEdades_RTCols'))
    col_names = main_config.get_value('CPEdades_RTHdr')
    parsed_columns = []
    for i in range(0, n_cols):
        # Append age group names columns
        if(i == 0):
            pdf_image_data = []
            n_rows = int(main_config.get_value('CPEdades_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(age_group_index.get_value(str(j)))
            parsed_columns.append(pdf_image_data)
            continue
        # Select area and crop image    
        print('CPEdades - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols))
        bounds_pdf_image = cv2.selectROI('CPEdades', cv2_pdf_image, False, False)
        cv2.destroyWindow('CPEdades')
        col_pdf_image = cv2_pdf_image[int(bounds_pdf_image[1]):int(bounds_pdf_image[1]+bounds_pdf_image[3]),
                                      int(bounds_pdf_image[0]):int(bounds_pdf_image[0]+bounds_pdf_image[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CPEdades - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols)
            cv2.imshow(window_name, col_pdf_image)
            cv2.waitKey(0)
            print('CPEdades done.')
        # Convert opencv2 image back to PIL image
        pil_pdf_image = Image.fromarray(col_pdf_image)
        # Perform OCR in PIL image with pytesseract
        pdf_image_data = pytesseract.image_to_string(pil_pdf_image)
        pdf_image_data = pdf_image_data.split('\n')
        parsed_columns.append(pdf_image_data)
    
    # Find column with most elements
    max_col_len = 0
    for i in range(0, len(parsed_columns)):
        if(max_col_len < len(parsed_columns[i])):
            max_col_len = len(parsed_columns[i])

    # Create new Table and add each row of data
    raw_table_abs_path = top_level_directory + main_config.get_value('CPEdades_RT')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names,
        delimiter=';'
    )

    # Fill table with data
    for i in range(0, max_col_len):
        new_row = []
        for j in range(0, len(col_names)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(raw_table_abs_path)
    print('CPEdades - Done.')
    return 0

#####################################################################################################

def process_ma_depto(main_config, pdf_path, showimg=False):
    # Get top level directory based on platform
    top_level_directory = ''
    if(sys.platform == 'win32'):
        top_level_directory = main_config.get_value('WindowsTopLevel')
    else:
        top_level_directory = main_config.get_value('LinuxTopLevel')
    # Extract page from PDF file
    pdf_image = convert_from_path(pdf_path,
                                 first_page=int(main_config.get_value('MADepto_PDFPage')),
                                 last_page=int(main_config.get_value('MADepto_PDFPage')),
                                  dpi=200)[0]
    # Apply postprocessing to image
    pdf_image = ImageOps.invert(pdf_image)
    pdf_image = ImageOps.grayscale(pdf_image)
    enhancer = ImageEnhance.Contrast(pdf_image)
    pdf_image = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_pdf_image = np.array(pdf_image)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_pdf_image = cv2.resize(cv2_pdf_image, (w_width, w_height))

    # Get department names index
    dept_index = cu.Config(top_level_directory + main_config.get_value('DepartmentsIndex'))

    # Parse data in image column by column 
    n_cols = int(main_config.get_value('MADepto_RTCols'))
    col_names = main_config.get_value('MADepto_RTHdr')
    parsed_columns = []
    for i in range(0, n_cols):
        # Append department names columns
        if(i == 0):
            pdf_image_data = []
            n_rows = int(main_config.get_value('MADepto_RTRows'))
            for j in range(0, n_rows):
                pdf_image_data.append(dept_index.get_value(str(j)))
            parsed_columns.append(pdf_image_data)
            continue
        # Select area and crop image
        print('MADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols))
        bounds_pdf_image = cv2.selectROI('MADepto', cv2_pdf_image, False, False)
        cv2.destroyWindow('MADepto')
        col_pdf_image = cv2_pdf_image[int(bounds_pdf_image[1]):int(bounds_pdf_image[1]+bounds_pdf_image[3]),
                                    int(bounds_pdf_image[0]):int(bounds_pdf_image[0]+bounds_pdf_image[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'MADepto - Col[' + col_names[i] + '] ' + str(i + 1) + '/' + str(n_cols)
            cv2.imshow(window_name, col_pdf_image)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        pil_pdf_image = Image.fromarray(col_pdf_image)
        # Perform OCR in PIL image with pytesseract
        pdf_image_data = pytesseract.image_to_string(pil_pdf_image)
        pdf_image_data = pdf_image_data.split('\n')
        parsed_columns.append(pdf_image_data)
        
    # Find column with most elements
    max_col_len = 0
    for i in range(0, len(parsed_columns)):
        if(max_col_len < len(parsed_columns[i])):
            max_col_len = len(parsed_columns[i])

    # Create new Table and add each row of data
    raw_table_abs_path = top_level_directory + main_config.get_value('MADepto_RT')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names,
        delimiter=';'
    )
    
    # Fill table with data
    for i in range(0, max_col_len):
        new_row = []
        for j in range(0, len(col_names)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(raw_table_abs_path)
    print('MADepto done.')

#####################################################################################################

def process_ca_distr_20(main_config, table_names_config, table_pg_config, pdf_path, showimg=False):
    ca_distr_20 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CADistr20P1')),
                                    last_page=int(table_pg_config.get_value('CADistr20P1')),
                                    dpi=200)[0]
    # Apply postprocessing to image
    ca_distr_20 = ImageOps.invert(ca_distr_20)
    ca_distr_20 = ImageOps.grayscale(ca_distr_20)
    enhancer = ImageEnhance.Contrast(ca_distr_20)
    ca_distr_20 = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_ca_distr_20 = np.array(ca_distr_20)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_ca_distr_20 = cv2.resize(cv2_ca_distr_20, (w_width, w_height))

    # Get district names index
    distr_index = cu.Config(main_config.get_value('DistrictsIndex'))

    n_cols_p1 = int(main_config.get_value('CADistr20P1_RTCols'))
    col_names_p1 = main_config.get_value('CADistr20P2_RTHdr')
    n_cols_p2 = int(main_config.get_value('CADistr20P2_RTCols'))
    col_names_p2 = main_config.get_value('CADistr20P2_RTHdr')
    
    # Parse data in image column by column of first table 
    parsed_columns_p1 = []
    for i in range(0, n_cols_p1):
        # Append district names columns
        if(i == 0):
            ca_distr_20_data = []
            n_rows = int(main_config.get_value('CADistr20P1_RTRows'))
            for j in range(0, n_rows):
                ca_distr_20_data.append(distr_index.get_value(str(j)))
            parsed_columns_p1.append(ca_distr_20_data)
            continue
        # Select area and crop image
        print('CADistr20P1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1))
        bounds_ca_distr_20 = cv2.selectROI('CADistr20P1', cv2_ca_distr_20, False, False)
        cv2.destroyWindow('CADistr20P1')
        col_ca_distr_20 = cv2_ca_distr_20[int(bounds_ca_distr_20[1]):int(bounds_ca_distr_20[1]+bounds_ca_distr_20[3]),
                                          int(bounds_ca_distr_20[0]):int(bounds_ca_distr_20[0]+bounds_ca_distr_20[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CADistr20P1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1)
            cv2.imshow(window_name, col_ca_distr_20)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ca_distr_20 = Image.fromarray(col_ca_distr_20)
        # Perform OCR in PIL image with pytesseract
        ca_distr_20_data = pytesseract.image_to_string(img_ca_distr_20)
        ca_distr_20_data = ca_distr_20_data.split('\n')
        parsed_columns_p1.append(ca_distr_20_data)

    # Parse data in image column by column of second table 
    parsed_columns_p2 = []
    for i in range(0, n_cols_p2):
        # Append district names columns
        if(i == 0):
            ca_distr_20_data = []
            n_rows = int(main_config.get_value('CADistr20P2_RTRows'))
            for j in range(0, n_rows):
                ca_distr_20_data.append(distr_index.get_value(str(j + n_rows)))
            parsed_columns_p2.append(ca_distr_20_data)
            continue
        # Select area and crop image
        print('CADistr20P2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2))
        bounds_ca_distr_20 = cv2.selectROI('CADistr20P2', cv2_ca_distr_20, False, False)
        cv2.destroyWindow('CADistr20P2')
        col_ca_distr_20 = cv2_ca_distr_20[int(bounds_ca_distr_20[1]):int(bounds_ca_distr_20[1]+bounds_ca_distr_20[3]),
                                          int(bounds_ca_distr_20[0]):int(bounds_ca_distr_20[0]+bounds_ca_distr_20[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CADistr20P2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2)
            cv2.imshow(window_name, col_ca_distr_20)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ca_distr_20 = Image.fromarray(col_ca_distr_20)
        # Perform OCR in PIL image with pytesseract
        ca_distr_20_data = pytesseract.image_to_string(img_ca_distr_20)
        ca_distr_20_data = ca_distr_20_data.split('\n')
        parsed_columns_p2.append(ca_distr_20_data)

    # Find column with most elements
    max_col_len_p1 = 0
    for i in range(0, len(parsed_columns_p1)):
        if(max_col_len_p1 < len(parsed_columns_p1[i])):
            max_col_len_p1 = len(parsed_columns_p1[i])
    max_col_len_p2 = 0
    for i in range(0, len(parsed_columns_p2)):
        if(max_col_len_p2 < len(parsed_columns_p2[i])):
            max_col_len_p2 = len(parsed_columns_p2[i])

    # Create new Table and add each row of data from part 1
    raw_table_abs_path = table_names_config.get_value('CADistr20P1')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p1,
        delimiter=';'
    )

    # Fill table with data from part 1
    for i in range(0, max_col_len_p1):
        new_row = []
        for j in range(0, len(col_names_p1)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p1[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p1[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)

    # Create new Table and add each row of data from part 2
    raw_table_abs_path = table_names_config.get_value('CADistr20P2')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p2,
        delimiter=';'
    )
    
    # Fill table with data from part 2
    for i in range(0, max_col_len_p2):
        new_row = []
        for j in range(0, len(col_names_p2)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p2[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p2[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)
    print('CADistr20 done.')

#####################################################################################################

def process_ca_distr_21(main_config, table_names_config, table_pg_config, pdf_path, showimg=False):
    ca_distr_21 = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('CADistr21P1')),
                                    last_page=int(table_pg_config.get_value('CADistr21P1')),
                                    dpi=200)[0]
    # Apply postprocessing to image
    ca_distr_21 = ImageOps.invert(ca_distr_21)
    ca_distr_21 = ImageOps.grayscale(ca_distr_21)
    enhancer = ImageEnhance.Contrast(ca_distr_21)
    ca_distr_21 = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_ca_distr_21 = np.array(ca_distr_21)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_ca_distr_21 = cv2.resize(cv2_ca_distr_21, (w_width, w_height))

    n_cols_p1 = int(main_config.get_value('CADistr21P1_RTCols'))
    col_names_p1 = main_config.get_value('CADistr21P2_RTHdr')
    n_cols_p2 = int(main_config.get_value('CADistr21P2_RTCols'))
    col_names_p2 = main_config.get_value('CADistr21P2_RTHdr')

    # Get district names index
    distr_index = cu.Config(main_config.get_value('DistrictsIndex'))

    # Parse data in image column by column of first table 
    parsed_columns_p1 = []
    for i in range(0, n_cols_p1):
        # Append district names columns
        if(i == 0):
            ca_distr_21_data = []
            n_rows = int(main_config.get_value('CADistr21P1_RTRows'))
            for j in range(0, n_rows):
                ca_distr_21_data.append(distr_index.get_value(str(j)))
            parsed_columns_p1.append(ca_distr_21_data)
            continue
        # Select area and crop image
        print('CADistr21P1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1))
        bounds_ca_distr_21 = cv2.selectROI('CADistr21P1', cv2_ca_distr_21, False, False)
        cv2.destroyWindow('CADistr21P1')
        col_ca_distr_21 = cv2_ca_distr_21[int(bounds_ca_distr_21[1]):int(bounds_ca_distr_21[1]+bounds_ca_distr_21[3]),
                                          int(bounds_ca_distr_21[0]):int(bounds_ca_distr_21[0]+bounds_ca_distr_21[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CADistr21P1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1)
            cv2.imshow(window_name, col_ca_distr_21)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ca_distr_21 = Image.fromarray(col_ca_distr_21)
        # Perform OCR in PIL image with pytesseract
        ca_distr_21_data = pytesseract.image_to_string(img_ca_distr_21)
        ca_distr_21_data = ca_distr_21_data.split('\n')
        parsed_columns_p1.append(ca_distr_21_data)

    # Parse data in image column by column of second table 
    parsed_columns_p2 = []
    for i in range(0, n_cols_p2):
        # Append district names columns
        if(i == 0):
            ca_distr_21_data = []
            n_rows = int(main_config.get_value('CADistr21P2_RTRows'))
            for j in range(0, n_rows):
                ca_distr_21_data.append(distr_index.get_value(str(j + n_rows)))
            parsed_columns_p2.append(ca_distr_21_data)
            continue
        # Select area and crop image
        print('CADistr21P2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2))
        bounds_ca_distr_21 = cv2.selectROI('CADistr21P2', cv2_ca_distr_21, False, False)
        cv2.destroyWindow('CADistr21P2')
        col_ca_distr_21 = cv2_ca_distr_21[int(bounds_ca_distr_21[1]):int(bounds_ca_distr_21[1]+bounds_ca_distr_21[3]),
                                          int(bounds_ca_distr_21[0]):int(bounds_ca_distr_21[0]+bounds_ca_distr_21[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'CADistr21P2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2)
            cv2.imshow(window_name, col_ca_distr_21)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ca_distr_21 = Image.fromarray(col_ca_distr_21)
        # Perform OCR in PIL image with pytesseract
        ca_distr_21_data = pytesseract.image_to_string(img_ca_distr_21)
        ca_distr_21_data = ca_distr_21_data.split('\n')
        parsed_columns_p2.append(ca_distr_21_data)

    # Find column with most elements
    max_col_len_p1 = 0
    for i in range(0, len(parsed_columns_p1)):
        if(max_col_len_p1 < len(parsed_columns_p1[i])):
            max_col_len_p1 = len(parsed_columns_p1[i])
    max_col_len_p2 = 0
    for i in range(0, len(parsed_columns_p2)):
        if(max_col_len_p2 < len(parsed_columns_p2[i])):
            max_col_len_p2 = len(parsed_columns_p2[i])

    # Create new Table and add each row of data from part 1
    raw_table_abs_path = table_names_config.get_value('CADistr21P1')
    n_rows = int(main_config.get_value('CADistr21P1_RTRows'))
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p1,
        delimiter=';'
    )

    # Fill table with data from part 1
    for i in range(0, max_col_len_p1):
        new_row = []
        for j in range(0, len(col_names_p1)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p1[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p1[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)

    # Create new Table and add each row of data from part 2
    raw_table_abs_path = table_names_config.get_value('CADistr21P2')
    n_rows = int(main_config.get_value('CADistr21P2_RTRows'))
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p2,
        delimiter=';'
    )

    # Fill table with data from part 2
    for i in range(0, max_col_len_p2):
        new_row = []
        for j in range(0, len(col_names_p2)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p2[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p2[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)
    print('CADistr21 done.')

#####################################################################################################

def process_ma_distr(main_config, table_names_config, table_pg_config, pdf_path, showimg=False):
    ma_distr = convert_from_path(pdf_path,
                                    first_page=int(table_pg_config.get_value('MADistrP1')),
                                    last_page=int(table_pg_config.get_value('MADistrP1')),
                                    dpi=200)[0]
    # Apply postprocessing to image
    ma_distr = ImageOps.invert(ma_distr)
    ma_distr = ImageOps.grayscale(ma_distr)
    enhancer = ImageEnhance.Contrast(ma_distr)
    ma_distr = enhancer.enhance(1.5)
    # Convert PIL image to opencv2 image
    cv2_ma_distr = np.array(ma_distr)
    # Resize image to fit in 1080p screen
    w_width = int(main_config.get_value('WindowWidth'))
    w_height = int(main_config.get_value('WindowHeight'))
    cv2_ma_distr = cv2.resize(cv2_ma_distr, (w_width, w_height))

    n_cols_p1 = int(main_config.get_value('MADistrP1_RTCols'))
    col_names_p1 = main_config.get_value('MADistrP1_RTHdr')
    n_cols_p2 = int(main_config.get_value('MADistrP2_RTCols'))
    col_names_p2 = main_config.get_value('MADistrP2_RTHdr')

    # Get district names index
    distr_index = cu.Config(main_config.get_value('DistrictsIndex'))
    
    # Parse data in image column by column of first table 
    parsed_columns_p1 = []
    for i in range(0, n_cols_p1):
        # Append district names columns
        if(i == 0):
            ma_distr_data = []
            n_rows = int(main_config.get_value('MADistrP1_RTRows'))
            for j in range(0, n_rows):
                ma_distr_data.append(distr_index.get_value(str(j)))
            parsed_columns_p1.append(ma_distr_data)
            continue
        # Select area and crop image
        print('MADistrP1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1))
        bounds_ma_distr = cv2.selectROI('MADistrP1', cv2_ma_distr, False, False)
        cv2.destroyWindow('MADistrP1')
        col_ma_distr = cv2_ma_distr[int(bounds_ma_distr[1]):int(bounds_ma_distr[1]+bounds_ma_distr[3]),
                                    int(bounds_ma_distr[0]):int(bounds_ma_distr[0]+bounds_ma_distr[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'MADistrP1 - Col[' + col_names_p1[i] + '] ' + str(i + 1) + '/' + str(n_cols_p1)
            cv2.imshow(window_name, col_ma_distr)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ma_distr = Image.fromarray(col_ma_distr)
        # Perform OCR in PIL image with pytesseract
        ma_distr_data = pytesseract.image_to_string(img_ma_distr)
        ma_distr_data = ma_distr_data.split('\n')
        parsed_columns_p1.append(ma_distr_data)

    # Parse data in image column by column of second table 
    parsed_columns_p2 = []
    for i in range(0, n_cols_p2):
        if(i == 0):
            ma_distr_data = []
            n_rows = int(main_config.get_value('MADistrP2_RTRows'))
            for j in range(0, n_rows):
                ma_distr_data.append(distr_index.get_value(str(j)))
            parsed_columns_p2.append(ma_distr_data)
            continue
        # Select area and crop image
        print('MADistrP2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2))
        bounds_ma_distr = cv2.selectROI('MADistrP2', cv2_ma_distr, False, False)
        cv2.destroyWindow('MADistrP2')
        col_ma_distr = cv2_ma_distr[int(bounds_ma_distr[1]):int(bounds_ma_distr[1]+bounds_ma_distr[3]),
                                    int(bounds_ma_distr[0]):int(bounds_ma_distr[0]+bounds_ma_distr[2])]
        # Show cropped image if showimg = True
        if(showimg):
            window_name = 'MADistrP2 - Col[' + col_names_p2[i] + '] ' + str(i + 1) + '/' + str(n_cols_p2)
            cv2.imshow(window_name, col_ma_distr)
            cv2.waitKey(0)
        # Convert opencv2 image back to PIL image
        img_ma_distr = Image.fromarray(col_ma_distr)
        # Perform OCR in PIL image with pytesseract
        ma_distr_data = pytesseract.image_to_string(img_ma_distr)
        ma_distr_data = ma_distr_data.split('\n')
        parsed_columns_p2.append(ma_distr_data)

    # Find column with most elements
    max_col_len_p1 = 0
    for i in range(0, len(parsed_columns_p1)):
        if(max_col_len_p1 < len(parsed_columns_p1[i])):
            max_col_len_p1 = len(parsed_columns_p1[i])
    max_col_len_p2 = 0
    for i in range(0, len(parsed_columns_p2)):
        if(max_col_len_p2 < len(parsed_columns_p2[i])):
            max_col_len_p2 = len(parsed_columns_p2[i])

    # Create new Table and add each row of data from part 1
    raw_table_abs_path = table_names_config.get_value('MADistrP1')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p1,
        delimiter=';'
    )
    # Fill table with data from part 1
    for i in range(0, max_col_len_p1):
        new_row = []
        for j in range(0, len(col_names_p1)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p1[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p1[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)

    # Create new Table and add each row of data from part 2
    raw_table_abs_path = table_names_config.get_value('MADistrP2')
    output_table = du.Table(
        'n',
        filename=raw_table_abs_path,
        header_index=col_names_p2,
        delimiter=';'
    )
    # Fill table with data from part 2
    for i in range(0, max_col_len_p2):
        new_row = []
        for j in range(0, len(col_names_p2)):
            # If columns is shorter than longest one in set -> put row entry placeholder
            if(i >= len(parsed_columns_p2[j])):
                new_row.append(' ')
            # Otherwise store data in row
            else:
                new_row.append(parsed_columns_p2[j][i])
        output_table.append_end_row(new_row)
    output_table.save_as_csv(main_config.get_value('RawTablesDir') + '/' + raw_table_abs_path)
    print('MADistr done.')


#####################################################################################################

def main():
    main_config = cu.Config('config/ParsePDFConfig.cl')
    areas_config = cu.Config('config/AreasPDF.cl')
    pdf_path = areas_config.get_value('ReportPath') + areas_config.get_value('ReportFilename')

    menu_selection = {
        'PADepto'     : True,
        'CADepto'     : True,
        'CPEdades'    : True,
        'MADepto'     : True,
        'CADistr20'   : True,
        'CADistr21'   : True,
        'MADistr'     : True,
    }

    menu_selection = select_read_tables_menu(menu_selection)

    #if(menu_selection['PADepto']):
    #    process_pa_depto(main_config, pdf_path, showimg=False)
    #if(menu_selection['CADepto']):
    #    process_ca_depto(main_config, pdf_path, showimg=False)
    #if(menu_selection['CPEdades']):
    #    process_cp_edades(main_config, pdf_path, showimg=False)
    if(menu_selection['MADepto']):
        process_ma_depto(main_config, pdf_path, showimg=False)
    #if(menu_selection['CADistr20']):
    #    process_ca_distr_20(main_config, pdf_path, showimg=False)
    #if(menu_selection['CADistr21']):
    #    process_ca_distr_21(main_config, pdf_path, showimg=False)
    #if(menu_selection['MADistr']):
    #    process_ma_distr(main_config, pdf_path, showimg=False)
    
#####################################################################################################

main()
    