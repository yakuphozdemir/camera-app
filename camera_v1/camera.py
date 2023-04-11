#*  
# ! EN This program was developed referanced by pythonpool's camera application. -> https://github.com/pythonpool/small-projects
# ! When examine the codes, recommended to examine them in this order: 
# ! createWidgets(), destBrowse(), deleteTempText(), imageBrowse(), camera(), capture(), startCamera(), stopCamera()
# ! The comment lines have been tried to be wide in English and Turkish for new library learners.
# ! For who bothered by the comment lines: Hide Comments by Elio Struyf, eliostruyf.com -> https://github.com/estruyf/vscode-hide-comments
# TODO Lastly who want to use colorful comments in vscode -> Better Comments by Aaron Bond, aaronbond.co.uk -> https://github.com/aaron-bond/better-comments
# ***********************************************************************************************************************************************
# ? TR Bu uygulama pythonpool tarafından yapılan kamera programı baz alınarak yapılmıştır -> https://github.com/pythonpool/small-projects
# ?  Kodlar incelenirken fonksiyonları createWidgets(), destBrowse(), deleteTempText(), imageBrowse(), camera(), capture(), startCamera(),
# ?  stopCamera() sırasıyla incelenmesi tavsiye edilir.
# ?  Kütüphaneleri yeni öğrenenler için yorum satırları İngilizce ve Türkçe olarak geniş tutulmaya çalışılmıştır. 
# ?  Yorum satırlarından rahatsız olanlar için -> Hide Comments by Elio Struyf, eliostruyf.com -> https://github.com/estruyf/vscode-hide-comments
# TODO Son olarak, vscode'da renkli yorum satırları isteyenler için -> Better Comments by Aaron Bond, aaronbond.co.uk -> https://github.com/aaron-bond/better-comments
# *#

import tkinter as tk
import cv2 as cv
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

#EN Creating object of tk class       
#TR tk modülünün Tk sınıfından obje oluşturma
root = tk.Tk()

#EN The most beautiful horse in the world for photo window when start-up ;)
#TR Fotoğraf penceresi için program başlatıldığında ilk açılış için dünyanın en güzel atının fotoğrafı ;)
imagee = ImageTk.PhotoImage(Image.open('horse2.jpg').resize((640, 480)))
#or <>
#imagee = tk.PhotoImage(file="image.png").resize(640, 480)

#EN Setting the title, window size, background color and disabling the resizing property
#TR Başlığı, pencere boyutunu, arkaplan rengini ve pencerenin boyutunu değiştirme ayarını yapma
root.title("Camera")
root.geometry("1920x1080")
root.resizable(True,True)
bg = "#262626"
#print(tk.Tk().configure().keys())
root.configure(background=bg)

#EN Creating object of class VideoCapture with webcam index
#TR Kamerayı açmak adına VideoCapture sınıfını çağırıp root objesinde bir değişkene atama 
root.cam = cv.VideoCapture(0)

#EN Creating tkinter variables
#TR Çekilecek ve sonradan açılacak fotoğraflar için adres atamak adına string tipinde değişken oluşturma 
destPath = tk.StringVar()
imagePath = tk.StringVar()

def destBrowse():
    #EN Presenting user with a pop-up for directory selection. initialdir argument is optional 
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    #TR Çekilecek fotoğrafın kaydedileceği adresi belirlemek adına gerekli bir fonksiyon. 
    # initialdir browse tuşuna basıldığında default olarak açılacak klasör konumu için kullanılıyor, kullanmak şart değildir
    directory = filedialog.askdirectory(initialdir="")
    
    #EN Displaying the directory in the directory textbox
    #TR Boş olarak atanan destPath'e, directory'ye tanımlanan konumu atama
    destPath.set(directory)
    
def deleteTempText(herhangiKelime):
    #EN The function that requires for delete to temporary text which on the browse bar
    # If any parameter is not typed in function, the function will not work
    #TR Arama çubuğuna tıklandığında geçici yazının ortadan kalkması için gereken fonksiyon
    # Eğer fonksiyonun içine herhangi bir parametre yazılmazsa fonksiyon çalışmaz
    root.saveLocationEntry.delete(0,"end")

