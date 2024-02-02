from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top1=Image.open(r'college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg')
        img_top1=img_top1.resize((1330,720),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=0,y=55,width=1330,height=720)
           
          #changes required Email 
        dev_label=Label(f_lbl,text="Email:sidkhanduri13@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=450,y=220)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop() 