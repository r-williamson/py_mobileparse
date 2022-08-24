from tabula import convert_into
# from tabula import read_pdf

#TODO: implement so that this program takes parameters?

def runExtract():
    f_name = 'County-Tax-Liens-as-of-08052022'
    
    # file_in = 'parse\\input\\Available-County-Tax-Liens-as-of-07012022.pdf'
    # file_out = 'parse\\output\\Available-County-Tax-Liens-as-of-07012022.csv'
    # # file_out = 'parse\\output\\Available-County-Tax-Liens-as-of-07012022.json'

    file_in = 'parse\\input\\' + f_name +'.pdf'
    file_out = 'parse\\output\\' + f_name + '.csv'
    
    # file_in = 'parse\\input\\County-Tax-Liens-as-of-08052022.pdf'
    # file_out = 'parse\\output\\County-Tax-Liens-as-of-08052022.csv'

    # df = read_pdf(filename, pages='all', multiple_tables=True)

    table_extract = convert_into(file_in, file_out, 'csv', pages='all')
    # table_extract = convert_into(file_in, file_out, 'json', pages='all')