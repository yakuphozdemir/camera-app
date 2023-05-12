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

noble = ImageTk.PhotoImage(Image.open("icons\\flag.png"))
cam_cap = ImageTk.PhotoImage(Image.open("icons\\capture_1.png"))
cam_rec = ImageTk.PhotoImage(Image.open("icons\\cam-rec_2.png"))
image = ImageTk.PhotoImage(Image.open("icons\\image_3.png"))
folder = ImageTk.PhotoImage(Image.open("icons\\folder_4.png"))
#rec_button = ImageTk.PhotoImage(Image.open("icons\\record-button_5.png"))
pause_button = ImageTk.PhotoImage(Image.open("icons\\pause-button_6.png"))
play_button = ImageTk.PhotoImage(Image.open("icons\\play-button_7.png"))
stop_button = ImageTk.PhotoImage(Image.open("icons\\stop-button_8.png"))

root.cam = cv.VideoCapture(0)

width_1, height_1 = 640, 480
root.cam.set(cv.CAP_PROP_FRAME_WIDTH, width_1)
root.cam.set(cv.CAP_PROP_FRAME_HEIGHT, height_1)
    
destPath = tbs.StringVar()      # value="C:\\Users\\yakup\\Pictures\\cameraapp"
def destBrowse():
    directory = filedialog.askdirectory()   #initialdir="C:\\Users\\yakup\\Pictures\\cameraapp"
    destPath.set(directory)
    
def openImage():
    openDirectory = filedialog.askopenfilename()    #initialdir=destPath
    image = Image.open(openDirectory)
    image.show()

i = 1
def changeTheme():
    global i
    i += 1
    if i % 2 == 0:
        style = tbs.Style("darkly")
        root.roundToggle.configure(text="Dark")
    else:
        style = tbs.Style("cosmo")
        root.roundToggle.configure(text="Light")

def createWidgets():

    root.cameraLabel = tbs.Label(master=root, bootstyle="primary", borderwidth=10, relief="solid")
    root.cameraLabel.place(relx=.5, rely=.5, anchor="center")

    browseButton = tbs.Button(root, width=30, text="Kaydın kaydedileceği adres", bootstyle="link", image=folder, command=destBrowse)
    browseButton.place(rely=1, x=5, y=-5, anchor="sw")

    captureButton = tbs.Button(root, text="Fotoğraf Çek",bootstyle="link", image=cam_cap, command=capture)
    captureButton.place(rely=0.5, relx=1, x=-60, y=40, anchor="center")

    root.recordButton = tbs.Button(root, text="Video Çek", bootstyle="link", image=cam_rec, command=increaseControl)
    root.recordButton.place(rely=0.5, relx=1, x=-60, y=-40,  anchor="center")
    
    root.pauseVideoButton = tbs.Button(root, text="Videoyu duraklat",bootstyle="link", image=pause_button, command=pauseCommand)
    #root.pauseVideoButton.place(rely=0.5, relx=1, x=-60, y=-120, anchor="center")
    #root.pauseVideoButton.place_forget()
    
    photoButton = tbs.Button(root, text="Dosyayı Aç",bootstyle="link", image=image, command=openImage)
    photoButton.place(rely=1, relx=1, x=-5, y=-5, anchor="se")

    root.roundToggle = tbs.Checkbutton(root, bootstyle="success, round-toggle", text="Light", command=changeTheme)
    root.roundToggle.place(relx=1, x=-10, y=5, anchor="ne")
    
    flag = tbs.Label(root, text="Bayrak", image=noble)
    flag.place(anchor="nw")
    
    camera()

recordControl = 0
def increaseControl():
    global recordControl
    recordControl = recordControl+1

p = 0
def pauseCommand():
    global p
    p+=1    

def camera():
    global out, recordControl, p
    
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
                videoName = videoPath + "\\" + videoTime + ".mp4v"
                fourcc = cv.VideoWriter_fourcc(*"mp4v")
                out = cv.VideoWriter(videoName, fourcc, 25, (width_1,height_1))
                increaseControl()
                print(recordControl)
            else:
                Messagebox.show_error(message="Directory is not selected for video storing", title="Error")
                recordControl = 0
            #out = destVideo()
            
        elif recordControl == 2 and p % 2 == 0:
            out.write(frame)
            root.recordButton.configure(text="Video Durdur", image=stop_button)
            root.pauseVideoButton.configure(image=pause_button)
            root.pauseVideoButton.place(rely=0.5, relx=1, x=-60, y=-120, anchor="center")
        elif p % 2 == 1:
            root.pauseVideoButton.configure(text="Videoyu devam ettir", image=play_button)
        elif recordControl == 3:
            out.release()
            recordControl = 0
            p = 0
            root.recordButton.configure(text="Video Başlat", image=cam_rec)
            root.pauseVideoButton.place_forget()
        
        root.cameraLabel.after(10,camera)
      
    else:
        root.cameraLabel.configure(image="")
    
def capture():
    imageTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    if destPath.get() != "":
        imagePath = destPath.get()
    else:
        Messagebox.show_error(message="Directory is not selected to image storing, please select directory by use left bottom button", 
                              title="Error")
        
    imageName = imagePath + "\\" + imageTime + ".png"
    
    ret, frame = root.cam.read()
    frame = cv.flip(frame,1)
    cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (430,460), cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
    success = cv.imwrite(imageName,frame)

createWidgets()
root.mainloop()



"""
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
"""