#performing the face recognition  operations 
#video_06
#some addition in main.py file (stored in screenshort )

# from tkinter import*
# from tkinter import ttk 
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector 
# import cv2
# import os
# import numpy as np


# class Face_Recognition :
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("face Recognition System")
       
#         title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
#         title_lbl.place(x=0,y=0,width=1530,height=45)
        
#         # 1st image
#         img_top=Image.open(r"1628243597666college-images/college_images/face_detector1.jpg")
#         img_top=img_top.resize((650,700),Image.Resampling.LANCZOS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)

#         f_lbl=Label(self.root,image=self.photoimg_top)
#         f_lbl.place(x=0,y=55,width=650,height=700)
        
#         # 2nd image
#         img_bottom=Image.open(r"1628243597666college-images/college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
#         img_bottom=img_bottom.resize((950,700),Image.Resampling.LANCZOS)
#         self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

#         f_lbl=Label(self.root,image=self.photoimg_bottom)
#         f_lbl.place(x=650,y=55,width=950,height=700)

#         #button
#         b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
#         b1_1.place(x=365,y=620,width=200,height=40)


#         #========= face recognition ==========



#     def face_recog(self):
#         def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
#             gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#             features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

#             coord=[]

#             for (x,y,w,h) in features :
#                 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#                 id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                 confidece=int((100*(1-predict/300)))

#                 conn=mysql.connector.connect(host="localhost",username="root",password="SC@131",database="face_recognizer")
#                 my_cursor=conn.cursor()

#                 my_cursor.execute("select name from student where Student_id="+str(id))
#                 n=my_cursor.fetchone()
#                 n="+".join(n)

#                 my_cursor.execute("select roll from student where Student_id="+str(id))
#                 r=my_cursor.fetchone()
#                 r="+".join(r)

#                 my_cursor.execute("select Department from student where Student_id="+str(id))
#                 d=my_cursor.fetchone()
#                 d="+".join(d)



#                 if confidence>77:
#                     cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 else:
#                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
#                     cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

#                 coord=[x,y,w,h]

#             return coord
        
#         def recognize(img,clf,faceCascade):
#             coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
#             return img
        
#         faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf=cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap=cv2.VideoCapture(0)

#         while True:
#             ret,img=video_cap.read()
#             img=recognize(img,clf,faceCascade)
#             cv2.imshow("Welcome To face Recognition",img)

#             if cv2.waitKey(1)==13:
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()


# if __name__=="__main__":
#     root=Tk()
#     obj=Face_Recognition(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import threading
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"1628243597666college-images/college_images/face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"1628243597666college-images/college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", font=("times new roman", 18, "bold"), bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)

    #=================attendence=====================================
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                

    # ========== Face Recognition ==========
    def face_recog(self):
        # Define the function to draw the bounding box and recognize faces
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection and retrieval
                conn = mysql.connector.connect(host="localhost", username="root", password="SC@131", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)

                my_cursor.execute("select roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)

                my_cursor.execute("select Department from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                if i:
                    i = "+".join(i)

                # Display text
                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            return img

        # Load face cascade and classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Start video capture in a separate thread
        def capture_video():
            video_cap = cv2.VideoCapture(0)
            while True:
                ret, img = video_cap.read()
                if not ret:
                    break

                img = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), clf)
                cv2.imshow("Welcome To Face Recognition", img)

                # Exit the loop when 'Enter' is pressed
                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        # Start the video capture in a new thread
        video_thread = threading.Thread(target=capture_video)
        video_thread.start()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

