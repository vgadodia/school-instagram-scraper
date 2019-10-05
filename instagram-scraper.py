from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import os

# browser = webdriver.Chrome()
# browser.get("https://www.instagram.com/nnhsabsence/")

username = 'nnhsabsence'

# browser = webdriver.Chrome()
# browser.get('https://www.instagram.com/'+username+'/?hl=en')

# links=[]
# source = browser.page_source
# data=bs(source, 'html.parser')
# body = data.find('body')
# script = body.find('span')
# for link in script.findAll('a'):
#      if re.match("/p", link.get('href')):
#         links.append('https://www.instagram.com'+link.get('href'))

# links=[links[0]]
# print(links)

# result=pd.DataFrame()
# for i in range(len(links)):
#     try:
#         page = urlopen(links[i]).read()
#         data=bs(page, 'html.parser')
#         body = data.find('body')
#         script = body.find('script')
#         raw = script.text.strip().replace('window._sharedData =', '').replace(';', '')
#         json_data=json.loads(raw)
#         posts =json_data['entry_data']['PostPage'][0]['graphql']
#         posts= json.dumps(posts)
#         posts = json.loads(posts)
#         x = pd.DataFrame.from_dict(json_normalize(posts), orient='columns') 
#         x.columns =  x.columns.str.replace("shortcode_media.", "")
#         result=result.append(x)
       
#     except:
#         np.nan

# result = result.drop_duplicates(subset = 'shortcode')
# result.index = range(len(result.index))

# import requests
# result.index = range(len(result.index))
# directory="/Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/"
# for i in range(len(result)):
#     r = requests.get(result['display_url'][i])
#     with open(directory+result['shortcode'][i]+".jpg", 'wb') as f:
#                     f.write(r.content)


import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/usr/local/Cellar/tesseract/4.1.0/bin/tesseract"

img = cv2.imread(r'/Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/sample.jpg')
# img = cv2.imread(r'/Users/veergadodia/Downloads/credcard.png')
# print(pytesseract.image_to_string(img))

file = open("testfile.txt", "a")
# file.write("Now the file has more content!")
print(pytesseract.image_to_string(img), file = file)
file.close() 

database = ['BAUER', 'BENOIT', 'CRAWFORD', 'DUROCHER', 'ESPELIN', 'GARGARO', 'GREENFIELD', 'KADEHJIAN', 'LUTZ', 'MINGOS', 'MOLE', 'MOORE', 'OBRIEN', 'SAHADEVAN', 'SCHUBERT', 'SHURTLEFF', 'SIMMONDS']
newwords = []

f=open("testfile.txt", "r")
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

for word in newwords:
	if word in database:
		print(word + " is out today!")





# def detect_text(path):
#     """Detects text in the file."""
#     from google.cloud import vision
#     import io
#     client = vision.ImageAnnotatorClient()

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print('Texts:')

#     for text in texts:
#         print('\n"{}"'.format(text.description))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])

#         print('bounds: {}'.format(','.join(vertices)))


# detect_text('Users/veergadodia/Documents/2019-2020/NNHSProgrammingClub/Selenium/B3MeCulD30A.jpg')

