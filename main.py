import pyttsx3
import PyPDF2
name = input("Please enter the file name, It must be in the same directory: ")
book = open(name,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
start = int(input("Please input the starting you want: "))
# print(pages)
speaker = pyttsx3.init()
newVoiceRate = 130
speaker.setProperty('rate',newVoiceRate)
for num in range(start, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
