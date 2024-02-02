from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1330,height=45)

        img_top=Image.open(r'college_images\dev.jpg')
        img_top=img_top.resize((1280,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1280,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="lightblue")
        main_frame.place(x=800,y=0,width=480,height=600)


       

        # Developer info 07:34 copy paste->done
        JayeshLable=Label(main_frame,text="Sudhanshu Khanduri-02396203119",font=("times new roman",22,"bold"),fg="white",bg="lightblue")
        JayeshLable.place(x=0,y=5)

        JayeshLable=Label(main_frame,text="Jayesh Kumar Singh-04996203119",font=("times new roman",22,"bold"),fg="white",bg="lightblue")
        JayeshLable.place(x=0,y=50)

        avi_label=Label(main_frame,text="Avneesh Singh Tanwar-04196203119",font=("times new roman",22,"bold"),fg="white",bg="lightblue")
        avi_label.place(x=0,y=100)

        

        img2=Image.open(r'college_images\lap.jpg')
        img2=img2.resize((475,390),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=475,height=390)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()