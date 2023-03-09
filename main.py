import pyttsx3
import PyPDF2
book = open("opp.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()
for i in range(7, pages):
    page = pdfReader.pages[i]
    text = str(page.extract_text()).strip()
    speaker.say(text)
    speaker.runAndWait()
