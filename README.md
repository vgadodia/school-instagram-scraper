# School Instagram Scraper
Project which scrapes photos of my school's teacher absence list from Instagram, uses Tesseract, an optical character recognition tool, to read and detect text embedded in the images, and finally matches detected text with user input to indicate which teachers are absent that day. 

## How to run the algorithm
Install Selenium, a website automation tool.
```python
pip install selenium
```
In addition to installing the selenium package as detailed above, you must download the chromedriver as well. You can find that download here: https://chromedriver.chromium.org/downloads

Install Pytesseract, an Optical Character Recognition tool to read and detect text in images.
```python
pip install pytesseract
```

Lastly, before you run the code, make sure you change all the file paths in the code to fit your directories/folders in your computer. Then run:
```python
python instagram-scraper.py
```

