import pyttsx3
import PyPDF2
import time
book = open('oop.pdf', 'rb') # oop.pdf is the file used in this code, you can specify the pdf in your own code later on
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say('Reading OOP.pdf')
    time.sleep(2)
    speaker.say(text)
    speaker.runAndWait()
