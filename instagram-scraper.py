from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import os
import glob

username = 'nnhsabsence'

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/'+username+'/?hl=en')

links=[]
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('span')
for link in script.findAll('a'):
     if re.match("/p", link.get('href')):
        links.append('https://www.instagram.com'+link.get('href'))
browser.quit()

links=[links[0]]
# print(links)

result=pd.DataFrame()
for i in range(len(links)):
    try:
        page = urlopen(links[i]).read()
        data=bs(page, 'html.parser')
        body = data.find('body')
        script = body.find('script')
        raw = script.text.strip().replace('window._sharedData =', '').replace(';', '')
        json_data=json.loads(raw)
        posts =json_data['entry_data']['PostPage'][0]['graphql']
        posts= json.dumps(posts)
        posts = json.loads(posts)
        x = pd.DataFrame.from_dict(json_normalize(posts), orient='columns') 
        x.columns =  x.columns.str.replace("shortcode_media.", "")
        result=result.append(x)
       
    except:
        np.nan

result = result.drop_duplicates(subset = 'shortcode')
result.index = range(len(result.index))

import requests
result.index = range(len(result.index))
directory="/Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/"
for i in range(len(result)):
    r = requests.get(result['display_url'][i])
    with open(directory+result['shortcode'][i]+".jpg", 'wb') as f:
                    f.write(r.content)



os.chdir("/Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/")
for index, oldfile in enumerate(glob.glob("*.jpg"), start=1):
    newfile = 'scrapedimg.jpg'
    os.rename (oldfile,newfile)

import cv2
import pytesseract

def imgToText(location):
	pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"
	img = cv2.imread(location)
	# img = cv2.imread(r'/Users/veergadodia/Downloads/credcard.png')
	# print(pytesseract.image_to_string(img))

	file = open("infofile.txt", "w")
	print(pytesseract.image_to_string(img), file = file)
	file.close()

def readData():
	f=open("infofile.txt", "r")
	contents=f.read()
	words = contents.split()
	for word in words:
		newword = word.replace('_', '')
		newword = newword.replace('|', '')	
		newword = newword.replace('_', '')
		newword = newword.replace('|', '')
		newword = newword.replace('/', '')
		newword = newword.replace(']', '')
		newword = newword.replace('[', '')
		newword = newword.replace('/', '')
		newword = newword.replace(',', '')
		newword = newword.upper()
		newwords.append(newword)

def teacherInput():
	while True:
		teacherName = input("Name of Teacher: ")
		if teacherName == '':
			break
		else:
			teacherArray.append(teacherName.upper())

def printOutput(num):
	if num == 0:
		for word in newwords:
			if word in database:
				print(word + " is out today!")
	elif num == 1:
		for word in newwords:
			if word in teacherArray:
				print(word + " is out today!")





imgToText('/Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/scrapedimg.jpg') 

database = ['BAUER', 'BENOIT', 'CRAWFORD', 'DUROCHER', 'ESPELIN', 
			'GARGARO', 'GREENFIELD', 'KADEHJIAN', 'LUTZ', 'MINGOS', 
			'MOLE', 'MOORE', 'OBRIEN', 'SAHADEVAN', 'SCHUBERT', 
			'SHURTLEFF', 'SIMMONDS', 'CAHILL', 'DUROCHER', 'IBOKETTE', 
			'KAVANAUGH', 'KERDOK', 'MANNELLY', 'MARTENIS', 'MCNAMARA',
			'MITCHELL', 'SCHUBERT']
newwords = []

readData()
# print(newwords)

teacherArray = []
teacherInput()
print(teacherArray)

print("")

		

if len(teacherArray) == 0:
	print("All Teachers Absent Today:")
	printOutput(0)
else:
	print("Your Teachers Absent Today:")
	printOutput(1)



