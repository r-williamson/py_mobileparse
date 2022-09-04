import csv
import pdf_extract
import html_parse
import sys
import os.path

parseKeys = []
data = []
filtered_data = []
project_root = os.path.dirname(os.path.realpath(__file__))

def parsePDF():
    print('parsekeys: get filename')
    sys.stdout.flush()

    headers = ['#', 'Parcel Number', 'Key Number', 'Owner', 'Orig. Auction Value', 'Mun Code', 'Cert. Number', 'Interest Percent', 'In Prior Tax Sale']
    # filename = '.\\output\\Available-County-Tax-Liens-as-of-07012022.csv'
    filename = project_root + '\\output\\County-Tax-Liens-as-of-08052022.csv'
    result = []

    # TODO: add functionality to create file if it is not found
    with open(filename,  newline='') as csvfile:
        reader = csv.DictReader(csvfile, headers)
        for row in reader:
            if '$' in row['Orig. Auction Value']:
                value = float(row['Orig. Auction Value'].replace('$', '').replace(',', ''))
                if(value > 100 and value <= 2500):
                    result.append(row['Key Number'])
    return result

def checkImprovements(data_in):
    i = 0

    print('checkimprovements: start')
    sys.stdout.flush()

    for item in data_in:
        if 'Improvements' in item and item['Improvements'] != "$N/A":
            # print(item['Improvements'])
            value = int(item['Improvements'].replace('$', '').replace(',', ''))
            if isinstance(value, int) and value > 10000:
                print('improvement found')
                sys.stdout.flush()

                i = i + 1
                str =  'Key: ' + data_in[0]['Key Number'] + ' Year: ' + item['Year'] + ' Improvements: ' + item['Improvements']
                # print(str)
                filtered_data.append(str)
    if i > 0:
        filtered_data.append('==================================================================')
    
    print('checkimprovements: end')
    sys.stdout.flush()


def writeData():
    print('writeData: start')
    sys.stdout.flush()

    for item in filtered_data:
        file_out = project_root + '\\output\\LOG.txt'
        with open(file_out, 'a') as f:
            f.write(item + '\n')

def main(argv):
    print('pdf_runextract')
    sys.stdout.flush()

    pdf_extract.runExtract()

    print('parsekeys')
    sys.stdout.flush()

    parseKeys = parsePDF()

    print('checking improvements')
    sys.stdout.flush()

    for key in parseKeys:
        prop_data = html_parse.runParse(key)

        checkImprovements(prop_data)

    # print(filtered_data)

    writeData()

    print(200)
    sys.stdout.flush()

main(sys.argv)