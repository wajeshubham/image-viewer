from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("image viewer")

def exit():
    root.quit()

def forword(img_number):
    global myLable_1
    global button_1
    global button_2
    myLable_1.grid_forget()
    myLable_1=Label(image=myImg[img_number-1])
    button_1 = Button(root, text=">>", padx=20, pady=5, command=lambda: forword(img_number+1))
    button_2 = Button(root, text="<<", padx=20, pady=5, command=lambda :back(img_number-1))
    myLable_1.grid(row=0, column=0, columnspan=3)
    if img_number==len(myImg):
        button_1=Button(root,text="||",state=DISABLED)

    button_2.grid(row=1, column=0)
    button_1.grid(row=1, column=2)
    myLable_2 = Label(root, text=f"Image {img_number} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
    myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(img_number):
    global myLable_1
    global button_1
    global button_2
    myLable_1.grid_forget()
    myLable_1 = Label(image=myImg[img_number - 1])
    button_1 = Button(root, text=">>", padx=20, pady=5, command=lambda: forword(img_number + 1))
    button_2 = Button(root, text="<<", padx=20, pady=5, command=lambda: back(img_number - 1))
    myLable_1.grid(row=0, column=0, columnspan=3)
    if img_number ==1:
        button_2 = Button(root, text="||", state=DISABLED)

    button_2.grid(row=1, column=0)
    button_1.grid(row=1, column=2)
    myLable_2 = Label(root, text=f"Image {img_number} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
    myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)




myImg_1= ImageTk.PhotoImage(Image.open("photo_1.jpeg"))
myImg_2= ImageTk.PhotoImage(Image.open("photo_2.jpeg"))
myImg_3= ImageTk.PhotoImage(Image.open("photo_3.jpeg"))
myImg_4=ImageTk.PhotoImage(Image.open("photo_4.jpeg"))
myImg_5=ImageTk.PhotoImage(Image.open("photo_5.jpeg"))
myImg_6=ImageTk.PhotoImage(Image.open("photo_6.jpeg"))


myImg=[myImg_1,myImg_2,myImg_3,myImg_4,myImg_5,myImg_6]

myLable_2 = Label(root, text=f"Image {1} of {len(myImg)}", bd=2, relief=SUNKEN, anchor=E)
myLable_2.grid(row=2, column=0, columnspan=3, sticky=W + E)




myLable_1=Label(image=myImg_1)
myLable_1.grid(row=0,column=0,columnspan=3)

button_1=Button(root,text=">>",padx=20,pady=5,command=lambda:forword(2))
button_2=Button(root,text="<<",padx=20,pady=5,command=back)
button_back=Button(root,text="Back",padx=40,pady=5,command=exit)

button_2.grid(row=1,column=0)
button_1.grid(row=1,column=2)
button_back.grid(row=1,column=1)


root.mainloop()