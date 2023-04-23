import requests
import mwparserfromhell
from pandas import *
import os

folder = 'WikiCSV'
outputFile = 'DataSet.text'
doWrite = True

print("Warning doWrite is set to:", doWrite)

#open file
f = open(outputFile, 'w') # 'w' for overwrite, 'a' for append

#loop though files in folder
for file in os.listdir(folder) :
    data = read_csv(f"{folder}/{file}")
    #get all data from colum in csv
    #Note: Top row of file must be "===,"
    data = data['==='].tolist()
    nRows = len(data)
    
    counter = 1 #just to count number
    
    for cell in data :
        #format json
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': cell,
                'prop': 'revisions',
                'rvprop': 'content',
            }
        ).json()
        
        #turn into readble text from json
        page = next(iter(response['query']['pages'].values()))
        try :
            wikicode = page['revisions'][0]['*']
            parsed_wikicode = mwparserfromhell.parse(wikicode)
            text = parsed_wikicode.strip_code()
        except KeyError :
            print(f"NO WIKI FOR '{cell}'")
            continue
        
        #removes lines that are emtipy
        text = '\n'.join([line for line in text.splitlines() if line.strip() != ''])
        
        #writes to file
        if doWrite == True :
            f.write(f"From \"{cell}\" ==> \"\"\"\n")
            f.write(text)
            f.write(f"\n\"\"\"")
            f.write("\n\n")
        
        #for ui
        print(f"Finshed {cell:<5} from {file:<5} | #{counter} of {nRows}")
        counter += 1
