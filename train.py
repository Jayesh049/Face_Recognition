from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
#include <opencv2/face/facerec.hpp>

#numpy 88% performance hike inside the array or converting into the array


class Train:
    def __init__(self,root):
        self.root=root
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"college_images\facialrecognition.png") ##11-07:27 to  copy pste previous and changes
        img_top=img_top.resize((1310,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1310,height=325)

        # button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",26,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1310,height=60)
    
        img_bottom=Image.open("college_images\opencv_face_reco_more_data.jpg") #12- 13:00 button copy pste previous
        img_bottom=img_bottom.resize((1310,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1310,height=325)

        
#lbps is easy face recognition algo can represent local feature in the images and get possible to get greater result 
#grey scole strong
#opencv library provides you this algorithm

    def train_classifier(self):
        data_dir=("data")
        # list comprehensing used
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #path se data directory nikaal liya

        faces=[]
        ids=[]

        #getting faces and id
        for image in path:
            img=Image.open(image).convert('L') # grey sacale convert
            #13- install numpy
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

          ##**************************Train the classifier And Save***************
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        # after training storing/saving into the file
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")    
        
        


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()