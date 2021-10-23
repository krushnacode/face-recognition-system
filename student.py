from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
        def __init__(self,root):
                self.root=root
                #geometry
                self.root.geometry("1230x790+0+0")
                self.root.title("Face recognitions attendance system")

                # variable
                self.var_enrollment=StringVar()
                self.var_student_Name=StringVar()
                self.var_Faculty_Name=StringVar()
                self.var_Batch=StringVar()
                self.var_Department=StringVar()
                self.var_course=StringVar()
                self.var_semester=StringVar()
                self.var_year=StringVar()
 
                #title
                
                img1=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\background image.jpg")
                img1=img1.resize((1230,790),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)

                bg_image=Label(self.root,image=self.photoimg1)
                bg_image.place(x=0,y=0,width=1230,height=790)
        #title 
                title_lbl=Label(bg_image,text="Face Recognition Attendance System",font=("time new roman",35,"bold"),bg="white",fg="blue") 
                title_lbl.place(x=0,y=0,height=44,width=1230)

                main_frame =Frame(bg_image,bd=2)
                main_frame.place(x=5,y=49,width=1215,height=785)

        # Left level frame
                Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
                Left_frame.place(x=10,y=10,width=650,height=620)

                img_left=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
                img_left=img_left.resize((500,330),Image.ANTIALIAS)
                self.photoimg_left=ImageTk.PhotoImage(img_left)

                f_lbl=Label(Left_frame,image=self.photoimg_left)
                f_lbl.place(x=0,y=0,width=640,height=230)
