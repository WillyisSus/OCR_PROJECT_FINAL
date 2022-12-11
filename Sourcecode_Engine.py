from paddleocr import PaddleOCR, draw_ocr
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.title('My Image to Text')
root.geometry("900x600")
def file_open():
    global my_image, image_path
    root.filename = filedialog.askopenfilename(initialdir="D:/", title= "Select a file", filetypes =(("png files", "*.png"),("*.jpg", "jpg files"),("all files"))) 
    image_path = root.filename
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text = "Open File", command = file_open).pack()
my_button = Button(root, text = "Start Process", command = root.destroy).pack()
root.mainloop()

# Paddleocr supports Chinese, English, French, German, Korean and Japanese.
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
# to switch the language model in order.
ocr = PaddleOCR(use_angle_cls=True, lang="en", page_num = 1)  # need to run only once to download and load model into memory
result = ocr.ocr(image_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)

# draw result
from PIL import Image
imgs = []
for idx in range(len(result)):
    res = result[idx]
    txts = [line[1][0] for line in res]

my_output = ''
my_output = ' '.join(map(str, txts))
output_file = open('output.txt', 'w', encoding = "utf-8")
output_file.writelines(my_output)
output_file.close