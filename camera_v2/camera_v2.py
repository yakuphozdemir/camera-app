import cv2 as cv
import tkinter as tk
import ttkbootstrap as tbs
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import filedialog
from ttkbootstrap.dialogs import Messagebox
import os
from os import startfile
import pyaudio
import wave
from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip

root = tbs.Window()
root.title("Camera")
root.geometry("1280x800")
root.resizable(True, True)

# print(tbs.Style().theme_names())
style = tbs.Style("darkly")

noble = ImageTk.PhotoImage(Image.open("icons\\00_flag1.png"))
cam_cap = ImageTk.PhotoImage(Image.open("icons\\1_capture.png"))
cam_rec = ImageTk.PhotoImage(Image.open("icons\\2_cam-rec.png"))
image = ImageTk.PhotoImage(Image.open("icons\\3_image.png"))
folder = ImageTk.PhotoImage(Image.open("icons\\4_folder.png"))
#rec_button = ImageTk.PhotoImage(Image.open("icons\\5_record-button.png"))
pause_button = ImageTk.PhotoImage(Image.open("icons\\6_pause-button.png"))
play_button = ImageTk.PhotoImage(Image.open("icons\\7_play-button.png"))
stop_button = ImageTk.PhotoImage(Image.open("icons\\8_stop-button.png"))
brightness = ImageTk.PhotoImage(Image.open("icons\\9_brightness.png"))
contrast = ImageTk.PhotoImage(Image.open("icons\\10_contrast.png"))

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
    imageTypes = [".png", ".jpg", ".jpeg", ".svg"]
    videoTypes = [".avi", ".mp4", ".mp4a", ".xvid", ".mp4v"]
    if any(element in openDirectory for element in imageTypes):
        image = Image.open(openDirectory)
        image.show()
        #startfile(openDirectory)
    elif any(element in openDirectory for element in videoTypes):
        startfile(openDirectory)
    elif openDirectory == "":
        ""
    else:
        Messagebox.show_error(message="This is not a valid file. \nPlease select a video or image.", 
                              title="Error")
        
i = 2
def changeTheme():
    global i
    i+=1
    if i % 2 == 0:
        style = tbs.Style("darkly")
        root.roundToggle.configure(text="Dark")
    else:
        style = tbs.Style("cosmo")
        root.roundToggle.configure(text="Light")
    
def createWidgets():
    theme="primary"
    #print(tbs.Style().theme_names())
    bootstyle="link"
    root.cameraLabel = tbs.Label(master=root, bootstyle="primary", borderwidth=10, relief="solid")
    root.cameraLabel.place(relx=.5, rely=.5, anchor="center")

    browseButton = tbs.Button(root, width=30, text="Kaydın kaydedileceği adres", bootstyle=bootstyle, takefocus=True, image=folder, command=destBrowse)
    browseButton.place(rely=1, x=5, y=-5, anchor="sw")

    captureButton = tbs.Button(root, text="Fotoğraf Çek",bootstyle=bootstyle, image=cam_cap, command=capture)
    captureButton.place(rely=0.5, relx=1, x=-60, y=40, anchor="center")

    root.recordButton = tbs.Button(root, text="Video Çek", bootstyle=bootstyle, image=cam_rec, command=increaseControl)
    root.recordButton.place(rely=0.5, relx=1, x=-60, y=-40,  anchor="center")
    
    root.pauseVideoButton = tbs.Button(root, text="Videoyu duraklat",bootstyle=bootstyle, image=pause_button, command=pauseCommand)
    #root.pauseVideoButton.place(rely=0.5, relx=1, x=-60, y=-120, anchor="center")
    #root.pauseVideoButton.place_forget()
    
    photoButton = tbs.Button(root, text="Dosyayı Aç",bootstyle=bootstyle, image=image, command=openImage)
    photoButton.place(rely=1, relx=1, x=-5, y=-5, anchor="se")

    root.roundToggle = tbs.Checkbutton(root, bootstyle=f"{theme}, round-toggle", text="Dark", command=changeTheme)
    root.roundToggle.place(relx=1, x=-10, y=5, anchor="ne")
    
    root.flipToggle = tbs.Checkbutton(root, bootstyle=f"{theme}, round-toggle", text="Flip", command=increaseFlip)
    root.flipToggle.place(relx=1, x=-18, y=30, anchor="ne")
    
    #Brightness Buttons
    root.brightCheck = tbs.Checkbutton(root, bootstyle=f"outline-toolbutton-{theme}", image=brightness, command=openScaler1)
    root.brightCheck.place(rely=0.5, x=10, y=-21, anchor="w")
    
    root.brightScale = tbs.Scale(root, bootstyle="warning", length=200, orient="vertical", cursor="circle", from_=50, to=-50, value=0, command=scaler2)
    #root.brightScale.place(rely=0.5, x=30, anchor="w")
    
    root.brightValue = tbs.Label(root, bootstyle="warning",text=f'{int(root.brightScale.get())*2}%')
    #root.brightValue.place(rely=0.5, x=30, y=-150, anchor="w")
    
    root.brightLabel = tbs.Label(root, text="Brightness", font=('Segoe UI',12))
    #root.brightLabel.place(rely=0.5, x=30, y=-150, anchor="w")
    
    #Contrass Buttons
    root.contrastCheck = tbs.Checkbutton(root, bootstyle=f"outline-toolbutton-{theme}", image=contrast, command=openScaler2)
    root.contrastCheck.place(rely=0.5, x=10, y=21, anchor="w")
    
    root.contrastScale = tbs.Scale(root, bootstyle="warning", length=200, orient="vertical", cursor="circle", from_=2, to=0, value=1, command=scaler1)
    #root.contrastScale.place(rely=0.5, x=70, anchor="w")
    
    root.contrastValue = tbs.Label(root, bootstyle="warning",text=f'{float(root.contrastScale.get())*50}%')
    #root.contrastValue.place(rely=0.5, x=70, y=-150, anchor="w")
    
    root.contrastLabel = tbs.Label(root, text="Contrast", font=('Segoe UI',12))
    #root.contrastLabel.place(rely=0.5, x=70, y=-50, anchor="w")
    
    flag = tbs.Label(root, text="Bayrak", image=noble)
    flag.place(anchor="nw")
    
    camera()

