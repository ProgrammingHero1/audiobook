# this package is used to convert text to speech
import pyttsx3 
#this package is used to read pdf and convert it to text
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
# you can use any number instead of 7 it is just a page number in oop.pdf file
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
