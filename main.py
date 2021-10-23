from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import attendance
import tkinter


class Face_recognition:
        def __init__(self,root):
                self.root=root
                #geometry
                self.root.geometry("1230x790+0+0")
                #title
                self.root.title("Face recognitions attendance system")
        # for adding the images on title(front page) page



        #for decorating the system
        # img=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
        # img=img.resize((500,330),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # for seting the window and useing the label
        #MAKE SURE TO EDIT THIS FOR THE PRESENTATION IT WILL GET SOME MORE SETTINGS
        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=1200,height=330)

                #for extra images 
        #for decorating the system
        #  img1=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
        #  img1=img1.resize((500,330),Image.ANTIALIAS)
        #  self.photoimg1=ImageTk.PhotoImage(img1)

        # for seting the window and useing the label
        #MAKE SURE TO EDIT THIS FOR THE PRESENTATION IT WILL GET SOME MORE SETTINGS
        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=0,y=0,width=1200,height=330)

        # background IMage

                img1=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\background image.jpg")
                img1=img1.resize((1230,790),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                bg_image=Label(self.root,image=self.photoimg1)
                bg_image.place(x=0,y=0,width=1230,height=790)

        # title 
                title_lbl=Label(bg_image,text="Face Recognition Attendance System",font=("time new roman",35,"bold"),bg="white",fg="blue")
                title_lbl.place(x=0,y=0,height=44,width=1230)

        # image button making for student button
                img3=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
                img3=img3.resize((200,200),Image.ANTIALIAS)
                self.photoimg3=ImageTk.PhotoImage(img3)

                b1=Button(bg_image,image=self.photoimg3,command=self.student_details)
                b1.place(x=150,y=100,width=210,height=210)

                b1_1=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=150,y=300,width=210,height=40)

                # image button For face detection
                img4=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\student.jpg")
                img4=img4.resize((200,200),Image.ANTIALIAS)
                self.photoimg4=ImageTk.PhotoImage(img4)

                b1=Button(bg_image,image=self.photoimg4,command=self.face_data)
                b1.place(x=450,y=100,width=210,height=210)

                b1_1=Button(bg_image,text="Face Detector",command=self.face_data,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=450,y=300,width=210,height=40)
        
                # image button for attendance

                img5=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\attendance1.JFIF")
                img5=img5.resize((200,200),Image.ANTIALIAS)
                self.photoimg5=ImageTk.PhotoImage(img5)

                b1=Button(bg_image,image=self.photoimg5,command=self.attendance_data)
                b1.place(x=750,y=100,width=210,height=210)

                b1_1=Button(bg_image,text="Attendance",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=750,y=300,width=210,height=40)

        # image button for help desk

               # img6=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\attendance1.JFIF")
               # img6=img6.resize((200,200),Image.ANTIALIAS)
               # self.photoimg6=ImageTk.PhotoImage(img6)

               # b1=Button(bg_image,image=self.photoimg6)
               # b1.place(x=900,y=100,width=210,height=210)

               # b1_1=Button(bg_image,text="Help Desk",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
               # b1_1.place(x=900,y=300,width=210,height=40)

                # image button for train Button

                img7=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\train data.PNG")
                img7=img7.resize((200,200),Image.ANTIALIAS)
                self.photoimg7=ImageTk.PhotoImage(img7)

                b1=Button(bg_image,image=self.photoimg7,command=self.train_data)
                b1.place(x=150,y=400,width=210,height=210)

                b1_1=Button(bg_image,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=150,y=600,width=210,height=40)

                # image button for photos

                img8=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\face_detection.PNG")
                img8=img8.resize((200,200),Image.ANTIALIAS)
                self.photoimg8=ImageTk.PhotoImage(img8)

                b1=Button(bg_image,image=self.photoimg8,command=self.open_img)
                b1.place(x=450,y=400,width=210,height=210)

                b1_1=Button(bg_image,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=450,y=600,width=210,height=40)

                # image button for photos

               # img9=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\developer.PNG")
               # img9=img9.resize((200,200),Image.ANTIALIAS)
               # self.photoimg9=ImageTk.PhotoImage(img9)
#
               # b1=Button(bg_image,image=self.photoimg9)
               # b1.place(x=650,y=400,width=210,height=210)
#
               # b1_1=Button(bg_image,text="Developer",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
               # b1_1.place(x=650,y=600,width=210,height=40)

                # image button for photos

                img10=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\exit.JFIF")
                img10=img10.resize((200,200),Image.ANTIALIAS)
                self.photoimg10=ImageTk.PhotoImage(img10)

                b1=Button(bg_image,image=self.photoimg10,command=self.Wexit)
                b1.place(x=750,y=400,width=210,height=210)      #b1.place(x=900,y=400,width=210,height=210)

                b1_1=Button(bg_image,text="Exit",cursor="hand2",command=self.Wexit,font=("time new roman",15,"bold"),bg="darkblue",fg="white")
                b1_1.place(x=750,y=600,width=210,height=40)     #b1_1.place(x=900,y=600,width=210,height=40)
        def open_img(self):
                os.startfile("data")


# FUNCTION BUTTON other window
        def student_details(self):
                self.new_window=Toplevel(self.root)
                self.app=Student(self.new_window)

        def train_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Train(self.new_window)

        def face_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition(self.new_window)

        def attendance_data(self):
                self.new_window=Toplevel(self.root)
                self.app=attendance(self.new_window)
        
        def Wexit(self):
                self.Wexit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit?",parent=self.root)
                if self.Wexit>0:
                        self.root.destroy()
                else:
                        return





if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
