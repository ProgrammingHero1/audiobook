"""Audio book in python
original author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
original code: https://github.com/ProgrammingHero1/audiobook
Code forked by Samuel Githinji
mail: samuelwgithinji@gmail.com
"""

import PyPDF3  # to extract text from pdf file
import pyttsx3  # to convert text into speech
import os  # to pick path of the pdf file
import sys  # to get rid of possible errors & to exit program
from tkinter import filedialog  # to enable user to choose file of choice
from PyPDF3 import PdfFileReader  # to read file

# to get rid of the possible warnings
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

print('-------------------------------------------------------')
print("Welcome to Sam's pdf2speech Program. Enjoy!")
print('-------------------------------------------------------')

# select PDF file
file_name = filedialog.askopenfilename()
reader = PdfFileReader(file_name, strict=False)
numPages = reader.numPages
reading_speed = 200  # words per minute
voice_id = 1  # 1 -female voice, 0 -male voice


fileName = os.path.basename(file_name)[0:-4]  # to truncate .ext
print('\nBook Name: ' + fileName)  # to see the name of the book
print(numPages.__str__() + ' Pages')  # to see number of pages
print("\nNote: If program is just reading out page numbers your PDf file has an issue!")
print('\n-------------------------------------------------------')
print("Coded by Samuel Githinji")
print('Email: samuelwgithinji@gmail.com')
print('-------------------------------------------------------')

speaker = pyttsx3.init()  # initialize pyttsx3 engine
fileObj = open(file_name, 'rb')  # open the file in read and binary mode
pdfReader = PyPDF3.PdfFileReader(fileObj)  # create a file object
pages_num = pdfReader.numPages  # get num of pages in our file

for num in range(pages_num):
    pageObj = pdfReader.getPage(num)  # select a page by number (We count from 0, mind it)
    text = pageObj.extractText()  # get the text from our file
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[voice_id].id)
    volume = speaker.getProperty('volume')
    speaker.setProperty('volume', 1.0)
    # speak the page number, then the text
    speaker.say(f"Page {num + 1}" + ", -" + text)  # convert the text into speech (,- used to create a delay)
    speaker.setProperty('rate', reading_speed)
    speaker.runAndWait()  # run until finish
    speaker.save_to_file(text, fileName + '.mp3')
    speaker.runAndWait()

fileObj.close()  # close the file we opened before finishing

sys.exit()