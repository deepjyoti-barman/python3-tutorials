import pyttsx3
import PyPDF2

book = open('oop.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdf_reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()