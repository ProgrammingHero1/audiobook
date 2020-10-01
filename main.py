import pyttsx3
import PyPDF2
import Translator
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
all=''
pages = pdfReader.numPages
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    all=text
    speaker.say(text)
    speaker.runAndWait()
 trans=Translator()
 t= trans.translate(all,src='en',dest='hi')
    obj=pyttsx3(text=t.text,slow='False',lang='hi')
    obj.save("audio.mp3")
