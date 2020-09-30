import pyttsx3
import PyPDF2

#opening the pdf file
name_of_pdf=input("Please enter the name of the file:")
book = open(name_of_pdf+'.pdf', 'rb')

#reading the text written
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

#intialising the text to speech
speaker = pyttsx3.init()

#speaking the text
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
