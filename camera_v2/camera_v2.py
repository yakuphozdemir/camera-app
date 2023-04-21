import cv2 as cv
import tkinter as tk
import ttkbootstrap as tbs
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import filedialog
from ttkbootstrap.dialogs import Messagebox

root = tbs.Window()
root.title("Camera")
root.geometry("1280x800")
root.resizable(True, True)

# print(tbs.Style().theme_names())
style = tbs.Style("cosmo")

image = ImageTk.PhotoImage(Image.open("image2.png"))

root.cam = cv.VideoCapture(0)

width_1, height_1 = 640, 480
root.cam.set(cv.CAP_PROP_FRAME_WIDTH, width_1)
root.cam.set(cv.CAP_PROP_FRAME_HEIGHT, height_1)
    
destPath = tbs.StringVar(value="C:\\Users\\yakup\\Pictures\\cameraapp")
def destBrowse():
    directory = filedialog.askdirectory(initialdir="C:\\Users\\yakup\\Pictures\\cameraapp")
    destPath.set(directory)
    
def openImage():
    openDirectory = filedialog.askopenfilename(initialdir=destPath)
    image = Image.open(openDirectory)
    image.show()

i = 1
def changeTheme():
    global i
    i += 1
    if i % 2 == 0:
        style = tbs.Style("darkly")
        root.roundToggle.configure(text="Karanlık Tema")
    else:
        style = tbs.Style("cosmo")
        root.roundToggle.configure(text="Açık Tema")

def createWidgets():

    root.cameraLabel = tbs.Label(master=root, bootstyle="primary", borderwidth=10, relief="solid")
    root.cameraLabel.place(relx=.5, rely=.5, anchor="center")

    browseButton = tbs.Button(root, width=30, text="Kaydın kaydedileceği adres", bootstyle="success",  command=destBrowse)
    browseButton.place(rely=1, x=5, y=-5, anchor="sw")

    captureButton = tbs.Button(root, text="Fotoğraf Çek", command=capture)
    captureButton.place(rely=0.5, relx=1, x=-60, y=20, anchor="center")

    root.recordButton = tbs.Button(root, text="Video Çek", command=increaseCheck)
    root.recordButton.place(rely=0.5, relx=1, x=-50, y=-20,  anchor="center")
    
    root.pauseVideoButton = tbs.Button(root, text="Videoyu duraklat", command=pauseCommand)
    #root.pauseVideoButton.place(rely=0.5, relx=1, x=-70, y=-60, anchor="center")
    #root.pauseVideoButton.place_forget()
    
    photoButton = tbs.Button(root, text="Dosyayı Aç", command=openImage)
    photoButton.place(rely=1, relx=1, x=-5, y=-5, anchor="se")

    root.roundToggle = tbs.Checkbutton(root, bootstyle="success, round-toggle", text="Açık tema", command=changeTheme)
    root.roundToggle.place(relx=1, x=-10, y=5, anchor="ne")
    
    flag = tbs.Label(root, text="Bayrak", image=image)
    flag.place(anchor="nw")
    
    camera()

recordControl = 0
def increaseCheck():
    global recordControl
    recordControl = recordControl+1
    return recordControl

def destVideo():
    videoTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    if destPath.get() != "":
        videoPath = destPath.get()
    else:
        Messagebox.show_error(message="Error", title="No Directory Selected for Store Video")
        
    videoName = videoPath + "\\" + videoTime + ".mp4v"
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    out = cv.VideoWriter(videoName, fourcc, 25, (width_1,height_1))
    return out

p = 0
def pauseCommand():
    global p
    p+=1    

def camera():
    global out
    global recordControl
    global p
    ret,frame = root.cam.read()
    
    if ret == True:
        frame = cv.flip(frame,1)
        cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (430,460), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
        frame2 = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        videoImage = Image.fromarray(frame2)
        imageTk = ImageTk.PhotoImage(image=videoImage)
        
        root.cameraLabel.configure(image=imageTk)
        root.cameraLabel.image = imageTk
        
        if recordControl == 1:
            videoTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")        
            if destPath.get() != "":
                videoPath = destPath.get()
            else:
                Messagebox.show_error(message="Error", title="No Directory Selected for Store Video")
            out = destVideo()
            increaseCheck()
            
        elif recordControl == 2 and p % 2 == 0:
            out.write(frame)
            root.recordButton.configure(text="Video Durdur")
            root.pauseVideoButton.configure(text="Videoyu duraklat")
            root.pauseVideoButton.place(rely=0.5, relx=1, x=-70, y=-60, anchor="center")
        elif p % 2 == 1:
            out.release
            root.pauseVideoButton.configure(text="Videoyu devam ettir")
        elif recordControl == 3:
            out.release()
            recordControl = 0
            p = 0
            root.recordButton.configure(text="Video Başlat")
            root.pauseVideoButton.place_forget()
        
        root.cameraLabel.after(10,camera)
      
    else:
        root.cameraLabel.configure(image="")
    
def capture():
    imageTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    if destPath.get() != "":
        imagePath = destPath.get()
    else:
        Messagebox.show_error(message="Error",title="No Directory Selected to Store Image")
        
    imageName = imagePath + "\\" + imageTime + ".png"
    
    ret, frame = root.cam.read()
    frame = cv.flip(frame,1)
    cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:/%M:%S"), (430,460), cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
    success = cv.imwrite(imageName,frame)

createWidgets()
root.mainloop()

"""
def camera():

    ret, frame = root.cam.read()
    
    if ret == True:
        frame = cv.flip(frame,1)                  #day/month/year , hour/minute/second
        cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (430,460), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255))
        frame2 = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
        videoImage = Image.fromarray(frame2)
        imageTk = ImageTk.PhotoImage(image=videoImage)
        
        root.cameraLabel.configure(image=imageTk)
        root.cameraLabel.image = imageTk
        root.cameraLabel.after(10,camera)
    else:
        root.cameraLabel.configure(image="")
"""

"""
recordControl = 0	
def record():
    global recordControl
    videoTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")        
    if destPath.get() != "":
        videoPath = destPath.get()
    else:
        Messagebox.show_error(message="Error", title="No Directory Selected for Store Video")
        
    videoName = videoPath + "\\" + videoTime + ".avi"
        
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(videoName, fourcc, 25, (width_1,height_1))
    
    while True:   
        ret, frame = root.cam.read()
        frame = cv.flip(frame, 1)
        if recordControl == 0:
            out.write(frame)
        elif recordControl == 2:
            break
    out.release()
"""

"""
def record():
    
    videoTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    if destPath.get() != "":
        videoPath = destPath.get()
    else:
        Messagebox.show_error(message="Error", title="No Directory Selected for Store Video")
    
    videoName = videoPath + "\\" + videoTime + ".avi"
    
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    out = cv.VideoWriter(videoName, fourcc, 25, (width_1,height_1))
        
    ret, frame = root.cam.read()
    frame = cv.flip(frame, 1)
    cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (430,460), cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
    out.write(frame)
"""

