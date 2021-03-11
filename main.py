import pyttsx3
import PyPDF2

book = open(r"C:\Users\Sachith R Gowda\Desktop\AUDIBLE\cprogramming_tutorial.pdf",'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages =input("Enter psge sto be read")
pages=int(pages)
engine=pyttsx3.init()
for num in range(pages):
    page=pdfReader.getPage(num)
    text =page.extractText()
    engine.say(text)
    engine.runAndWait()