def imageBrowse():
    #EN Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    #TR Açılacak resmin adresini belirtmek adına gerekli bir fonksiyon. 
    # initialdir browse tuşuna basıldığında default olarak açılacak klasör konumu için kullanılıyor, kullanmak şart değildir
    openDirectory = filedialog.askopenfilename(initialdir="")
    
     #EN Displaying the directory in the directory textbox
     #TR Boş olarak atanan imagePath'e, bir önceki satırda openDirectory'ye tanımlanan dosyanın konumunu atama 
    imagePath.set(openDirectory)
    
    #EN Opening the saved image using the open() of Image class which takes the saved image as the argument
    #TR Image sınıfına bağlı, kaydedilen resmi argüman olarak alan open() fonksiyonuyla konumu kaydedilen dosyanın açılması 
    imageView = Image.open(openDirectory)
    
    #EN Resizing the image using Image.resize()
    #TR Seçilen fotoğrafın boyutunu ayarlama
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    
    #EN Creating object of PhotoImage() class to display the frame
    #TR PhotoImage sınıfında, seçilen resmi çerçevede göstermeyi sağlayan objeyi oluşturma
    # Böylece resim root a bağlı imageLabel çerçevesi içerisinde gösterilebilecek
    imageDisplay = ImageTk.PhotoImage(imageResize)
    
    #EN Configuring the label to display the frame
    #TR root da daha önce oluşturulan imageLabel çerçevesine seçtiğimiz resmi atama
    # Böylece eğer 'image=' a atanan başka bir resim varsa onu kaldırıyoruz ve yerine yeni seçtiğimiz resmi atıyoruz
    root.imageLabel.config(image=imageDisplay)
    
    #EN Keeping a reference
    # When you forget to do is include the root.imageLabel.photo=imageDisplay, to prevent garbage collection from deleting the image.
    #TR Resmi imageLabel'a referans olarak tutma
    # Garbage collection, pythonda hafızada kullanılmayan gereksiz değişkenlerin/allocation'ların silinmesine yarayan bir mekanizma
    # Kısacası bir değişkene kaydetmediğinde python o resmi silebiliyor
    # c'de malloc ile yer açtığında manuel olarak free yapmak gerekir
    # Bu tarz yüksek seviyeli dillerde garbage collection vardır, otomatik olarak kullanılmayan yerleri free'ler
    root.imageLabel.photo = imageDisplay

#EN Defining createWidgets() function to create necessary tkinter widgets
#TR Tkinter Widgetlarının oluşturulması
def createWidgets(root):
    #EN Create "Canlı Kamera" sentence label
    #TR Canlı Kamera yazısını ekleme                            
    feedLabel = tk.Label(root, bg=bg, fg="white", text="Canlı Kamera", font=('Segoe UI',20))                        
    feedLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)        # padx,pady = coordinates of x and y
    
    #EN Create camera window widget
    #TR Kamera çerçevesini ekleme
    root.cameraLabel = tk.Label(root, background=bg, borderwidth=10, relief="groove")        #print(tk.Label().relief.keys()) ???????
    root.cameraLabel.grid(row=2, column=1, padx=70, pady=10, columnspan=2)
    
    #EN Create browse bar under the camere window
    #TR Kamera çerçevesinin altına adres çubuğu ekleme
    root.saveLocationEntry = tk.Entry(root, width=80, textvariable=destPath)
    root.saveLocationEntry.insert(0, "Fotoğrafın Kaydedileceği Adresi Yazınız...")
    root.saveLocationEntry.grid(row=3, column=1, sticky="w", padx=70, pady=10)
    root.saveLocationEntry.bind("<FocusIn>", deleteTempText)
    
    #EN Create left browse button
    #TR Sol Browse Button
    root.browseButton = tk.Button(root, width=20, text="Fotoğraf Adresi için Tara", command=destBrowse)
    root.browseButton.grid(row=3, column=1, padx=70, pady=10, columnspan=4)
    
    #EN Create capture button
    #TR Fotoğraf çekme butonu
    root.captureButton = tk.Button(root, text="Fotoğraf Çek", command=capture, bg="white", font=('Segoe UI', 20), width=20)
    root.captureButton.grid(row=4, column=1, padx=10, pady=10, columnspan=5)
    
    #EN Create stop-start button
    #TR Kamerayı Durur butonu
    root.cameraButton = tk.Button(root, text="Kamerayı Durdur",font=('Segoe UI', 15), command=stopCamera, width=15)
    root.cameraButton.grid(row=5,column=1, padx=10, pady=10, columnspan=5)
    
    #EN Create "Resim Önizleme" sentence label
    #TR Resim Önizleme yazısı
    root.previewLabel = tk.Label(root, bg=bg, fg="white", text="Resim Önizleme", font=('Segoe UI', 20))
    root.previewLabel.grid(row=1, column=4, padx=10, pady=10, columnspan=2)
    
    #EN Create window that show captured photo or display selected images
    #TR Çekilen Resmin bulunduğu çerçeveyi ekleme
    root.imageLabel = tk.Label(root, bg=bg, borderwidth=10, image=imagee, relief="groove")
    root.imageLabel.grid(row=2, column=4, padx=10, pady=10, columnspan=2)
    
    #EN Create browse bar under imageLabel
    #TR Fotoğraf çerçevesinin altına adres çubuğu ekleme
    root.openImageEntry = tk.Entry(root, width=80, textvariable=imagePath)
    root.openImageEntry.grid(row=3, column=4, padx=10, pady=10)
    
    #EN Create right browse button
    #TR Sağ browse butonu
    root.openImageButton = tk.Button(root, width=20, text="Çekilen Fotoğrafları Tara", command=imageBrowse)
    root.openImageButton.grid(row=3, column=5, padx=10, pady=10)
    
    camera()

