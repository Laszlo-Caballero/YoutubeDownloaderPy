from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from youtube import YT
import threading
class App:
    def __init__(self, ventana):
        self.youtube = YT()
        self.ventana = ventana
        self.ventana.title("YoutubeDownloader")
        self.ventana.geometry("500x200")
        self.frame = Frame(self.ventana)
        self.frame.pack()
        self.containerTitle = Frame(ventana)
        self.containerTitle.pack(pady=20)
        self.logoImg = PhotoImage(file="./images/Youtube_logo.png").subsample(8,8)
        self.imgYt = Label(self.containerTitle, image=self.logoImg)
        self.imgYt.pack(side=LEFT, padx=10)
        self.lbl_saludo = Label(self.containerTitle, text="Descargar Youtube", font=("WorkSans", 15))
        self.lbl_saludo.pack(side=LEFT, padx=20)
        self.menu = ttk.Combobox(self.containerTitle, values=["Audio", "Video", "Playlist"], state="readonly")
        self.menu.current(0)
        self.menu.pack(side=RIGHT)
        self.urlVar = StringVar(ventana, value="", name="urlVar")
        self.urlVar.trace_add("write", self.obtenerTexto)
        self.input = Entry(ventana, width=60, textvariable=self.urlVar)
        self.input.pack()
        self.btnDownloader = Button(ventana, text="Descargar", command=self.Download, width=15, height=1)
        self.btnDownloader.config(state="disabled")
        self.btnDownloader.pack(pady=10)
    def obtenerTexto(self, *args):
        texto = self.urlVar.get()
        if "www.youtube.com/playlist" in texto and texto:
            self.btnDownloader.config(state="normal")
            self.menu.config(state="disabled")
            self.menu.current(2)
        elif "www.youtube.com" in texto and texto:
            self.btnDownloader.config(state="normal")
        else:
            self.menu.config(state="normal")
            self.btnDownloader.config(state="disabled")
    def Download(self, *args):
        threading.Thread(target=self.DownloadYoutube).start()
    def DownloadYoutube(self, *args):
        texto = self.urlVar.get()
        opcion = self.menu.get()
        self.btnDownloader.config(state="disabled")
        self.input.config(state="disabled")
        try:
            if opcion == "Audio":
                self.youtube.DownloadAudio(texto)
            elif opcion == "Video":
                self.youtube.DownloadVideo(texto)
            else:
                self.youtube.DownloadPlaylist(texto)
            messagebox.showinfo("Descarga", "Se descargo correctamente")
            self.btnDownloader.config(state="normal")
            self.input.config(state="normal")
        except:
            messagebox.showerror("Error", "Error en la descarga")
root = Tk()
aplication = App(root)
root.mainloop()