s1 = 0
def openScaler1():
    global s1
    s1+=1
    if s1 % 2 == 1:
        root.brightScale.place(rely=0.5, x=120, anchor="w")
        root.brightValue.place(rely=0.5, x=120, y=-150, anchor="w")
        root.brightLabel.place(rely=0.5, x=80, y=130, anchor="w")
    else:
        root.brightScale.place_forget()
        root.brightValue.place_forget()
        root.brightLabel.place_forget()

s2 = 0
def openScaler2():
    global s2
    s2+=1
    if s2 % 2 == 1:
        root.contrastScale.place(rely=0.5, x=220, anchor="w")
        root.contrastValue.place(rely=0.5, x=210, y=-150, anchor="w")
        root.contrastLabel.place(rely=0.5, x=190, y=130, anchor="w")
    else:
        root.contrastScale.place_forget()
        root.contrastValue.place_forget()
        root.contrastLabel.place_forget()

def scaler1(e):
    global frame
    frame = cv.convertScaleAbs(frame,alpha=root.contrastScale.get(), beta=int(root.brightScale.get()))
    root.contrastValue.configure(text=f'{float(root.contrastScale.get())*50:.4}%')
    return frame

def scaler2(e):
    global frame
    frame = cv.convertScaleAbs(frame,alpha=root.contrastScale.get(),beta=int(root.brightScale.get()))
    root.brightValue.configure(text=f'{int(root.brightScale.get())*2}%')
    return frame

"""
j = 1
def flip():
    global frame, j
    if j % 2 == 1:
        frame = cv.flip(frame,1)
    j+=1
    return frame
"""

flipControl = 0
def increaseFlip():
    global flipControl
    flipControl+=1

recordControl = 0
def increaseControl():
    global recordControl
    recordControl = recordControl+1

p = 0
def pauseCommand():
    global p
    p+=1

k = 1
def audioRecord(k):
    global stream, frames_per_buffer, audio_frames, audio, filename, channels, rate, format
    if k == 1:
        rate, frames_per_buffer, channels = 26825, 1024, 2
        format = pyaudio.paInt32
        audioTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")   
        audioPath = destPath.get()
        filename = audioPath + "\\" + audioTime + ".wav"
        
        audio = pyaudio.PyAudio()  # Create an interface to PortAudio
        
        stream = audio.open(format=format, channels=channels, rate=rate, frames_per_buffer=frames_per_buffer, input=True)
        audio_frames = []  # Initialize array to store frames
    if k == 2:
        data = stream.read(frames_per_buffer)
        audio_frames.append(data)
    if k == 3:
        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        audio.terminate()
        
        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(audio_frames))
        wf.close()
 

def camera():
    global out, recordControl, p, frame, k, videoName
    
    ret,frame = root.cam.read()
    
    if ret == True:
        if flipControl % 2 == 0:
            frame = cv.flip(frame,1)
        frame = scaler1(frame)
        frame = scaler2(frame)
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
                videoName = videoPath + "\\" + videoTime + ".mp4"
                fourcc = cv.VideoWriter_fourcc(*"mp4v")
                out = cv.VideoWriter(videoName, fourcc, 25, (width_1,height_1))
                increaseControl()
                audioRecord(k=1)
                print(recordControl)
            else:
                Messagebox.show_error(message="Directory is not selected for video storing", title="Error")
                recordControl = 0
            #out = destVideo()
            
        elif recordControl == 2 and p % 2 == 0:
            out.write(frame)
            audioRecord(k=2)
            root.recordButton.configure(text="Video Durdur", image=stop_button)
            root.pauseVideoButton.configure(image=pause_button)
            root.pauseVideoButton.place(rely=0.5, relx=1, x=-60, y=-120, anchor="center")
        elif p % 2 == 1:
            root.pauseVideoButton.configure(text="Videoyu devam ettir", image=play_button)
        elif recordControl == 3:
            root.recordButton.configure(text="Video Başlat", image=cam_rec)
            root.pauseVideoButton.place_forget()
            out.release()
            audioRecord(k=3)
            
            video_clip = VideoFileClip(videoName)
            audio_clip = AudioFileClip(filename)
            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(videoName + ".mp4")
            os.remove(filename)
            os.remove(videoName)
            
            recordControl = 0
            p = 0
        
        root.cameraLabel.after(10,camera)
      
    else:
        root.cameraLabel.configure(image="")
    
def capture():
    imageTime = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    
    if destPath.get() != "":
        imagePath = destPath.get()
    else:
        Messagebox.show_error(message="Directory is not selected to image storing.\nPlease select directory by use left bottom button.", 
                              title="Error")
        
    imageName = imagePath + "\\" + imageTime + ".png"
    
    ret, frame = root.cam.read()
    if flipControl % 2 == 0:
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