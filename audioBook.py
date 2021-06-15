import pyttsx3
import PyPDF2
from  tkinter.filedialog import *

# making engine to speak//
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)

# making speak function//
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# main code//
if __name__ == '__main__':
    print("Only text pdf files are supported")
    print("Enter the file location of the file")
    book=askopenfilename()
    pdfreader=PyPDF2.PdfFileReader(book)
    pages= pdfreader.numPages
    print("Enter the page number You want to hear")
    mainPageNumber=int(input("ENTER HERE: "))
    if mainPageNumber<=pages:
        pass
    else:
        print("The page number you have entered is greater than the pages in the book")
        exit()

    mainPage=pdfreader.getPage(mainPageNumber)


    for i in range(mainPageNumber, pages):
        text =mainPage.extractText()

        print(text)
        speak(text)



