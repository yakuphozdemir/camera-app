# camera_app
## EN
**Camera application by using tkinter library for interface**

 - This program was developed referanced by pythonpool's camera application. -> https://github.com/pythonpool/small-projects
 - When examine the codes, recommended to examine them in this order: 
 - createWidgets(), destBrowse(), deleteTempText(), imageBrowse(), camera(), capture(), startCamera(), stopCamera()
 - The comment lines have been tried to be wide in English and Turkish for new library learners.
 - For who bothered by the comment lines: Hide Comments by Elio Struyf, eliostruyf.com -> https://github.com/estruyf/vscode-hide-comments
 - Lastly who want to use colorful comments in vscode -> Better Comments by Aaron Bond, aaronbond.co.uk -> https://github.com/aaron-bond/better-comments

    _For compile the program, type command window -> pyinstaller camera.py --oneline_

## TR
**Arayüz tasarımında tkinter kütüphanesi kullanılarak oluşturulan kamera uygulaması**

  - Bu uygulama pythonpool tarafından yapılan kamera programı baz alınarak yapılmıştır -> https://github.com/pythonpool/small-projects
  - Kodlar incelenirken fonksiyonları createWidgets(), destBrowse(), deleteTempText(), imageBrowse(), camera(), capture(), startCamera(), stopCamera() sırasıyla incelenmesi tavsiye edilir.
  - Kütüphaneleri yeni öğrenenler için yorum satırları İngilizce ve Türkçe olarak geniş tutulmaya çalışılmıştır. 
  - Yorum satırlarından rahatsız olanlar için -> Hide Comments by Elio Struyf, eliostruyf.com -> https://github.com/estruyf/vscode-hide-comments
  - Son olarak, vscode'da renkli yorum satırları isteyenler için -> Better Comments by Aaron Bond, aaronbond.co.uk -> https://github.com/aaron-bond/better-comments

    _Programı compile etmek için, komut satırına şunu giriniz -> pyinstaller camera.py --oneline_


### Used modules and their versions;
### Kullanılan kütüphaneler ve versiyonları;
 * tkinter(8.6) / https://github.com/python/cpython/tree/main/Lib/tkinter / https://docs.python.org/3/library/tkinter.html
 * opencv(4.7.0) / https://github.com/opencv/opencv-python/  https://docs.opencv.org/4.x/
 * datetime / https://github.com/python/cpython/blob/main/Lib/datetime.py / https://docs.python.org/3/library/datetime.html
 * Pillow(9.4.0) / https://github.com/python-pillow/Pillow / https://pillow.readthedocs.io/en/stable/
 * pyinstaller(5.9.0) / https://github.com/pyinstaller/pyinstaller / https://pyinstaller.org/en/stable/


# camera_v2
**New Camera App that contains video recording, pausing and continuing and many features, additionly have new interface and less faulty**

  - This is not a update, this a new application.
  - Tttbootstrap is used for new user interface.

  - There are some steps for improve the app in the commits.
    - First and second commit is about first version of app.
    - camera_v2 commit includes new interface and the upper version of first version.
    - Fourth commit includes new icons about buttons.
    - In fifth commit flip, contrast, brightness settings were added, default theme is changed. In additionly, videos can be opened by using file open button. Just images could be opened in before versions however you can just open images and videos. If you try to open another type file, you face error message.
    - In the sixth commit, voice recording feature is added in video record.

**Important: Multiprocessing, thereading or ascynio is not used for voice recording. Therefore there are optimization and stabilization problems in the program. Recommended to use fifth commit.** 

### Contact 
- Yakup Hüseyin Özdemir
- Mail: yakuph.ozdemir@gmail.com
- Github: https://github.com/yakuphozdemir