import instaloader
from tkinter import *
from tkinter import ttk , messagebox
from PIL import ImageTk , Image

class insta(Tk) :
    def __init__(self) :
        super().__init__()
        self.title('Instagram Downloader')
        self.geometry('560x220')
        self.configure(bg='white')
        self.resizable(False, False)

        self.get_username()
        self.LABLE()
        self.button()

    def get_username(self) :
        global string
        string = StringVar()
        self.entry = ttk.Entry(self, width=25, textvariable=string)
        self.entry.place(x=350, y=60)

    def LABLE(self) :
        img = Image.open('E:\\Programming\\Projects\\icons8-instagram-200.png')
        re = ImageTk.PhotoImage(img)

        self.img = ttk.Label(self, image=re)
        self.img.place(x=30, y=10)
        self.img = re

        self.lable = Label(self, text='Enter Username : ', bg='#ffffff')
        self.lable.place(x=250, y=60)

    def button(self) :
        self.btn = ttk.Button(self, width=25, text='Download', command=self.Download)
        self.btn.place(x=350, y=100)
    
    def Download(self) :
        text = string.get()
        if text != '' :
            img = instaloader.Instaloader()
            img.download_profile(text, profile_pic_only=True)
            messagebox.showinfo('Result', 'Image Downloaded')


app = insta()

app.mainloop()