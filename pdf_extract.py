from tabula import convert_into
# from tabula import read_pdf
import sys
import os.path

project_root = os.path.dirname(os.path.realpath(__file__))

def runExtract():
    f_name = 'County-Tax-Liens-as-of-08052022'
    
    print('pdf_extract.py: filenames in/out')
    sys.stdout.flush()

    # file_in = '.\\input\\' + f_name +'.pdf'    
    # file_out = '.\\output\\' + f_name + '.csv'

    file_in = project_root + '\\input\\' + f_name +'.pdf'
    file_out = project_root + '\\output\\' + f_name +'.csv'

    # df = read_pdf(filename, pages='all', multiple_tables=True)

    print('pdf_extract.py: convert files to csv')
    print(file_in)
    print(file_out)
    sys.stdout.flush()

    table_extract = convert_into(file_in, file_out, 'csv', pages='all')
    # table_extract = convert_into(file_in, file_out, 'json', pages='all')