#current course 
                current_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Course Information ",font=("time new roman",12,"bold"))
                current_frame.place(x=0,y=200,width=640,height=150)
        # department and combo boxes
                dep_label=Label(current_frame,text="Department",font=("time new roman",12,"bold"))
                dep_label.grid(row=0,column=0,padx=10,sticky=W)

                dep_combo=ttk.Combobox(current_frame,textvariable=self.var_Department,font=("time new roman",12,"bold"),width=17,state="readonly")
                dep_combo["values"]=("select Department","computer","IT","Civil","Mechnical","Electrical","EC")
                dep_combo.current(0)
                dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course and combo boxes
                course_label=Label(current_frame,text="Course",textvariable=self.var_course,font=("time new roman",12,"bold"))
                course_label.grid(row=0,column=2,padx=10,sticky=W)

                course_combo=ttk.Combobox(current_frame,font=("time new roman",12,"bold"),width=17,state="readonly")
                course_combo["values"]=("select Course","Python","JAVA","AI","DMBI","DBMS","AEM")
                course_combo.current(0)
                course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
                year_label=Label(current_frame,text="Year",textvariable=self.var_year,font=("time new roman",12,"bold"))
                year_label.grid(row=1,column=0,padx=10,sticky=W)

                year_combo=ttk.Combobox(current_frame,font=("time new roman",12,"bold"),width=17,state="readonly")
                year_combo["values"]=("select year","2020-2021","2020-2019","2019-2018","2018-2017","2017-2016")
                year_combo.current(0)
                year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        # semester
                semster_label=Label(current_frame,text="Semester",textvariable=self.var_semester,font=("time new roman",12,"bold"))
                semster_label.grid(row=1,column=2,padx=10,sticky=W)

                semster_combo=ttk.Combobox(current_frame,font=("time new roman",12,"bold"),width=17,state="readonly")
                semster_combo["values"]=("select semester","1","2","3","4","5","6","7","8")
                semster_combo.current(0)
                semster_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
                
                
                
                
                
        # class student information
                class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Student Information ",font=("time new roman",12,"bold"))
                class_student_frame.place(x=0,y=350,width=640,height=245)
                
                studrnrt_id_label=Label(class_student_frame,text="Student ID",font=("time new roman",12,"bold"))
                studrnrt_id_label.grid(row=0,column=0,padx=10,sticky=W)

                studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_enrollment,font=("time new roman",12,"bold"))
                studentID_entry.grid(row=0,column=1,padx=10,sticky=W)
                # name of the student 
                studrnrt_name_label=Label(class_student_frame,text="Student Name",font=("time new roman",12,"bold"))
                studrnrt_name_label.grid(row=0,column=2,padx=0,sticky=W)

                student_name_entry=ttk.Entry(class_student_frame,width=12,textvariable=self.var_student_Name,font=("time new roman",12,"bold"))
                student_name_entry.grid(row=0,column=3,padx=0,sticky=W)
                # Batch
                batch_id_label=Label(class_student_frame,text="Batch/class ID",font=("time new roman",12,"bold"))
                batch_id_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

                batchID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Batch,font=("time new roman",12,"bold"))
                batchID_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

                # Enrollment number
                Enroll_label=Label(class_student_frame,text="Enrollment Number",font=("time new roman",12,"bold"))
                Enroll_label.grid(row=1,column=2,padx=0,pady=5,sticky=W)

                Enroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_enrollment,width=12,font=("time new roman",12,"bold"))
                Enroll_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)
                
                #Teacher name
                Teacher_label=Label(class_student_frame,text="Faculty Name",font=("time new roman",12,"bold"))
                Teacher_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

                Teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Faculty_Name,font=("time new roman",12,"bold"))
                Teacher_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
                
        
        # RADIO BUTTON FOR THE TAKING PICTURE
                self.var_radio1=StringVar()
                radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
                radiobtn1.grid(row=3,column=0,padx=10)
                
                self.var_radio2=StringVar()
                radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo",value="No")
                radiobtn2.grid(row=3,column=1,padx=10)

                
        # button frame for the variable
                btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
                btn_frame.place(x=0,y=120,width=620,height=100)
                
                #adding the save data/ update /reset / delete
                save_btn=Button(btn_frame,text="Save",command=self.add_data,width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                save_btn.grid(row=0,column=0)
                
                Upadte_btn=Button(btn_frame,text="update",command=self.update_data,width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Upadte_btn.grid(row=0,column=1)
                
                Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Reset_btn.grid(row=1,column=0)
                
                Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                Delete_btn.grid(row=1,column=1)

                take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take a Photo",width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                take_photo_btn.grid(row=2,column=0)

                update_photo_btn=Button(btn_frame,text="Update the Photo",width=30,font=("time new roman",12,"bold",),fg="white",bg="blue")
                update_photo_btn.grid(row=2,column=1)




        #Right level frame
                Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
                Right_frame.place(x=630,y=10,width=650,height=620)
                
                #img_rigth=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\front.PNG")
                #img_rigth=img_rigth.resize((500,330),Image.ANTIALIAS)
                #self.photoimg_right=ImageTk.PhotoImage(img_rigth)

                #f_lbl=Label(Right_frame,image=self.photoimg_right)
                #f_lbl.place(x=0,y=0,width=640,height=230)

        #Serech System
                search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search Frame",font=("time new roman",12,"bold"))
                search_frame.place(x=0,y=2,width=640,height=100)
                
                
        # making the lables for the right section
                search_label=Label(search_frame,text="Search Bar:",font=("time new roman",12,"bold"),bg="blue",fg="white")
                search_label.grid(row=0,column=0,padx=0,pady=5,sticky=W)

                search_combo=ttk.Combobox(search_frame,font=("time new roman",12,"bold"),width=17,state="readonly")
                search_combo["values"]=("select ","Enrollment Number")
                search_combo.current(0)
                search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
                
                search_entry=ttk.Entry(search_frame,width=20,font=("time new roman",12,"bold"))
                search_entry.grid(row=0,column=2,padx=0,pady=5,sticky=W)

                search_btn=Button(search_frame,text="Search",width=10,font=("time new roman",12,"bold",),fg="white",bg="blue")
                search_btn.grid(row=1,column=0)

                show_all_btn=Button(search_frame,text="Show All",width=10,font=("time new roman",12,"bold",),fg="white",bg="blue")
                show_all_btn.grid(row=1,column=1)

        #Table frame-----------------------------
                Table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
                Table_frame.place(x=5,y=101,width=570,height=300)

                #scrollbar
                Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
                Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
                
                self.student_table=ttk.Treeview(Table_frame,columns=("enrollment","student Name","Faculty Name","Batch","Department","course","semester","year"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

                Scroll_x.pack(side=BOTTOM,fill=X)
                Scroll_y.pack(side=BOTTOM,fill=Y)
                Scroll_x.config(command=self.student_table.xview)
                Scroll_y.config(command=self.student_table.yview)

                self.student_table.heading("enrollment",text="Enrolment Number")
                self.student_table.heading("student Name",text="student Name")
                self.student_table.heading("Faculty Name",text="Faculty Name")
                self.student_table.heading("Batch",text="Batch")
                self.student_table.heading("Department",text="Departmentr")
                self.student_table.heading("course",text="course")
                self.student_table.heading("semester",text="semester")
                self.student_table.heading("year",text="year")

                self.student_table["show"]="headings"


        #for editing the size of the system data showing
        #   self.student_table.column("enrollment",Width=100)
        #   self.student_table.column("student Name",Width=100)
        #   self.student_table.column("Faculty Name",Width=100)
        #   self.student_table.column("Batch",Width=100)
        #   self.student_table.column("Department",Width=100)
        #   self.student_table.column("course",Width=100)
        #   sel f.student_table.column("semester",Width=100)
        #   self.student_table.column("year",Width=100)


                
                self.student_table.pack(fill=BOTH,expand=1)
                self.fetch_data()
        # FUNTION DECRATION
        def add_data(self):
                if self.var_Department.get()=="Select Department" or self.var_enrollment()=="" :
                        messagebox.showerror("Error","All Info is required",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                                my_curser=conn.cursor()
                                my_curser.execute("instert student values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                                                (
                                                                                                        self.var_Department.get(),
                                                                                                        self. var_student_Name.get(),
                                                                                                        self.var_Faculty_Name.get(),
                                                                                                        self.var_Batch.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_enrollment.get()

                                                                                                ))
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Success","student info has been added",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("error",f"Due to:{str(es)}",parent=self.root)
                        
                        
        # fetch Data
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                my_curser=conn.cursor()
                my_curser.execute("select * from student")
                data=my_curser.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                                self.student_table.insert("",END,values=i)

                        conn.commit()
                conn.close()

# dont try the get cursor system.


# update functions
        def update_data(self):
                if self.var_Department.get()=="Select Department" or self.var_enrollment()=="" :
                        messagebox.showerror("Error","All Info is required",parent=self.root)
                else:
                        try:
                                update=messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
                                if update>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                                        my_curser=conn.cursor()
                                        my_curser.execute("update student set deparment=%s,student_name=%s,faculty_name=%s,Batch=%s,Course=%s,semester=%s,Year=%s,Enrollment=%s"
                                        (
                                                                                                                self.var_Department.get(),
                                                                                                                self. var_student_Name.get(),
                                                                                                                self.var_Faculty_Name.get(),
                                                                                                                self.var_Batch.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_enrollment.get()  
                                        ))
                                else:
                                        if  not update:
                                                return
                                conn.comit()
                                self.fetch_data()
                                conn.close()
                        except Exception as es:
                                messagebox.showerror("Error",f"Not worrking{str(es)}",parent=self.root)

        def delete_data(self):
                if self.va_std_id_get()=='':
                        messagebox.showerror("Error",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("student delete page","Do you want to delete this student data",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                                        my_curser=conn.cursor()
                                        sql="delete from student id=%s"
                                        val=(self.va_std_id.get())
                                        my_curser.execute(sql,val)

                                else:
                                        if not delete:
                                                return
                                conn.comit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","success deleted student detail",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Error",f"Not worrking{str(es)}",parent=self.root)
# reset data error
        def reset_data(self):
                self.var_Department.set("select Department"),
                self. var_student_Name.set("Name"),
                self.var_Faculty_Name.set(""),
                self.var_Batch.set(""),
                self.var_course.set(""),
                self.var_semester.set(""),
                self.var_year.set(""),
                self.var_enrollment.set("")  
                

# generating the dataset and taking the photo sample
        def generate_dataset(self):
                if self.var_Department.get()=="Select Department" or self.var_enrollment()=="" :
                        messagebox.showerror("Error","All Info is required",parent=self.root)
                else:
                        try:
                                conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                                my_curser=conn.cursor()
                                my_curser.execute("Select * from student")
                                myresult=my_curser.fetchall()
                                id=0
                                for x in myresult:
                                        id+=1
                                my_curser.execute("update student set deparment=%s,student_name=%s,faculty_name=%s,Batch=%s,Course=%s,semester=%s,Year=%s,Enrollment=%s"
                                                                                                                (
                                                                                                                self.var_Department.get(),
                                                                                                                self. var_student_Name.get(),
                                                                                                                self.var_Faculty_Name.get(),
                                                                                                                self.var_Batch.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_enrollment.get()==id+1  
                                                                                                                ))
                        
                                conn.commit()
                                self.fetch_data()
                                self.reset_data()
                                conn.close()

                                # load predifinend data on face recognition
                                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                                def face_crope(img):
                                        gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
                                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                                        # scaling factor is 1.3
                                        # minimum neibhor is 5

                                        for (x,y,w,h) in faces:
                                                face_crope=img[y:y+h,x:x+W]
                                                return face_crope

                                cap=cv2.VideoCapture(0)
                                img_id=0
                                while True:
                                        ret,myframe=cap.read()
                                        if face_crope(myframe) is not None:
                                                img_id+=1
                                                face=cv2.resize(face_crope(myframe),(450,450))
                                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                                filel_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                                cv2.imwrite(filel_name_path)
                                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                                cv2.imshow("crooped face",face)

                                        if cv2.waitKey(1)==13 or int(img_id)==70:
                                                break

                                cap.release()
                                cv2.destroyAllWindows()

                                messagebox.showinfo("Result","Genrating data sets ")
                        except Exception as es:
                                messagebox.showerror("Error",f"Not worrking{str(es)}",parent=self.root)




if __name__=="__main__":
        root=Tk()
        obj=Student(root)
        root.mainloop()