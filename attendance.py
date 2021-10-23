from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class attendance:
        def __init__(self,root):
                self.root=root
                #geometry
                self.root.geometry("1230x790+0+0")
                self.root.title("Face recognitions attendance system")
# photo
                img1=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\student.jpg")
                img1=img1.resize((1230,790),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                bg_image=Label(self.root,image=self.photoimg1)
                bg_image.place(x=0,y=0,width=1230,height=790)

                title_lbl=Label(self.root,text="Attendance",font=("time new roman",35,"bold"),bg="white",fg="blue") 
                title_lbl.place(x=0,y=0,height=50,width=1230)

                main_frame =Frame(bg_image,bd=2)
                main_frame.place(x=5,y=49,width=1215,height=785)
#left
                Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
                Left_frame.place(x=10,y=10,width=650,height=620)

                img_left=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
                img_left=img_left.resize((500,330),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=0,y=0,width=640,height=230)

                left_insideframe =Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
                left_insideframe.place(x=5,y=240,width=635,height=500)

            #labels and entrys
                
                attendance_id_label=Label(left_insideframe,text="Student ID",font=("time new roman",12,"bold"))
                attendance_id_label.grid(row=0,column=0,padx=10,sticky=W)

                attendance_entry=ttk.Entry(left_insideframe,width=20,font=("time new roman",12,"bold"))
                attendance_entry.grid(row=0,column=1,padx=10,sticky=W)

                Enrollment_label=Label(left_insideframe,text="Enrollment ID",font=("time new roman",12,"bold"))
                Enrollment_label.grid(row=0,column=2,padx=10,sticky=W)

                Enrollment_entry=ttk.Entry(left_insideframe,width=20,font=("time new roman",12,"bold"))
                Enrollment_entry.grid(row=0,column=3,padx=10,sticky=W)


                batch_label=Label(left_insideframe,text="Batch ID",font=("time new roman",12,"bold"))
                batch_label.grid(row=1,column=0,padx=10,sticky=W)

                batch_entry=ttk.Entry(left_insideframe,width=20,font=("time new roman",12,"bold"))
                batch_entry.grid(row=1,column=1,padx=10,sticky=W)



                subject_label=Label(left_insideframe,text="subject ID",font=("time new roman",12,"bold"))
                subject_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

                subject_entry=ttk.Entry(left_insideframe,width=20,font=("time new roman",12,"bold"))
                subject_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

                 #adding the save data/ update /reset / delete
                btn_frame=Frame(left_insideframe,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=120,width=620,height=100)

                save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                save_btn.grid(row=0,column=0)
                
                Upadte_btn=Button(btn_frame,text="update",width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Upadte_btn.grid(row=0,column=1)
                
                Reset_btn=Button(btn_frame,text="Reset",width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Reset_btn.grid(row=1,column=0)
                
                Delete_btn=Button(btn_frame,text="Delete",width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Delete_btn.grid(row=1,column=1)


#right
                Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
                Right_frame.place(x=630,y=10,width=650,height=620)

                table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
                table_frame.place(x=0,y=5,width=580,height=500)

                # scroll bar table
                scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

                self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id,enrollment,batch,subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)

                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                
                scroll_x.config(command=self.AttendanceReportTable.xview)
                scroll_y.config(command=self.AttendanceReportTable.yview)
#error showing here plz make it workring
                #self.AttendanceReportTable.heading("id",text="Attendance ID")
                #self.AttendanceReportTable.heading("id",text="attendance ID")

                #self.AttendanceReportTable["show"]="headings"
                
                #self.AttendanceReportTable.pack(fill=BOTH,expand=1)

                # fatch data
        def fetchdata(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable)
            for i in rows:
                self.AttendanceReportTable.insert("",END,value=i)

        
        def importCsv (self):
            
            global mydata
            mydata.clear()
            fln=filedialog.askopenfile(initaldir=os.getcwd(),title="open csv",filetypes=(("csv File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)

                self.fetchdata(mydata)

# We are not going to use the export data because the system is giving the error
# the text variable is also showwing the error so dont try it

                



                
                
               


if __name__=="__main__":
        root=Tk()
        obj=attendance(root)
        root.mainloop()