import requests
import mwparserfromhell
from pandas import *
import os

input_sheet = 'wikipedia_sheet.csv'
output_file = 'output.text'

# read the csv file
data = read_csv(input_sheet)
data = data['==='].tolist()
n_rows = len(data)

#open output file
f = open(output_file, 'w') # 'w' for overwrite, 'a' for append

# loop through all the cells in csv file
for cell, i in zip(data, range(len(data))) :
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
        output_text = parsed_wikicode.strip_code()
    except KeyError :
        print(f"# NO WIKIPEDIA PAGE FOR '{cell}'")
        continue
    
    # removes lines that are empty
    output_text = '\n'.join([line for line in output_text.splitlines() if line.strip() != ''])
    
    # writes to file
    f.write(f'From \"{cell}\" ==> \"\"\"\n')
    f.write(output_text)
    f.write(f'\n\"\"\"')
    f.write('\n\n')
    
    # for ui
    print(f'# Wrote : {cell:<5} | #{i+1} of {n_rows}')
