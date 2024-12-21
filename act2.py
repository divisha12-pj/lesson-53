from tkinter import *
from  tkinter import messagebox
window=Tk()
window.geometry("400x500")
window.title("adding messagebox in tkinter")
def msg():
    messagebox.showerror("Alert","Virus found")
btn=Button(window,text="error found",command=msg,bg="red",fg="yellow")
btn.pack()
window.mainloop()