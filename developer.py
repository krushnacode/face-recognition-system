from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class developer:
        def __init__(self,root):
                self.root=root
                #geometry
                self.root.geometry("1230x790+0+0")
                self.root.title("Face recognitions attendance system")

                title_lbl=Label(self.root,text="Developer",font=("time new roman",35,"bold"),bg="white",fg="blue") 
                title_lbl.place(x=0,y=0,height=50,width=1230)

                img_top=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\train data.PNG")
                img_top=img_top.resize((1230,790),Image.ANTIALIAS)
                self.photoimg_top=ImageTk.PhotoImage(img_top)

                f_lbl=Label(self.root,image=self.photoimg_top)
                f_lbl.place(x=0,y=50,width=1230,height=790)

if __name__=="__main__":
        root=Tk()
        obj=developer(root)
        root.mainloop()