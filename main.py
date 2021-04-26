import PyPDF2
import pyttsx3

# taking user input to get the pdf to be read(Make sure the pdf is available on the current directory)
pdf_name = input("Enter the name of the pdf to be listened:")
pdf_name = pdf_name + '.pdf'

book = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

# set the voice rate
speaker.setProperty('rate', 150)

# set volume
volume = speaker.getProperty('volume')
speaker.setProperty('volume', 1.0)

# set the voice property  voices[0] is male and voices[1] is female
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

# It skips the first page since numbering starts from 0.
for num in range(1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
