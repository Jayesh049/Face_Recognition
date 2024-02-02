from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
import csv
from tkinter import filedialog
from datetime import datetime
#include <opencv2/face/facerec.hpp>

mydata =[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #     #################varaiables##################
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        #31:00 changes required
        #32:00 changes required

        # 1st image
        # image inserting or adding(path)
        img = Image.open(r"college_images\smart-attendance.jpg")
        # converting into hll image to  lll Antialias
        img = img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #setting image

        f_lbl = Label(self.root , image = self.photoimg)
        f_lbl.place(x=0 ,y=0,width=800,height=200)


        # second image
        img1 = Image.open(r"college_images\clg.jpg")
        # converting into hll image to lll Antialias
        img1 = img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) #setting image

        f_lbl = Label(self.root , image = self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # third image
        img3 = Image.open(r"college_images\bg_img.jpg")
        # converting into hll image to lll Antialias
        img3 = img3.resize((1280,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #setting image

        # labelling init first
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1280,height=710)


        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        #Frame 
        main_frame=Frame(bg_img,bd=2,bg="white") #creation
        main_frame.place(x=10,y=55,width=1285 ,height=600) #placing

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="StudentAttendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=545)

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=545)

         # left frame image
        img_left = Image.open(r"college_images\clg.jpg")
        # converting into hll image to lll Antialias
        img_left = img_left.resize((590,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) #setting image

        f_lbl =Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=590,height=130)

        #Frame 
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white") #creation
        left_inside_frame.place(x=0,y=135,width=595,height=340) #placing

        #labels and entry
        # attendance id
        attendanceId_label =Label(left_inside_frame,text="Attendance ID:",font=("comicsansns",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=20,pady=8,sticky=W) #grid initialization

        attendanceId_entry = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_id,font=("comicsansns",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=20,pady=8,sticky=W)

        # Roll number
        roll_label =Label(left_inside_frame,text="Roll:",font=("comicsansns",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W) #grid initialization

        atten_roll = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_roll,font=("comicsans",13,"bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)

        # namelabel
        nameLabel =Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 12 bold")
        nameLabel.grid(row=1,column=0) #grid initialization

        atten_name = ttk.Entry(left_inside_frame,width=15,textvariable=self.var_atten_name,font="comicsansns 13 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel =Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 12 bold")
        depLabel.grid(row=1,column=2) #grid initialization

        atten_dep = ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,padx=1,pady=8)

        #time
        timeLabel =Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0) #grid initialization

        atten_time = ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        # Date
        dateLabel =Label(left_inside_frame,text="Date :",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2) #grid initialization

        atten_date = ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # attendance combo box
        attendancelabel =Label(left_inside_frame,text="Attendance Status:",font=("comicsansns",11,"bold"),bg="white")
        attendancelabel.grid(row=3,column=0) #grid initialization

        self.atten_status=ttk.Combobox(left_inside_frame,width=15,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=245,width=585,height=35)

        # savinig button from function add_data
        save_btn=Button(btn_frame,text="Import csv",command=self.import_Csv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="Export csv",command=self.export_Csv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)
        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=600,height=545)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white") #creation
        table_frame.place(x=5,y=5,width=585,height=410) #placing

    #**************************scroll bar table*****************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,colum=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings" #removing spaces
 
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# class Attendance:


########fetch data###########
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

####  import csv
    def import_Csv(self):
        global mydata
        mydata.clear()#for same data
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
                                    ##2-12:35 changes done

    ####   export csv
    def export_Csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No DAta Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            ########23:35 changes required by jayesh
    #getting data
    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance.set(rows[6])
         #####34:59 changes required->done

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        #####37:39 changes required 

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()