#EN Defining camera() function to display webcam feed in the cameraLabel;
#TR cameraLabel çerçevesinde kameranın çıktısının gösterilmesi için camera() fonksiyonunu tanımlanması
def camera():
    #EN Capturing frame by frame
    #TR Kameranın çalıştırılması
    ret, frame = root.cam.read()
    
    if ret:
        #EN Flipping the frame vertically
        #TR Çerçevenin aynalanması
        frame = cv.flip(frame,1)
        
        #EN Displaying date and time on the feed
        #TR Çerçevede tarih ve zamanın gösterilmesi
        cv.putText(frame, datetime.now().strftime('%d/%m/%Y %H:%M:%S'),(430,460), cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
        
        #EN Changing the frame color from BGR to RGB
        #TR Çerçeve renginin BGR'den RGB'ye dönüştürülmesi
        frame2 = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        
        #EN Creating an image memory from the above frame exporting array interface
        #TR Çerçevenin yani kameradan bize array olarak gelen görüntüden görüntü belleği oluşturma
        videoImage = Image.fromarray(frame2)
        #print(frame2)             # -> array
        #print(videoImage)         # -> <PIL.Image.Image image mode=RGBA size=640x480 at 0x199FF603AF0>
        
        #EN Creating object of PhotoImage() class to display the frame  
        #TR PhotoImage sınıfında, framedeki görüntüyü çerçevede göstermeyi sağlayan objeyi oluşturma
        imageTk = ImageTk.PhotoImage(image = videoImage)
        #print(imageTk)            # ->pyimage64
        
        #EN Configuring the label to display the frame
        #TR Kameranın anlık olarak çektiği görüntü olan imageTk'yı cameraLabel'a atama
        root.cameraLabel.configure(image=imageTk)
        
        #EN Keeping a reference
        #TR Referans tutma
        root.cameraLabel.imageTk = imageTk
    
        #EN Calling the function after 10 milliseconds
        #TR Fonksiyonu 10 milisaniye sonra çağırma
        root.cameraLabel.after(10, camera)
        
    else:
        #EN Configuring the label to display the frame
        #TR cameraLabel çerçevesindeki görüntüyü kaldırma
        root.cameraLabel.configure(image='')       
        
def capture():
    #EN Storing the date in the mentioned format in the imageTime variable
    #TR capture() fonksiyonu çalıştırıldığında o anda ki zamanı imageTime değişkenine belirtilen formatta kaydetme
    imageTime = datetime.now().strftime('%d-%m-%Y %H-%M-%S')
    
    #EN If the user has selected the destination directory, then get the directory and save it in imagePath
    #TR Eğer kullanıcı fotoğrafın kaydedileceği konumu seçerse, bu konum imagePath değişkenine kaydedilecek
    if destPath.get() != "":
        imagePath = destPath.get()
    #EN If the user has not selected any destination directory, then set the imagePath to default directory
    #TR Eğer kullanıcı herhangi bir konum seçmezse, uygulama konum seçilmediğine dair hata bâbından mesaj kutusu oluşturacak
    else:
        messagebox.showerror("Error", "No Directory Selected to Store Image")
        
    #EN Concatenating the imagePath with imageTime and with .jpg extension and saving it in imageName variable
    #TR Oluşturulacak dosyanın dizin adı için yoluyla beraber isim ve uzantısının imageName değişkenine atanması
    imageName = imagePath + '\\' + imageTime + ".jpg"
    
    #EN Capturing the frame
    #TR Kamerayı açma
    ret, frame = root.cam.read()
    frame = cv.flip(frame,1)
    
    #EN Displaying date and time on the frame
    #TR Frame'e anlık tarih ve zamanı ekleme 
    cv.putText(frame, datetime.now().strftime("%d/%m/%Y %H:%M:%S"),(430,460), cv.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255))
    
    #EN Writing the image with the captured frame. Function returns a Boolean Value which is stored in success variable
    #TR Çekilen fotoğrafı kaydetme. imageName anlık frame'in kaydedileceği dizini ifade edem stringtir.frame de o anki görüntüdür.
    # imrite ile frame'deki görüntü imageName dizinine kaydedilir. Fonksiyon success değişleninde depolanan bir boolean değeri döndürür.
    success = cv.imwrite(imageName, frame)
    
    #EN Opening the saved image using the open() of Image class which takes the saved image as the argument
    #TR Image sınıfına bağlı, kaydedilen resmi argüman olarak alan open() fonksiyonuyla konumu 
    savedImage = Image.open(imageName)
    
    #EN Creating object of PhotoImage() class to display the frame
    #TR PhotoImage sınıfında, savedImage'daki görüntüyü çerçevede göstermeyi sağlayan objeyi oluşturma
    savedImage = ImageTk.PhotoImage(savedImage)
    
    #EN Configuring the label to display the frame
    #TR imageLabel çerçevesindeki görüntüye savedImage olarak güncelleme
    root.imageLabel.config(image=savedImage)
     
    #EN Keeping a reference
    #TR imageLabel'a referans tutma
    root.imageLabel.photo = savedImage
    
    #EN Displaying messagebox
    #TR Fotoğraf başarılı şekilde çekilip kaydedildiği takdirde mesaj kutusu gösterme
    if success:
        messagebox.showinfo("Success", "Image Captured and saved in." + imageName)

