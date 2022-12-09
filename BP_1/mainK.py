import PTS as pt
import kamera as km


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import ttk

#Window

window = tk.Tk()
window.geometry("1080x640")
window.title("Plaka Tanıma Sistemi!")

#Frames

frame_left = tk.Frame(window,width=540,height=640,bd="2")
frame_left.grid(row=0,column=0)

frame_right = tk.Frame(window,width=540,height=640,bd="2")
frame_right.grid(row=0,column=1)

frame1 = tk.LabelFrame(frame_left,text="Resim",width=540,height=500)
frame1.grid(row=0,column=0)

frame2 = tk.LabelFrame(frame_left,text="İşlemler",width=540,height=140)
frame2.grid(row=1,column=0)

frame3 = tk.LabelFrame(frame_right,text="Plakalar",width=540,height=640)
frame3.grid(row=0,column=0)

camphoto = tk.PhotoImage(file="cam.png")
dosyaphoto = tk.PhotoImage(file="dosya.png")

#Menubar
menubar = tk.Menu(window)
window.config(menu=menubar)
file = tk.Menu(menubar)
info = tk.Menu(menubar)

def filefunc():
    file_name = filedialog.askopenfilename(initialdir="veriseti3",title="Bir resim seçiniz...")
    img = Image.open(file_name)
    img = ImageTk.PhotoImage(img)

    labell = tk.Label(frame1,image=img)
    labell.image = img
    labell.grid(row=8,column=0)
def infofunc():
    messagebox.showinfo(title="Uygulama Hakkındaki Bilgiler!",message="190204023 Mahsun Can Akgül \n"
                                                                      "190204053 Barış Uyar \n"
                                                                      "Bitirme Projesi-1 \n"
                                                                      "Celal Alagöz \n")

def pts():
    message_box3 = messagebox.showinfo(title="Bilgilendirme!", message="Geçmek için 'Q' tuşuna basınız!")
    pt.resim()


def cam():
    message_box2 = messagebox.showinfo(title="Bilgilendirme!", message="Kapatmak için 'Q' tuşuna basınız!")
    km.kamera()


def search():
    message_box = messagebox.showerror(title="Uyarı!", message="Şuan için bu özellik çalışmıyor!")

def alg():
    message_box4 = messagebox.showinfo(title="Bilgilendirme!", message="Geçmek için 'Q' tuşuna basınız!")
    import alg1



menubar.add_cascade(label="Dosya",menu=file)
menubar.add_cascade(label="Daha Fazla",menu=info)
file.add_command(label="Resim Aç",command=filefunc)
info.add_command(label="Hakkında",command=infofunc)

button1 = tk.Button(frame2,text="Resim",activebackground="red",
                   bg="purple",fg="white",activeforeground="white",
                   command=pts)
button2 = tk.Button(frame2,text="Kamera",activebackground="red",
                   bg="purple",fg="white",activeforeground="white",
                  command=cam)
button3 = tk.Button(frame2,text="Ara",activebackground="red",
                   bg="purple",fg="white",activeforeground="white",
                  command=search)
button4 = tk.Button(frame2,text="Histogram",activebackground="red",
                   bg="purple",fg="white",activeforeground="white",
                  command=alg)

entry = tk.Entry(frame2,width=50)
entry.insert(string="Aranılan Plakayı Giriniz!",index=0)
#label1 = tk.Label(frame2,text="1",image=camphoto) #İstenilirse # işareti kaldırılıp resim ve kamera fotoğrafı gelebilir!
#label2 = tk.Label(frame2,text="1",image=dosyaphoto) #İstenilirse # işareti kaldırılıp resim ve kamera fotoğrafı gelebilir!
x=1

listBox = tk.Listbox(frame3)
listBox.insert(1,"Araç 1")
listBox.insert(2,"Araç 2")
listBox.insert(3,"Araç 3")
listBox.insert(4,"Araç 4")
listBox.insert(5,"Araç 5")
listBox.insert(6,"Araç 6")
listBox.insert(7,"Araç 7")
listBox.insert(8,"Araç 8")
listBox.insert(9,"Araç 9")
listBox.insert(10,"Araç 10")
listBox.insert(11,"Araç 11")
listBox.insert(12,"Araç 12")
listBox.insert(13,"Araç 13")
listBox.insert(14,"Araç 14")
listBox.insert(15,"Araç 15")

def getItem():
    index_list = listBox.curselection()
    y = listBox.get(index_list)
    img = Image.open("veriseti2/{}.png".format(y))
    img = ImageTk.PhotoImage(img)

    labell = tk.Label(frame1, image=img)
    labell.image = img
    labell.grid(row=8, column=0)

buttonnnn = tk.Button(frame3,text="Göster",command=getItem)


scroll = tk.Scrollbar(frame3,orient=tk.VERTICAL,command=listBox.yview)
listBox.config(yscrollcommand=scroll.set)



button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
entry.grid(row=0,column=3,padx=5)
button3.grid(row=0,column=4,padx=5,pady=5)
#label1.grid(row=1,column=1) #İstenilirse # işareti kaldırılıp resim ve kamera fotoğrafı gelebilir!
#label2.grid(row=1,column=0) #İstenilirse # işareti kaldırılıp resim ve kamera fotoğrafı gelebilir!
listBox.grid(row=0,column=0)
scroll.grid(row=0,column=1,sticky=tk.N +tk.S)
buttonnnn.grid(row=1,column=1)
button4.grid(row=0,column=2)



window.mainloop()
