from tkinter import *
from PIL import Image,ImageTk
Window=Tk()
Window.geometry("500x400")
Window.title("IMAGE ")
img=Image.open("mountain.jpeg")
upload=ImageTk.PhotoImage(img)
lbl=Label(Window,image=upload,height=400,width=400)
lbl.place(x=10,y=15)
Window.mainloop()
