# gui application making tkinter
from tkinter import *
from tkinter import ttk
import tkinter
# for images we use pillow {crop}
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import time




class Face_Recognition_System:
    # calling construction
    # self then root window
    def __init__(self,root):
        # initialize root
        self.root = root
        # x +0 y + 0
        self.root.geometry("1530x790+0+0")
        self.root.title(r"Face recognition system")


        # 1st image
        # image inserting or adding(path)
        img = Image.open(r"college_images\Stanford.jpg")
        # converting into hll image to lll Antialias
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #setting image

        f_lbl = Label(self.root , image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1 = Image.open(r"college_images\facialrecognition.png")
        # converting into hll image to lll Antialias
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) #setting image

        f_lbl = Label(self.root , image = self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        

        # third image
        img2 = Image.open(r"college_images\u.jpg")
        # converting into hll image to lll Antialias
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) #setting image

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        # bg image
        # third image
        img3 = Image.open(r"college_images\bg_img.jpg")
        # converting into hll image to lll Antialias
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #setting image

        # labelling init first
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1350,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION AUTOMATED ATTENDANCE SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1350,height=45)

          #=====================time=======================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font= ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        

        # student button
        img4 = Image.open(r"college_images\student.jpg")
        # converting into hll image to lll Antialias
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) #setting image

        #for redirecting command =self.student_details
        b1 = Button(bg_img, image = self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100 , y=100,width=220,height=220)

        #Studentc button
        b1_1 = Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=300,width=220,height=40)



        # Detect Face button
        img5 = Image.open(r"college_images\face_detector1.jpg")
        # converting into hll image to lll Antialias
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) #setting image

        b1 = Button(bg_img, image = self.photoimg5,cursor="hand2",command=self.face_data,)
        b1.place(x=400,y=100,width=220,height=220)

        
        b1_1 = Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=300,width=220,height=40)


        # Attendance  button
        img6 = Image.open(r"college_images\Attendance.jpg")
        # converting into hll image to lll Antialias
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) #setting image

        b1 = Button(bg_img, image = self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=300,width=220,height=40)
        
        #Help button
        img7 = Image.open(r"college_images\Help.jpg")
        # converting into hll image to lll Antialias
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) #setting image

        b1 = Button(bg_img, image = self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=100,width=220,height=220)

        b1_1 = Button(bg_img, text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=300,width=220,height=40)

        #Train  button
        img8 = Image.open(r"college_images\Train.jpg")
        # converting into hll image to lll Antialias
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8) #setting image

        b1 = Button(bg_img, image = self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=100,y=360,width=220,height=220)

        b1_1 = Button(bg_img, text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=560,width=220,height=40)

        #Photos button
        img9 = Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        # converting into hll image to lll Antialias
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) #setting image

        b1 = Button(bg_img, image = self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=360,width=220,height=220)

        b1_1 = Button(bg_img, text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=560,width=220,height=40)
        
        #developer face  button
        img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
        # converting into hll image to lll Antialias
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10) #setting image

        b1 = Button(bg_img, image = self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=360,width=220,height=220)

        b1_1 = Button(bg_img, text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=560,width=220,height=40)


        #Exit face  button
        img11 = Image.open(r"college_images\exit.jpg")
        # converting into hll image to lll Antialias
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) #setting image

        b1 = Button(bg_img, image = self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1000,y=360,width=220,height=220)

        b1_1 = Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=560,width=220,height=40)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recogination","Are You Sure you want to exit",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            # vedio 9 21:09 exit button chnges 
            return

        #****************************Functions Buttons************************
   #for redirecting page
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Student(self.new_window)

    #9- 02:27 main file 
    def open_img(self):
        os.startfile("data")
    #10-03:00 previous changes 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    #15 -46:43 changes in button previous

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)#Function Name which we have defined inside the face_recognintion page 
    #16 -05:25 changes in button previous

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # video 9 13:04 developer fce button changes
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

        # video 9 18:11 help fce button changes
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

     


   
















        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
