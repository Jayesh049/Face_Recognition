# gui application making tkinter
from tkinter import*
from tkinter import ttk
# for images we use pillow {crop}
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from email import message
import cv2
#it consist of 2500 algo which recognises object and face 



class Student:
    # calling construction
    # self then root window
    def __init__(self ,root):
        # initialize root
        self.root = root
        # x +0 y + 0
        self.root.geometry("1530x790+0+0")
        self.root.title("Student")


        #--------variables--------------with the help of text variables 
        # we will fill the entry field and combo box
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        

        
        # 1st image
        # image inserting or adding(path)
        img = Image.open(r"C:\Users\DELL\Desktop\FaceRecognitionSystem\college_images\face-recognition.png")
        # converting into hll image to  lll Antialias
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) #setting image

        f_lbl = Label(self.root , image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1 = Image.open(r"C:\Users\DELL\Desktop\FaceRecognitionSystem\college_images\smart-attendance.jpg")
        # converting into hll image to lll Antialias
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1) #setting image

        f_lbl = Label(self.root , image = self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        

        # third image
        img2 = Image.open(r"C:\Users\DELL\Desktop\FaceRecognitionSystem\college_images\clg.jpg")
        # converting into hll image to lll Antialias
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2) #setting image

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

       # bg image
        # third image
        img3 = Image.open(r"C:\Users\DELL\Desktop\FaceRecognitionSystem\college_images\bg_img.jpg")
        # converting into hll image to lll Antialias
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) #setting image

        # labelling init first
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Frame 
        main_frame=Frame(bg_img,bd=2,bg="white") #creation
        main_frame.place(x=10,y=55,width=1285 ,height=600) #placing


        #left frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=545)

         # left frame image
        img_left = Image.open(r"C:\Users\DELL\Desktop\FaceRecognitionSystem\college_images\AdobeStock_303989091.jpeg")
        # converting into hll image to lll Antialias
        img_left = img_left.resize((590,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) #setting image

        f_lbl = Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=590,height=130)


        # CURRENT COURSE
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=120,width=590,height=110)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W) #grid initialization
        #stylist combo box by ttk
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly" ,width=17)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W) #grid initialization
        #stylist combo box by ttk
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly" ,width=17)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W) #grid initialization
        #stylist combo box by ttk
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly" ,width=17)
        year_combo["values"]=("Select Year","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W) #grid initialization
        #stylist combo box by ttk
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class Student Information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=230,width=590,height=290)

        # student id
        studentId_label =Label(class_Student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W) #grid initialization

        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        # student name
        studentName_label =Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) #grid initialization

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label =Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) #grid div

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly" ,width=15)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll number
        roll_no_label =Label(class_Student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) #grid initialization

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        gender_label =Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) #grid initialization

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gen,font=("times new roman",12,"bold"),state="readonly" ,width=15)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # dob
        dob_label =Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) #grid initialization

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email
        email_label =Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) #grid initialization

        email_entry = ttk.Entry(class_Student_frame,width=15,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # phone number
        phone_label =Label(class_Student_frame,text="Phone No.:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) #grid initialization

        phone_entry = ttk.Entry(class_Student_frame,width=15,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Address
        address_label =Label(class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W) #grid initialization

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Teacher Name
        teacher_label =Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W) #grid initialization

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons with same id with combo box
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1) #radio btn2 

        # buttons frame
        btn_frame = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=195,width=585,height=35)

        # savinig button from function add_data
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)


        #button frame2
        btn_frame1 = Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=585,height=35)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=27,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=600,height=545)

         # Right frame image
        img_right = Image.open(r"college_images\student.jpg")
        # converting into hll image to lll Antialias
        img_right = img_right.resize((590,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right) #setting image

        f_lbl = Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=585,height=130)

        # ******************Search System***********
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=590,height=62)

        search_label =Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) #grid initialization

        # stylist combo box by ttk
        semester_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),state="readonly",width=10)
        semester_combo["values"]=("Select","Roll_No","Phone_No")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=12,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=10,font=("times new roman",11,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3)
        
        showAll_btn=Button(Search_frame,text="Show All",width=10,font=("times new roman",11,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

        # ********************table frame************
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=590,height=305)


        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gen","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_no")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)#jaise
        self.fetch_data()
        
    #*************************************function declaration*****************
    # adding data function entering text variable into entry field
    def add_data(self): #data from get
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                ( 
                                                                    self.var_dep.get(),
                                                                    self.var_course.get(),
                                                                    self.var_year.get(),
                                                                    self.var_semester.get(),
                                                                    self.var_std_id.get(),
                                                                    self.var_std_name.get(),
                                                                    self.var_div.get(),
                                                                    self.var_roll.get(),
                                                                    self.var_gen.get(),
                                                                    self.var_dob.get(),
                                                                    self.var_email.get(),
                                                                    self.var_phone.get(),
                                                                    self.var_address.get(),
                                                                    self.var_teacher.get(),
                                                                    self.var_radio1.get()
                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)                                                                                        
            except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #==================fetch data=================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student") #selecting student database
        data=my_cursor.fetchall() #fetching all data so that we can use it further

    # data length is not 0 then something must be inside it
        if len(data)!= 0:
             self.student_table.delete(*self.student_table.get_children()) #getchildren is our inbuilt function so our first step is to delete
             #the data we have fetched all we have applied for loop for inserting data into it
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
        conn.close()

    #================get cursor====================

    def get_cursor(self,event=""):
        #cursor focusing on studenttable
        cursor_focus=self.student_table.focus()
        #taking content of table
        content = self.student_table.item(cursor_focus)
        #content values
        data=content["values"]
        #setting all the variables
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    #*********************update function**********
    def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
            else:
                try:
                    Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                    if Update>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gen.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_std_id.get(), #changes to be done in inside student 
                                                                                                                                                                                                    ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    

    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)    
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gen.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

            
    ## Generate data set take photo samples
    def generate_dataset(self):
        #2- 03:06(copy paste from above) update function
        if self .var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Feild are required",parent=self.root)
        else :   
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student") #all data select
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Name=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gen.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),#changes to be done in inside student 
                                                                                                                                                                                self.var_std_id.get()==id+1  #id calculate hota jaaye
                                                                                                                                                                                ))
                conn.commit() #4-04:38 update function query paste
                self.fetch_data()
                self.reset_data()
                conn.close() 
            ##  (For Face detection using Haar Cascades)
            ##  It is machine learning aproach train a image postive or negaitive both type of image for face detection
            ## Load predefined data on face frontal from open CV......
            #5-08:20 changes required ...
                face_classifier =cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #file for object detection

                def face_cropped(img): # convert colour image into grey scale
                    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                ##scaling factor =1.3
                ##Minimum neighbour =5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0) ## open camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))##we cropeed the images and store in varaiable no need of rectangle
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg" ##(the image which are save 100 calculate it like 1.1,1.2,1.3) #6.18.23 Create new folder
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        ##camera ko fronted face ko show karna hai
                        cv2.imshow("Cropped face",face)
                        #after entering tab will close after calculation of 100 images then break
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data  sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            #7-25:50 changes in previous files..
            


    
               
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()




    # def update_data(self):
    #     if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
    #             messagebox.showerror("Error","All Fields are required",parent=self.root)
    #     else:
    #         try:
    #             Upadate=messagebox.askyesno("Upadate","Do you want to update this student details",parent=self.root) #we want to ask user if you want to update the data
    #             if Upadate>0:  #yes kiya toh update ho jaega 
    #                 conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
    #                 my_cursor=conn.cursor()
    #                 my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Division=%s,Roll=%s,Gender,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(                                                                                                                                                                                      
                                                                                                                                                                                
    #                                                                                                                                                                             self.var_dep.get(),
    #                                                                                                                                                                             self.var_course.get(),
    #                                                                                                                                                                             self.var_year.get(),
    #                                                                                                                                                                             self.var_semester.get(),
    #                                                                                                                                                                             self.var_std_name.get(),
    #                                                                                                                                                                             self.var_div.get(),
    #                                                                                                                                                                             self.var_roll.get(),
    #                                                                                                                                                                             self.var_gen.get(),
    #                                                                                                                                                                             self.var_dob.get(),
    #                                                                                                                                                                             self.var_email.get(),
    #                                                                                                                                                                             self.var_phone.get(),
    #                                                                                                                                                                             self.var_address.get(),
    #                                                                                                                                                                             self.var_teacher.get(),
    #                                                                                                                                                                             self.var_teacher.get(),
    #                                                                                                                                                                             self.var_radio1.get(),
    #                                                                                                                                                                             self.var_std_id.get() #changes to be done in inside student   
    #                                                                                                                                                                         ))
                    
    #             else:   #   no kiya toh wahi ruk jaega return ho jaega  
    #                 if not Upadate:
    #                     return
    #                 messagebox.showinfo("Success","Student details successfully update completed",parent=self.root) 
    #                 conn.commit()
    #                 self.fetch_data()
    #                 my_cursor.close()
    #                 # conn.close()                                                                                                                                                                                             ))
    #         except Exception as es:
    #                 messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)