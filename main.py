from tkinter import *
from tkinter import messagebox

ortalama = ''

def hesapla():
    global ortalama
    try:
        Not1 = float(not1Entry.get())
        Not2 = float(not2Entry.get())
        ortalama = (Not1 + Not2)/2   
        ortalama = str(ortalama)
        
    except:
        messagebox.showerror('HATA:sayi','Lütfen sayı giriniz!')

    finally:
    #     notOrtalamaEntry.delete('1.0', END)
    #     dersAdiEntry.delete(0, END)
    #     not1Entry.delete(0, END)
    #     not2Entry.delete(0, END)
        notOrtalamaEntry.insert(END, ortalama, 'style')

def sifirla():
    notOrtalamaEntry.delete('1.0', END)
    dersAdiEntry.delete(0, END)
    not1Entry.delete(0, END)
    not2Entry.delete(0, END)
    
def kaydet():
    s = messagebox.askyesno('Kaydet','Kaydetmek istediğinizden emin misiniz?')
    if s == True:
        with open('Not Ortalaması.txt','w',encoding='utf8') as dosya:
            dosya.write(f'Ders Adı={dersAdiEntry.get().upper()}:\n\n1.Not:{not1Entry.get()}\n2.Not:{not2Entry.get()}\nNot ortalaması:{ortalama}\n\n\n')
            sifirla()
    else:
        pass

pencere = Tk()

pencere.title('Not Ortalaması Hesaplayıcı')
pencere.iconbitmap('icon.ico')
pencere.configure(bg='#3B3939')

pencere.minsize(950,650)
pencere.attributes('-topmost', True)

not1Frame = Frame(pencere)
not2Frame = Frame(pencere)
hesaplaFrame = Frame(pencere,bg='#3B3939')
notOrtalamaFrame = Frame(pencere,bg='green')
dersAdiFrame = Frame(pencere,bg='red')
ustMenuFrame = Frame(pencere,bg='grey')

not1Frame.place(relx=0.2,rely=0.2,relheight=0.10,relwidth=0.35)
not2Frame.place(relx=0.2,rely=0.4,relheight=0.10,relwidth=0.35)
hesaplaFrame.place(relx=0.3,rely=0.6,relheight=0.10,relwidth=0.33)
notOrtalamaFrame.place(relx=0.1,rely=0.8,relheight=0.10,relwidth=0.80)
dersAdiFrame.place(relx=0.3,rely=0.05,relheight=0.05,relwidth=0.4)
ustMenuFrame.place(relwidth=1.0,relheight=0.03)


not1Yazi = Label(not1Frame,text='1.Notunuz:',bg='#3B3939',fg='white',font=('arial 50 bold italic'))
not2Yazi = Label(not2Frame,text='2.Notunuz:',bg='#3B3939',fg='white',font=('arial 50 bold italic'))
notOrtalamaYazi = Label(notOrtalamaFrame,bg='#3B3939',fg='white',text='Not Ortalamanız:',font=('arial 50 bold italic'))
dersAdiYazi = Label(dersAdiFrame,bg='#3B3939',fg='white',text='Ders adı:',font=('arial 30 bold italic'))

not1Yazi.pack(side=LEFT)
not2Yazi.pack(side=LEFT)
notOrtalamaYazi.pack(side=LEFT) 
dersAdiYazi.pack(side=LEFT)


not1Entry = Entry(not1Frame,font=('arial 50 bold italic'))
not2Entry = Entry(not2Frame,font=('arial 50 bold italic'))
dersAdiEntry = Entry(dersAdiFrame,font=('arial 20 bold italic'),width=100)

not1Entry.pack(side=LEFT)
not2Entry.pack(side=LEFT)
dersAdiEntry.pack(side=LEFT)


notOrtalamaEntry = Text(notOrtalamaFrame,font=('arial 50 bold italic'),state='normal')
notOrtalamaEntry.pack(side=LEFT)


hesaplaButton = Button(hesaplaFrame,text='Hesapla',font=('arial 50 bold italic'),command=hesapla)
kaydetButton = Button(ustMenuFrame,text='Kaydet',font=('arial 12 bold'),command=kaydet)
sifirlaButton = Button(ustMenuFrame,text='Sıfırla',font=('arial 12 bold'),command=sifirla)

hesaplaButton.pack(side=BOTTOM)
kaydetButton.pack(side=LEFT)
sifirlaButton.pack(side=RIGHT)

pencere.mainloop()
