__author__ = 'sbeltran'

import io
import json
import re

excludeSTR = ['rd', 'ave', 'drive', 'ma', 'boston', 'blvd', 'road', 'avenue', 'dr.', 'credit', 'debit', 'st', 'street']

def getText(fileName):
    fo = open(fileName, "r+")
    str = fo.read();
    fo.close()
    return str

def textToJSON(fileName):
    j = json.loads(getText(fileName))

    texts = []

    for region in j["regions"]:
        for box in region['lines']:
            lineGroup = []
            for words in box['words']:
                temp = words['text']
                if (temp.lower() == 'total' or temp.lower() == 'subtotal'):
                    print texts
                    return None
                if len(temp) > 2:
                    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
                    results =r.findall(temp)
                    if not results:
                        lineGroup.append(temp)
            if (lineGroup and len(lineGroup) > 1):
                strLine = ' '.join(lineGroup)
                if not any(x in strLine.lower() for x in excludeSTR):
                    if strLine not in texts:
                        texts.append(strLine)

    print texts

def wordOrNum(text):
    nums = [i for i in text if i.isdigit()]
    if len(nums) > len(text)-len(nums):
        return 0 # number
    else:
        return 1 # word
textToJSON("r1.txt")
textToJSON("r2.txt")    