def startCamera():
    #EN Creating object of class VideoCapture with webcam index
    #TR Kamerayı açmak adına VideoCapture sınıfını çağırıp root objesinde bir değişkene atama 
    root.cam = cv.VideoCapture(0)
    
    """
    #EN Setting width and height
    #TR Uzunluk ve Genişliği ayarlama
    width_1, height_1 = 640, 480
    root.cam.set(cv.CAP_PROP_FRAME_WIDTH, width_1)
    root.cam.set(cv.CAP_PROP_FRAME_HEIGHT, height_1)
    """
    #EN Configuring the cameraButton to display accordingly
    #TR Görüntünün gelmesiyle beraber cameraButton'un kemarayı kapatma tuşu haline getirilmesi
    root.cameraButton.config(text="Kamerayı Kapat", command=stopCamera, bg="white")
    #EN Removing text message from the camera label
    #TR Kapalı olan kameranın açılmasıyla cameraLabel'da bulunan yazının silinmesi
    root.cameraLabel.config(text="")
    
    #EN Calling the camera() Function
    #TR camera() fonksiyonunun çağırılması
    camera()

def stopCamera():
    #EN Stopping the camera using release() method of cv2.VideoCapture()
    #TR Kameranın kapatılması
    root.cam.release()
    
    #EN Configuring the cameraButton to display accordingly
    #TR Kameranın kapatılmasıyla beraber cameraButton'un kamerayı açma tuşu haline getirilmesi
    root.cameraButton.config(text="Kamerayı Aç", command=startCamera)
    #EN Displaying text message in the cameraLabel
    #TR Kameranın kapatılmasıyla boş olan cameraLabel'a "Kamerayı Kapat yazısının yazılması"
    root.cameraLabel.config(text="Kamerayı Kapat", font=('Segoe UI', 70), fg="white", borderwidth=0)


createWidgets(root)
root.mainloop()

"""
# Setting width and height
width, height = 640, 480
cam.set(cv.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, height)
"""

"""
fps = cam.get(cv.CAP_PROP_FPS)
frame_count = cam.get(cv.CAP_PROP_FRAME_COUNT)
resolution = cam.get(cv.CAP_PROP_FRAME_HEIGHT), cam.get(cv.CAP_PROP_FRAME_WIDTH)
print("fps: ", fps, "\nframe_count: ", frame_count, "\nresolution: ", resolution)
"""

"""
width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv.CAP_PROP_FPS)
frame_count = cam.get(cv.CAP_PROP_FRAME_COUNT)
saturation = cam.get(cv.CAP_PROP_SATURATION)
speed = cam.get(cv.CAP_PROP_SPEED)

print("\n\twidth: {}\n\
        height: {}\n\
        fps: {}\n\
        frame count: {}\n\
        saturation: {}\n\
        speed: {}".format(width,height,fps,frame_count,saturation,speed))
"""