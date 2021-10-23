from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
        def __init__(self,root):
            self.root=root
                #geometry
            self.root.geometry("1230x790+0+0")
            self.root.title("Face recognitions attendance system")


            title_lbl=Label(self.root,text="Face Recognition",font=("time new roman",35,"bold"),bg="white",fg="blue") 
            title_lbl.place(x=0,y=0,height=50,width=1230)

            img_top=Image.open(r"C:\Users\Admin\Desktop\FACE RECOGNITION SYSTEM FOR ATTENDANCE\Images for the system\face.JPG")
            img_top=img_top.resize((1230,790),Image.ANTIALIAS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=50,width=1230,height=790)
# ATTENDANCE
            def mark_attendance(slef,i,j,k):
                with open("krushna.csv","r+",newline="\n")as f:
                    myDataList=f.readlines()
                    name_list=[]
                    for line in myDataList:
                        entry=line.split((","))
                        name_list.append(entry[0])
                    if((i not in name_list) and (j not in name_list) (k not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtsting=now.strftime("%H:%M:S")
                        f.writelines(f"\n{i},{j},{k},{dtsting},{d1},preset")
                        


            #BUTTON
            b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("time new roman",25,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=0,y=450,width=1230,height=50)

            # FACE RECOGNTIION

            def recognition_face(self):
                def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
                    gray_image=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2GRAY)
                    features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)

                    coord=[]
                    for (x,y,w,h) in features:
                        cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                        id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                        confidence=int((100*(1-predict/300)))

                        conn=mysql.connector.connect(host="localhost",username="root",password="jhakrushna@079",database="face_recognition")
                        my_curser=conn.cursor()
                        
                        my_curser.execute("select student_name from student where studnt_name= "+str(id))

                        i=my_curser.fetchone()
                        i="+".join(i)

                        my_curser.execute("select Enrollment from student where Enrollment= "+str(id))

                        j=my_curser.fetchone()
                        j="+".join(j)

                        my_curser.execute("select Student_id from student where Student_id= "+str(id))

                        k=my_curser.fetchone()
                        k="+".join(j)

                        if confidence>75:
                            cv2.putText(img,f"student_id:{j}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"student_name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"enrollment:{j}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            self.mark_attendance(i,j,k)
                        else:
                            cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)

                            cv2.putText(img,"Unknown Face:",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                          
                        coord=[x,y,w,y]
                    return coord
                def recognized(img,clf,faceCascade):
                    coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                    return img

                faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                clf=cv2.face.LBPHFaceRecognizer_create()
                clf.read("classifier.xml")

                video_cap=cv2.VideoCapture(0)
                
                while True:
                    ret,img=video_cap.read()
                    img=recognized(img,clf,faceCascade)
                    cv2.imshow("attendace captured",img)

                    if cv2.waitKey(1)==13:
                        break
                    video_cap.release()
                    cv2.destroyAllWindows()






if __name__=="__main__":
        root=Tk()
        obj=Face_Recognition(root)
        root.mainloop()