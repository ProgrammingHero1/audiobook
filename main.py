import PyPDF2
from tkinter import *
from tkinter import filedialog
import pyttsx3
import time
win = Tk()
win.geometry("1500x1500")
txt1 = IntVar()
text = Text(win, width=80, height=30)
text.pack(pady=20)
try:
    def open_pdf():
        file = filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files", "*.pdf"), ("All Files", "*.*")))
        if file:
            pdf_file = PyPDF2.PdfFileReader(file)
            page = pdf_file.getPage(txt1.get())
            content = page.extractText()
            txt = pyttsx3.init()
            txt.say(content)
            txt.runAndWait()
            text.insert(1.0, content)
            time.sleep(2)
except FloatingPointError:
    pass
bt1_open = Button(win, text="Select the file ", command=open_pdf)
lbl = Label(win, text="input the page to speak")
lbl2 = Entry(win, textvariable=txt1)
lbl.pack()
lbl2.pack()
bt1_open.pack()
win.mainloop()
