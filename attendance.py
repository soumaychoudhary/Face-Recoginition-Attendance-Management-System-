from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #---------variables---------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # first image
        img = Image.open(r"1628243597666college-images/college_images/report.jpg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=0, y=0, width=800, height=200)

        # second image
        imgl = Image.open(r"1628243597666college-images/college_images/sample.jpg")
        imgl = imgl.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimgl = ImageTk.PhotoImage(imgl)

        f_lbl2 = Label(self.root, image=self.photoimgl)
        f_lbl2.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(r"1628243597666college-images/college_images/IMG_1183_augmented_reality_faces1.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        #left label frame

        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"1628243597666college-images/college_images/smart-attendance.jpg")
        img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl2= Label(Left_frame,image=self.photoimg_left)
        f_lbl2.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #labeland entry

        #attendance id
        AttendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        AttendanceId_entry.grid(row=0,column=1,pady=8)

        #name
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #date

        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department

        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #time

        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date

        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        #attendance

        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #button frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=18,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #----------scroll bar------------
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #----------fetch data --------------------------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","* *")),parent=self.root)
        with open(fln) as myfile:
            csvread =csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
#export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALl File","* *")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write =csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


 
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import csv
# from tkinter import filedialog

# mydata = []

# class Attendance:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         # --------variables---------
#         self.var_atten_id = StringVar()
#         self.var_atten_roll = StringVar()
#         self.var_atten_name = StringVar()
#         self.var_atten_dep = StringVar()
#         self.var_atten_time = StringVar()
#         self.var_atten_date = StringVar()
#         self.var_atten_attendance = StringVar()

#         # first image
#         img = Image.open(r"1628243597666college-images/college_images/report.jpg")
#         img = img.resize((800, 200), Image.Resampling.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)

#         f_lbl1 = Label(self.root, image=self.photoimg)
#         f_lbl1.place(x=0, y=0, width=800, height=200)

#         # second image
#         imgl = Image.open(r"1628243597666college-images/college_images/sample.jpg")
#         imgl = imgl.resize((800, 200), Image.Resampling.LANCZOS)
#         self.photoimgl = ImageTk.PhotoImage(imgl)

#         f_lbl2 = Label(self.root, image=self.photoimgl)
#         f_lbl2.place(x=800, y=0, width=800, height=200)

#         img3 = Image.open(r"1628243597666college-images/college_images/IMG_1183_augmented_reality_faces1.jpg")
#         img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img = Label(self.root, image=self.photoimg3)
#         bg_img.place(x=0, y=200, width=1530, height=710)

#         title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",35))
#         title_lbl.place(x=0,y=0,width=1530,height=710)

#         main_frame = Frame(bg_img, bd=2, bg="white")
#         main_frame.place(x=20, y=55, width=1480, height=600)

#         # left label frame
#         Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
#         Left_frame.place(x=10, y=10, width=730, height=580)

#         img_left = Image.open(r"1628243597666college-images/college_images/smart-attendance.jpg")
#         img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
#         self.photoimg_left = ImageTk.PhotoImage(img_left)

#         f_lbl_left = Label(Left_frame, image=self.photoimg_left)
#         f_lbl_left.place(x=5, y=0, width=720, height=130)

#         left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
#         left_inside_frame.place(x=0, y=135, width=720, height=370)

#         # Labels and entries
#         # Attendance ID
#         AttendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
#         AttendanceId_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

#         AttendanceId_entry = Label(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
#         AttendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

#         # Roll
#         rollLabel = Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 11 bold")
#         rollLabel.grid(row=0, column=2, padx=4, pady=8)

#         atten_roll = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font="comicsansns 11 bold")
#         atten_roll.grid(row=0, column=3, pady=8)

#         # Name
#         nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
#         nameLabel.grid(row=1, column=0)

#         atten_name = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font="comicsansns 11 bold")
#         atten_name.grid(row=1, column=1, pady=8)

#         # Department
#         depLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
#         depLabel.grid(row=1, column=2)

#         atten_dep = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_dep, font="comicsansns 11 bold")
#         atten_dep.grid(row=1, column=3, pady=8)

#         # Time
#         timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
#         timeLabel.grid(row=2, column=0)

#         atten_time = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_time, font="comicsansns 11 bold")
#         atten_time.grid(row=2, column=1, pady=8)

#         # Date
#         dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
#         dateLabel.grid(row=2, column=2)

#         atten_date = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_date, font="comicsansns 11 bold")
#         atten_date.grid(row=2, column=3, pady=8)

#         # Attendance
#         attendanceLabel = Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold")
#         attendanceLabel.grid(row=3, column=0)

#         self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
#         self.atten_status["values"] = ("Status", "Present", "Absent")
#         self.atten_status.grid(row=3, column=1, pady=8)
#         self.atten_status.current(0)

#         # Button frame
#         btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
#         btn_frame.place(x=0, y=300, width=715, height=35)

#         save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
#         save_btn.grid(row=0, column=0)

#         update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
#         update_btn.grid(row=0, column=1)

#         delete_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
#         delete_btn.grid(row=0, column=2)

#         reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
#         reset_btn.grid(row=0, column=3)

#         # right label frame
#         Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12))
#         Right_frame.place(x=750, y=10, width=720, height=580)

#         table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
#         table_frame.place(x=5, y=5, width=700, height=455)

#         # ----------scroll bar------------
#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)

#         scroll_x.config(command=self.AttendanceReportTable.xview)
#         scroll_y.config(command=self.AttendanceReportTable.yview)

#         self.AttendanceReportTable.heading("id", text="Attendance ID")
#         self.AttendanceReportTable.heading("roll", text="Roll")
#         self.AttendanceReportTable.heading("name", text="Name")
#         self.AttendanceReportTable.heading("department", text="Department")
#         self.AttendanceReportTable.heading("time", text="Time")
#         self.AttendanceReportTable.heading("date", text="Date")
#         self.AttendanceReportTable.heading("attendance", text="Attendance")

#         self.AttendanceReportTable["show"] = "headings"

#         self.AttendanceReportTable.column("id", width=100)
#         self.AttendanceReportTable.column("roll", width=100)
#         self.AttendanceReportTable.column("name", width=100)
#         self.AttendanceReportTable.column("department", width=100)
#         self.AttendanceReportTable.column("time", width=100)
#         self.AttendanceReportTable.column("date", width=100)
#         self.AttendanceReportTable.column("attendance", width=100)

#         self.AttendanceReportTable.pack(fill=BOTH, expand=1)
#         self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

#     # ----------fetch data--------------------------------
#     def fetchData(self, rows):
#         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
#         for i in rows:
#             self.AttendanceReportTable.insert("", END, values=i)

#     # Import csv
#     def importCsv(self):
#         global mydata
#         mydata.clear()
#         fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        
#         if not fln:  # If no file is selected
#             return
        
#         try:
#             with open(fln, newline="") as myfile:
#                 csvread = csv.reader(myfile, delimiter=",")
#                 for i in csvread:
#                     if i:  # Avoid appending empty rows
#                         mydata.append(i)
#             if len(mydata) == 0:
#                 messagebox.showerror("No Data", "The CSV file is empty", parent=self.root)
#             else:
#                 self.fetchData(mydata)
#         except Exception as e:
#             messagebox.showerror("Error", f"Unable to read file: {str(e)}", parent=self.root)

#     # Export csv
#     def exportCsv(self):
#         try:
#             if len(mydata) < 1:
#                 messagebox.showerror("No Data", "No data found to export", parent=self.root)
#                 return False
#             fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            
#             if not fln:  # If no file path is provided
#                 return
            
#             with open(fln, mode="w", newline="") as myfile:
#                 exp_write = csv.writer(myfile, delimiter=",")
#                 for i in mydata:
#                     exp_write.writerow(i)
#                 messagebox.showinfo("Data Export", f"Your data has been exported to {os.path.basename(fln)} successfully")
#         except Exception as es:
#             messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

#     def get_cursor(self, event=""):
#         cursor_row = self.AttendanceReportTable.focus()
#         content = self.AttendanceReportTable.item(cursor_row)
#         rows = content["values"]
#         self.var_atten_id.set(rows[0])
#         self.var_atten_roll.set(rows[1])
#         self.var_atten_name.set(rows[2])
#         self.var_atten_dep.set(rows[3])
#         self.var_atten_time.set(rows[4])
#         self.var_atten_date.set(rows[5])
#         self.var_atten_attendance.set(rows[6])

#     def reset_data(self):
#         self.var_atten_id.set("")
#         self.var_atten_roll.set("")
#         self.var_atten_name.set("")
#         self.var_atten_dep.set("")
#         self.var_atten_time.set("")
#         self.var_atten_date.set("")
#         self.var_atten_attendance.set("")


# if __name__ == "__main__":
#     root = Tk()
#     obj = Attendance(root)
#     root.mainloop()