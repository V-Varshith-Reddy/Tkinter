# Name   : Vonteri Varshith Reddy
# RollNo : 21CS10081
# Assignment - 4

from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    global my_image
    if cc:
        cc.destroy()
    if my_image:
        my_image.destroy()
    clicked.set(filedialog.askopenfilename(parent=window,
                                           initialdir="./data/imgs", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("All files", "*.*"))))
    file_name.set(
        f"Image - {clicked.get().split('.')[0].split('/')[-1]}" if clicked.get() else "")
    if file_name.get() == "":
        return
    image = ImageTk.PhotoImage(Image.open(clicked.get()))
    my_image = Label(window, image=image)
    my_image.config(image=image)
    my_image.image = image
    my_image.grid(row=1, column=0, columnspan=4)
    # To have a better clarity, please check out the sample video.


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    global cc
    if cc:
        cc.destroy()

    if clicked.get() == "":
        print("Select a file first!")
        return
    elif click.get() == "classifier":
        text = classifier(clicked.get())
        op = "The Classes are: \n"
        for t in text:
            op += t[1] + ": "
            op += str(t[0]*100) + "%"
            op += '\n'
    elif click.get() == "captioner":
        text = captioner(clicked.get())
        op = "The Captions are: \n"
        for t in text:
            op += t
            op += "\n"
    cc = Label(window, text=op)
    cc.grid(row=1, column=5)

    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.


if __name__ == '__main__':
    # Complete the main function preferably in this order:
    # Instantiate the root window.
    # Provide a title to the root window.
    window = Tk()
    window.title("Image Captioning GUI")
    window.minsize(width=800, height=100)

    # Instantiate the captioner, classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()

    # Declare the file browsing button.
    clicked = StringVar()
    clicked.set("")
    file_browsing_button = Button(
        window, text="open", command=partial(fileClick, clicked))
    file_browsing_button.grid(row=0, column=1)

    # Declare the drop-down button.
    click = StringVar()
    click.set("captioner")
    drop_down_button = OptionMenu(window, click, "captioner", "classifier")
    drop_down_button.grid(row=0, column=2)
    # drop_down_button.pack()
    # Declare the process button.
    cc = None
    my_image = None
    process_btn = Button(window, text="process", command=partial(
        process, clicked, captioner, classifier))
    process_btn.grid(row=0, column=3)

    file_name = StringVar()
    file_name.set("")
    select = Label(window, textvariable=file_name)
    select.grid(row=0, column=0)
    window.mainloop()
    # Declare the output label.
