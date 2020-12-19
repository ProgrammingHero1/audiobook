import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

n = int(input("Enter the page number from where you want to read:"))
t = int(input("Enter the page number till you want to read:"))
if t <= pages:
    for num in range(n , t):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
else:
    speaker.say("Please enter the valid page number..")
    speaker.runAndWait()
