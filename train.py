from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
        def __init__(self,root):
            self.root=root
                #geometry
            self.root.geometry("1230x790+0+0")
            self.root.title("Face recognitions attendance system")
                #title
            title_lbl=Label(self.root,text="Training Dataset",font=("time new roman",35,"bold"),bg="white",fg="blue") 
            title_lbl.place(x=0,y=0,height=50,width=1230)

            img_top=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\train data.PNG")
            img_top=img_top.resize((1230,790),Image.ANTIALIAS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=50,width=1230,height=790)
#FOR MAKING AND ADDING THE SECOND IMAGE
              #  img_bottom=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\train data.PNG")
              #  img_bottom=img_bottom.resize((1230,790),Image.ANTIALIAS)
              #  self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

              #  f_lbl=Label(self.root,image=self.photoimg_bottom)
              #  f_lbl.place(x=0,y=50,width=1230,height=790)
               #BUTTON
            b1_1=Button(self.root,text="Train Data",command=self.train_class,cursor="hand2",font=("time new roman",25,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=0,y=450,width=1230,height=50)

        def train_class(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
            faces=[]
            ids=[]

            for image in path:
                img=Image.open(image).convert('L')# gray scale Image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
# classifier ans save it
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.train(faces,ids)
            recognizer.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("result","training is compeleted")

            








if __name__=="__main__":
        root=Tk()
        obj=Train(root)
        root.mainloop()