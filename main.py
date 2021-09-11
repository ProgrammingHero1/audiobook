# To read PDF file using Python pip install pypdf2 To Read text (Text to speech) pip install pyaudio pip install pyttsx3

import pyttsx3
import PyPDF2

book = open("C:/Users/bhask\Desktop/tweet_summarization/DE1.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("total number of pages is:" ,pages)

speaker = pyttsx3.init() 


""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print ("current voice rate is: ",rate)                        #printing current voice rate
speaker.setProperty('rate',170)     # setting up new voice rate
speaker.runAndWait()


"""VOLUME"""
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ("volume level is at : ",volume)                          #printing current volume level
speaker.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
speaker.say("HII BHASKAR!, NICE to see you here............")
print("the reading of book is started!............")
speaker.say("the reading of book is started!!!!!!!!")


for num in range(1,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
