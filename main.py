import csv
import pdf_extract
import html_parse

parseKeys = []
data = []
filtered_data = []

def parsePDF():
    headers = ['#', 'Parcel Number', 'Key Number', 'Owner', 'Orig. Auction Value', 'Mun Code', 'Cert. Number', 'Interest Percent', 'In Prior Tax Sale']
    # filename = 'parse\\output\\Available-County-Tax-Liens-as-of-07012022.csv'
    filename = 'parse\\output\\County-Tax-Liens-as-of-08052022.csv'
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
    for item in data_in:
        if 'Improvements' in item and item['Improvements'] != "$N/A":
            # print(item['Improvements'])
            value = int(item['Improvements'].replace('$', '').replace(',', ''))
            if isinstance(value, int) and value > 10000:
                str =  'Key: ' + data_in[0]['Key Number'] + ' Year: ' + item['Year'] + ' Improvements: ' + item['Improvements']
                # print(str)
                filtered_data.append(str)
    filtered_data.append('==================================================================')

def writeData():
    for item in filtered_data:
        file_out = 'parse\\output\\LOG.txt'
        with open(file_out, 'a') as f:
            f.write(item + '\n')

pdf_extract.runExtract()
parseKeys = parsePDF()
print()

for key in parseKeys:
    prop_data = html_parse.runParse(key)

    checkImprovements(prop_data)

print(filtered_data)

writeData()