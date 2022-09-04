import requests
import json
from html.parser import HTMLParser

#TODO: implement so that it takes keys as parameters

data = []
filtered_data = []

def runParse(key_in):
    '''Parses a key for relevant info and saves the data as a json file'''
    key_num = key_in
    url = "https://esearch.mobilecopropertytax.com/Property/View/" + key_num

    r = requests.get(url)   #creates a Response object containing information from server

    class MyHTMLParser(HTMLParser):
        key = ''
        historyFound = False
        tableFound = False
        headerFound = False
        rowsFound = False
        stopDuplicates = False

        num = 0
        
        dict = {
            'Year' : '',
            'Improvements' : '',
            'Land Market' : '',
            'Appraised' : '',
            'Assessed' : ''
        }

        yearVals = []

        def handle_starttag(self, tag, attrs):
            if tag == 'table' and self.historyFound == True:
                self.tableFound = True
            if self.tableFound == True and (tag == 'th'):
                self.headerFound = True
            if self.tableFound == True and (tag == 'td'):
                self.rowsFound = True        

        def handle_endtag(self, tag):
            if tag == 'table':
                self.historyFound = False
                self.tableFound = False
                self.headerFound = False
                self.rowsFound = False

        def handle_data(self, data):   
            if "Property Roll Value History" in data and self.stopDuplicates == False:
                self.historyFound = True
                self.stopDuplicates = True
            if self.rowsFound == True:            
                data = data.replace('N/A', '$N/A')
                if '$' in data:
                    if self.num == 0:               #no switch statements in python 3.8 :(
                        self.dict['Improvements'] = data
                        self.num = self.num + 1
                    elif self.num == 1:
                        self.dict['Land Market'] = data
                        self.num = self.num + 1
                    elif self.num == 2:
                        self.dict['Appraised'] = data
                        self.num = self.num + 1
                    elif self.num == 3:
                        self.dict['Assessed'] = data
                        self.num = self.num + 1

                elif not data.isspace():            #handle data that is not $ or white space
                    if self.num == 4:
                        self.yearVals.append(self.dict)
                        self.clearDict()
                        self.num = 0
                    self.dict['Year'] = data

        def handle_charref(self, name):
            if name.startswith('x'):
                c = chr(int(name[1:], 16))
            else:
                c = chr(int(name))
            # print("Num ent  :", c)

        def getDict(self):
            return self.dict

        def getyearVals(self):
            return self.yearVals

        def setKey(self, key_in):
            self.key = key_in
            self.yearVals.append({'Key Number' : key_in})

        def clearDict(self):
            self.dict = {
                'Year' : '',
                'Improvements' : '',
                'Land Market' : '',
                'Appraised' : '',
                'Assessed' : ''
            }

    parser = MyHTMLParser()
    parser.setKey(key_in)
    parser.feed(r.text)

    return parser.getyearVals()

def loopKeys(keys_in):
    '''Passes a list of keys into the main parse function'''
    if isinstance(keys_in, list):
        keys = keys_in
        data = []
        for key in keys:
            data.append(runParse(key))
        return data
    else:
        print('Error: Not a list')

def saveToFile(data_in):
    '''Saves parsed HTML data as a JSON file'''
    extract = ''
    file_out = '.\\output\\HTML_output.json'
    extract = json.dumps(data_in)

    with open(file_out, 'w') as f:
        f.write(extract)

def checkImprovements(data_in):
    print('')

def getData():
    return data
    
# print(data)
# saveToFile(data)
# checkImprovements(data)