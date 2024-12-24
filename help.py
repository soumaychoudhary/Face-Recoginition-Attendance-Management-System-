#import help desk in main .py
#make function of help desk in mainpy
#button changes in main for help desk
#make exit function in main .py
#button changes in main for exit
#import tkinter in main.py
#some changes in exit function  in main  shown in ss
#define time fun in main.py
#import modules from main_project.py  to main.py
#add login.py file to face recognition system file
#login me import kiya face recognition system
#login file me changes


from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recogination system")

        title_lbl=Label(self.root,text="Help Desk",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"1628243597666college-images/college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Email:soumay212@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place( x=550,y=220)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()