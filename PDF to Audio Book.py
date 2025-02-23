import pyttsx3
import PyPDF2

# Open the PDF file in binary mode
book = open('C:/Users/Mae Pearl Naigan/Downloads/Michael B. Garbosa-Dev-CV.pdf', 'rb')  # Replace 'mybook.pdf' with the path to your PDF file

# Initialize the TTS engine
play = pyttsx3.init()

# Read the PDF using PyPDF2
pdf_reader = PyPDF2.PdfReader(book)
num_pages = len(pdf_reader.pages)


print('Playing Audio Book')

# Iterate through all pages and extract text
for num in range(num_pages):
    page = pdf_reader.pages[num]
    data = page.extract_text()

    # Use the TTS engine to read the extracted text
    play.say(data)
    play.runAndWait()

# Close the PDF file
book.close()