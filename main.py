from tkinter import filedialog, messagebox

from tkinter import *
from imageencoder import ImageEncoder
from imagedecoder import ImageDecoder
from PIL import ImageTk, Image

window = Tk()
window.title("Stego helper")

current_path = StringVar()

lblChosenImagePath = Label(window, textvariable=current_path)


def open_dialog():
    window.filename = filedialog.askopenfilename()
    current_path.set(window.filename)

    img = Image.open(current_path.get())
    img = img.resize((250, 250), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(img)
    img_label = Label(window, image=my_img)
    img_label.image = my_img
    img_label.grid(row=0, column=3)


def encode():
    if not hasattr(window, 'filename'):
        messagebox.showwarning("No image select", "You must select an image first")
        return
    encoder = ImageEncoder(window.filename)
    encoder.encode(txtMessage.get(), "testlauf")


def decode():
    if not hasattr(window, 'filename'):
        messagebox.showwarning("No image select", "You must select an image first")
        return
    decoder = ImageDecoder(print, window.filename)
    decoder.start()


lblImagePath = Label(window, text="Image path: ")

lblMessage = Label(window, text="Message: ")
txtMessage = Entry(window)
btnSelectImage = Button(window, text="Choose image", command=open_dialog, padx=5, pady=5)
btn_encode = Button(window, text="Encode image", command=encode, padx=5, pady=5)
btn_decode = Button(window, text="Decode image",command=decode, padx=5, pady=5)

lblImagePath.grid(column=0, row=0, sticky=N+W)
lblChosenImagePath.grid(column=1, row=0,sticky=N+W)
lblMessage.grid(column=0, row=1, sticky=N+W)
txtMessage.grid(column=1, row=1, columnspan=2,sticky=N+W)
btnSelectImage.grid(column=0, row=3,sticky=N+W)
btn_encode .grid(column=1, row=3,sticky=N+W)
btn_decode.grid(column=2, row=3,sticky=N+W)

window.mainloop()




