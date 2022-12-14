from paddleocr import PaddleOCR
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import yake
root = Tk()
root.title('My Image to Text')
root.geometry("1200x900")

isPhoto = False
def file_open():
    global my_image, image_path
    root.filename = filedialog.askopenfilename(initialdir="D:/", title= "Select a file", filetypes =(("png files", "*.png"),("*.jpg", "jpg files"),("all files"))) 
    image_path = root.filename
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()
def instruction():
    instruction = ("Note: If there is no need, hit X button to exit program \n Step 1. Click Open File to choose Image \n Step 2. Click Start process for word extraction and search") 
    messagebox.showinfo("How to use", instruction)
def full_process():
    # Paddleocr supports Chinese, English, French, German, Korean and Japanese.
    # You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
    # to switch the language model in order.
    ocr = PaddleOCR(use_angle_cls=True, lang="en", page_num = 1)  # need to run only once to download and load model into memory
    result = ocr.ocr(image_path, cls=True)
    
    for idx in range(len(result)):
        res = result[idx]
        txts = [line[1][0] for line in res]

    my_output = ''
    my_output = ' '.join(map(str, txts))
    output_file = open('output.txt', 'w', encoding = "utf-8")
    output_file.writelines(my_output)
    output_file.close
    

    #Key Word extraction
    text = my_output
    if len(text) > 100:
        max_ngram_size = 5
        deduplication_threshold = 0.4
        deduplication_algo = 'seqm'
        windowSize = 1
        numOfKeywords = 20
        custom_kw_extractor = yake.KeywordExtractor(n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(text)

        f = open('webSearch.bat', 'w', encoding="utf-8")

        writeString = "https://www.google.com/search?q="
        for kw in keywords:
            writeString += str(kw[0]) + ' '
        writeString = "start " + writeString.replace(' ', '+')
        f.write(writeString)
        f.close()
    else:
        f = open('webSearch.bat', 'w', encoding="utf-8")
        writeString = "https://www.google.com/search?q=" + text
        writeString = "start " + writeString.replace(' ', '+')
        f.write(writeString)
        f.close()

    #Search on Web
    os.system('webSearch.bat')
my_button = Button(root, text = "Open File", command = file_open).pack()
my_button = Button(root, text = "Start Process", command = full_process).pack()
my_button = Button(root, text = "How to use", command = instruction).pack()
root.mainloop()