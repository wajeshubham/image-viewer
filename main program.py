from tkinter import *
from PIL import Image, ImageTk

# create a window
root = Tk()
root.title("image viewer")


# function to exit the window using exit button
def exit():
    root.quit()


# function for forward button
def forward(img_number):
    global myLable_1
    global button_1
    global button_2
    # create label to display the image
    myLable_1.grid_forget()
    myLable_1 = Label(image=myImg[img_number - 1])

    # create forward and backward button
    button_1 = Button(root, text=">>", padx=20, pady=5, command=lambda: forward(img_number + 1))
    button_2 = Button(root, text="<<", padx=20, pady=5, command=lambda: back(img_number - 1))
    myLable_1.grid(row=0, column=0, columnspan=3)
    # logic to change button initials when last or first image is displayed
    if img_number == len(myImg):
        button_1 = Button(root, text="||", state=DISABLED)

    button_2.grid(row=1, column=0)
    button_1.grid(row=1, column=2)

    # create label to display the current image number
    myLable_2 = Label(root, text=f"Image {img_number} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
    myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(img_number):
    global myLable_1
    global button_1
    global button_2
    myLable_1.grid_forget()
    myLable_1 = Label(image=myImg[img_number - 1])
    button_1 = Button(root, text=">>", padx=20, pady=5, command=lambda: forward(img_number + 1))
    button_2 = Button(root, text="<<", padx=20, pady=5, command=lambda: back(img_number - 1))
    myLable_1.grid(row=0, column=0, columnspan=3)
    if img_number == 1:
        button_2 = Button(root, text="||", state=DISABLED)

    button_2.grid(row=1, column=0)
    button_1.grid(row=1, column=2)
    myLable_2 = Label(root, text=f"Image {img_number} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
    myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)


# add images on screen
myImg_1 = ImageTk.PhotoImage(Image.open("photo_1.jpeg"))
myImg_2 = ImageTk.PhotoImage(Image.open("photo_2.jpeg"))
myImg_3 = ImageTk.PhotoImage(Image.open("photo_3.jpeg"))
myImg_4 = ImageTk.PhotoImage(Image.open("photo_4.jpeg"))
myImg_5 = ImageTk.PhotoImage(Image.open("photo_5.jpeg"))
myImg_6 = ImageTk.PhotoImage(Image.open("photo_6.jpeg"))

# create a list of image
myImg = [myImg_1, myImg_2, myImg_3, myImg_4, myImg_5, myImg_6]

# display the current image numb er
myLable_2 = Label(root, text=f"Image {1} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)
# display current image
myLable_1 = Label(image=myImg_1)
myLable_1.grid(row=0, column=0, columnspan=3)
# create buttons
button_1 = Button(root, text=">>", padx=20, pady=5, command=lambda: forward(2))
button_2 = Button(root, text="<<", padx=20, pady=5, command=back)
button_back = Button(root, text="Back", padx=40, pady=5, command=exit)

button_2.grid(row=1, column=0)
button_1.grid(row=1, column=2)
button_back.grid(row=1, column=1)

root.mainloop()
