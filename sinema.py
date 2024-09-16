import tkinter as tk
from tkinter import messagebox
import db as db
import dbSetup as dbSetup
# import pencereMenu as menu
class Sinema():
    def __init__(self):
        # Veritabanı oluşturma ve tabloları oluşturma işlemi
        self.dbSetup = dbSetup.dbSetup()
        self.dbSetup.connect()
        self.dbSetup.create_database()
        self.dbSetup.create_tables()
        self.dbSetup.disconnect()
        self.db = db.dbClass()
        self.sorgular()
        self.anaPencere()
        self.pencere.mainloop()
    def sorgular(self):
        # veritabanı bağlantısını açtım
        self.db.connect()
        # film isimlerini çekip bir değişkene koydum
        self.film1dbAdi = self.db.filmAdi(1)
        self.film2dbAdi = self.db.filmAdi(2)
        # self.film2dbAdi = list(self.film2dbAdi)
        self.film3dbAdi = self.db.filmAdi(3)
        # self.film3dbAdi = list(self.film3dbAdi)
        self.film4dbAdi = self.db.filmAdi(4)
        # self.film4dbAdi = list(self.film4dbAdi)
        self.film5dbAdi = self.db.filmAdi(5)
        # self.film5dbAdi = list(self.film5dbAdi)
        self.film6dbAdi = self.db.filmAdi(6)
        # self.film6dbAdi = list(self.film6dbAdi)

        # filmlerin konusu bir değişkene koyalım
        self.film1dbKonu = self.db.filmKonu(1)
        self.film2dbKonu = self.db.filmKonu(2)
        self.film3dbKonu = self.db.filmKonu(3)
        self.film4dbKonu = self.db.filmKonu(4)
        self.film5dbKonu = self.db.filmKonu(5)
        self.film6dbKonu = self.db.filmKonu(6)
        
        self.film1tur = self.db.turCek(self.film1dbAdi)
        self.film2tur = self.db.turCek(self.film2dbAdi)
        self.film3tur = self.db.turCek(self.film3dbAdi)
        self.film4tur = self.db.turCek(self.film4dbAdi)
        self.film5tur = self.db.turCek(self.film5dbAdi)
        self.film6tur = self.db.turCek(self.film6dbAdi)

        self.db.disconnect()
        # veritabanı bağlantısını kapattım
    def koltukSil(self,filmAd):

        try:
            self.db.connect()
            self.db.koltuklariSil(filmAd)
            self.db.disconnect()
            messagebox.showinfo("Bilgi","Bütün Koltuklar Silindi")
        except:
            messagebox.showerror("Hata","Bir Hata Oluştu")

    def anaPencere(self):
        self.pencere = tk.Tk()
        self.pencere.title("Sinema")
        self.pencere.geometry("750x700")
        self.pencere.configure(background="#181717")
        
        # self.pencere.attributes("-fullscreen", True)
        self.pencere.resizable(False, False)
        self._menu(self.pencere)

        self.filmButon1resim = tk.PhotoImage(file="1.png")
        self.filmButon2resim = tk.PhotoImage(file="2.png")
        self.filmButon3resim = tk.PhotoImage(file="3.png")
        self.filmButon4resim = tk.PhotoImage(file="4.png")
        self.filmButon5resim = tk.PhotoImage(file="5.png")
        self.filmButon6resim = tk.PhotoImage(file="6.png")

        self.filmButon1 = tk.Button(self.pencere,image=self.filmButon1resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film1)
        self.filmButon1.place(x=100,y=0)
        self.film1Baslik = tk.Label(self.pencere,text=self.film1dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film1Baslik.place(x=100,y=270)
        self.film1DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film1Detay)
       
        self.film1DetayButon.place(x=100,y=3)
        
        
        self.filmButon2 = tk.Button(self.pencere,image=self.filmButon2resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film2)
        self.filmButon2.place(x=300,y=0)
        self.film2Baslik = tk.Label(self.pencere,text=self.film2dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film2Baslik.place(x=300,y=270)
        self.film2DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film2Detay)
        self.film2DetayButon.place(x=300,y=3)

        self.filmButon3 = tk.Button(self.pencere,image=self.filmButon3resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film3)
        self.filmButon3.place(x=500,y=0)
        self.film3Baslik = tk.Label(self.pencere,text=self.film3dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film3Baslik.place(x=500,y=270)
        self.film3DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film3Detay)
        self.film3DetayButon.place(x=500,y=3)

        self.filmButon4 = tk.Button(self.pencere,image=self.filmButon4resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film4)
        self.filmButon4.place(x=100,y=350)
        self.film4Baslik = tk.Label(self.pencere,text=self.film4dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film4Baslik.place(x=100,y=620)
        self.film4DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film4Detay)
        self.film4DetayButon.place(x=100,y=353)

        self.filmButon5 = tk.Button(self.pencere,image=self.filmButon5resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film5)
        self.filmButon5.place(x=300,y=350)
        self.film5Baslik = tk.Label(self.pencere,text=self.film5dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film5Baslik.place(x=300,y=620)
        self.film5DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film5Detay)
        self.film5DetayButon.place(x=300,y=353)

        self.filmButon6 = tk.Button(self.pencere,image=self.filmButon6resim,width=160,height=300,foreground="#181717",bg="#F3F9D2",command=self.film6)
        self.filmButon6.place(x=500,y=350)
        self.film6Baslik = tk.Label(self.pencere,text=self.film6dbAdi,font=("Arial",12,"bold"),height=2,background="#282927",foreground="white",width=16)
        self.film6Baslik.place(x=500,y=620)
        self.film6DetayButon = tk.Button(self.pencere,text="Detay",background="#282927",foreground="#BDC4A7",width=5,height=2,command=self.film6Detay)
        self.film6DetayButon.place(x=500,y=353)
    def film1Detay(self):
        self.film1DetayPencere = tk.Toplevel(self.pencere)
        self.film1DetayPencere.title(f"{self.film1dbAdi} konusu")
        # self.film1DetayPencere.configure(background="#181717")

        # self.film1DetayPencere.resizable(False, False)
        self.film1DetayLabel = tk.Label(self.film1DetayPencere,text=self.film1dbKonu,font=("Arial",10,"bold"))
        self.film1DetayLabel.pack()
        self.film1DetayLabel.configure(background="#181717")
        self.film1DetayLabel.configure(foreground="white")
        self.film1DetayPencere.grab_set()
        self.film1DetayPencere.focus_set()
    def film2Detay(self):
        self.film2DetayPencere = tk.Toplevel(self.pencere)
        self.film2DetayPencere.title(f"{self.film2dbAdi} konusu")
        # self.film2DetayPencere.resizable(False, False)
        self.film2DetayLabel = tk.Label(self.film2DetayPencere,text=self.film2dbKonu,font=("Arial",10,"bold"))
        self.film2DetayLabel.pack()
        self.film2DetayLabel.configure(background="#181717")
        self.film2DetayLabel.configure(foreground="white")
        self.film2DetayPencere.grab_set()
        self.film2DetayPencere.focus_set()
    def film3Detay(self):
        self.film3DetayPencere = tk.Toplevel(self.pencere)
        self.film3DetayPencere.title(f"{self.film3dbAdi} konusu")
        # self.film3DetayPencere.resizable(False, False)
        self.film3DetayLabel = tk.Label(self.film3DetayPencere,text=self.film3dbKonu,font=("Arial",10,"bold"))
        self.film3DetayLabel.pack()
        self.film3DetayLabel.configure(background="#181717")
        self.film3DetayLabel.configure(foreground="white")
        self.film3DetayPencere.grab_set()
        self.film3DetayPencere.focus_set()
    def film4Detay(self):
        self.film4DetayPencere = tk.Toplevel(self.pencere)
        self.film4DetayPencere.title(f"{self.film4dbAdi} konusu")
        # self.film4DetayPencere.resizable(False, False)
        self.film4DetayLabel = tk.Label(self.film4DetayPencere,text=self.film4dbKonu,font=("Arial",10,"bold"))
        self.film4DetayLabel.pack()
        self.film4DetayLabel.configure(background="#181717")
        self.film4DetayLabel.configure(foreground="white")
        self.film4DetayPencere.grab_set()
        self.film4DetayPencere.focus_set()
    def film5Detay(self):
        self.film5DetayPencere = tk.Toplevel(self.pencere)
        self.film5DetayPencere.title(f"{self.film5dbAdi} konusu")
        # self.film5DetayPencere.resizable(False, False)
        self.film5DetayLabel = tk.Label(self.film5DetayPencere,text=self.film5dbKonu,font=("Arial",10,"bold"))
        self.film5DetayLabel.pack()
        self.film5DetayLabel.configure(background="#181717")
        self.film5DetayLabel.configure(foreground="white")
        self.film5DetayPencere.grab_set()
        self.film5DetayPencere.focus_set()
    def film6Detay(self):
        self.film6DetayPencere = tk.Toplevel(self.pencere)
        self.film6DetayPencere.title(f"{self.film6dbAdi} konusu")
        # self.film6DetayPencere.resizable(False, False)
        self.film6DetayLabel = tk.Label(self.film6DetayPencere,text=self.film6dbKonu,font=("Arial",10,"bold"))
        self.film6DetayLabel.pack()
        self.film6DetayLabel.configure(background="#181717")
        self.film6DetayLabel.configure(foreground="white")
        self.film6DetayPencere.grab_set()
        self.film6DetayPencere.focus_set()
          
    def film1(self):
        
        self.koltukNumaraları1 = []
        self.film1Pencere = tk.Toplevel(self.pencere)
        # tam ekran yap
        # self.film1Pencere.attributes("-fullscreen", True)
        self.film1Pencere.title(f"{self.film1dbAdi}")
        self.film1Pencere.geometry("750x700")
        self.film1Pencere.configure(bg="#181717")
        self.film1Pencere.resizable(False, False)
        self.filmBirKoltuk = ['A','B','C','D','E','F','G','H']
        for i,koltukIsım in enumerate(self.filmBirKoltuk):
            for j in range(1,11):
                self.koltukButton = tk.Button(self.film1Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film1Pencere,self.koltukNumaraları1))
                self.koltukButton.grid(row=i, column=j, pady=5)
                self.koltukButton.config(fg="#E6E5D7")
        

        self.perde = tk.Label(self.film1Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=9, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film1Pencere, text="Kapat",bg="#DC170D",fg="#E6E5D7",width=10,height=2,command=self.film1Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film1Pencere, text="Koltukları Sil",fg="#E6E5D7",bg="#DC170D",height=2,command=lambda :self.koltukSil(self.film1dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film1TurLabel = tk.Label(self.film1Pencere, text=f"Tür: {self.film1tur}",fg="#E6E5D7",bg="#DC170D",height=2)
        self.film1TurLabel.grid(row=1, column=15, columnspan=2, padx=50)

 
        self.film1Pencere.grab_set()
        self.film1Pencere.focus_set()

    def film2(self):
        self.koltukNumaraları2 = []
        self.film2Pencere = tk.Toplevel(self.pencere)
        self.film2Pencere.configure(bg="#181717")
        self.film2Pencere.title(f"{self.film2dbAdi}")
        self.film2Pencere.geometry("750x700")
        self.film2Pencere.resizable(False, False)
        self.filmIkiKoltuk = ['A','B','C','D']
        for i,koltukIsım in enumerate(self.filmIkiKoltuk):
            for j in range(1,9):
                self.koltukButton = tk.Button(self.film2Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film2Pencere,self.koltukNumaraları2))
                self.koltukButton.grid(row=i, column=j,  pady=5)
        self.perde = tk.Label(self.film2Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=5, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film2Pencere, text="Kapat",bg="#DC170D",width=10,height=2,command=self.film2Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film2Pencere, text="Koltukları Sil",bg="#DC170D",width=10,height=2,command=lambda :self.koltukSil(self.film2dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film2TurLabel = tk.Label(self.film2Pencere, text=f"Tür: {self.film2tur}",bg="#DC170D",fg="white",height=2)
        self.film2TurLabel.grid(row=1, column=15, columnspan=2, padx=50)
 
        self.film2Pencere.grab_set()
        self.film2Pencere.focus_set()

    def film3(self):
        self.koltukNumaraları3 = []
        self.film3Pencere = tk.Toplevel(self.pencere)
        self.film3Pencere.configure(bg="#181717")
        self.film3Pencere.title(f"{self.film3dbAdi}")
        self.film3Pencere.geometry("750x700")
        self.film3Pencere.resizable(False, False)
        self.filmUcKoltuk = ['A','B','C','D']
        for i,koltukIsım in enumerate(self.filmUcKoltuk):
            for j in range(1,11):
                self.koltukButton = tk.Button(self.film3Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film3Pencere,self.koltukNumaraları3))
                self.koltukButton.grid(row=i, column=j,  pady=5)
        self.perde = tk.Label(self.film3Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=5, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film3Pencere, text="Kapat",bg="#DC170D",width=10,height=2,command=self.film3Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film3Pencere, text="Koltukları Sil",bg="#DC170D",width=10,height=2,command=lambda :self.koltukSil(self.film3dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film3TurLabel = tk.Label(self.film3Pencere, text=f"Tür: {self.film3tur}",bg="#DC170D",fg="white",height=2)
        self.film3TurLabel.grid(row=1, column=15, columnspan=2, padx=50)

        self.film3Pencere.grab_set()
        self.film3Pencere.focus_set()

    def film4(self):
        self.koltukNumaraları4 = []
        self.film4Pencere = tk.Toplevel(self.pencere)
        self.film4Pencere.configure(bg="#181717")
        self.film4Pencere.title(f"{self.film4dbAdi}")
        self.film4Pencere.geometry("750x700")
        self.film4Pencere.resizable(False, False)
        self.filmDortKoltuk = ['A','B','C','D']
        for i,koltukIsım in enumerate(self.filmDortKoltuk):
            for j in range(1,11):
                self.koltukButton = tk.Button(self.film4Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film4Pencere,self.koltukNumaraları4))
                self.koltukButton.grid(row=i, column=j,  pady=5)

        self.perde = tk.Label(self.film4Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=5, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film4Pencere, text="Kapat",bg="#DC170D",width=10,height=2,command=self.film4Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film4Pencere, text="Koltukları Sil",bg="#DC170D",width=10,height=2,command=lambda :self.koltukSil(self.film4dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film4TurLabel = tk.Label(self.film4Pencere, text=f"Tür: {self.film4tur}",bg="#DC170D",fg="white",height=2)
        self.film4TurLabel.grid(row=1, column=15, columnspan=2, padx=50)

        self.film4Pencere.grab_set()
        self.film4Pencere.focus_set()

    def film5(self):
        self.koltukNumaraları5 = []
        self.film5Pencere = tk.Toplevel(self.pencere)
        self.film5Pencere.configure(bg="#181717")
        self.film5Pencere.title(f"{self.film5dbAdi}")
        self.film5Pencere.geometry("750x700")
        self.film5Pencere.resizable(False, False)
        self.filmBesKoltuk = ['A','B','C','D','E']
        for i,koltukIsım in enumerate(self.filmBesKoltuk):
            for j in range(1,11):
                self.koltukButton = tk.Button(self.film5Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film5Pencere,self.koltukNumaraları5))
                self.koltukButton.grid(row=i, column=j,  pady=5)
        self.perde = tk.Label(self.film5Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=5, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film5Pencere, text="Kapat",bg="#DC170D",width=10,height=2,command=self.film5Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film5Pencere, text="Koltukları Sil",bg="#DC170D",width=10,height=2,command=lambda :self.koltukSil(self.film5dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film5TurLabel = tk.Label(self.film5Pencere, text=f"Tür: {self.film5tur}",bg="#DC170D",fg="white",height=2)
        self.film5TurLabel.grid(row=1, column=15, columnspan=2, padx=50)

        self.film5Pencere.grab_set()
        self.film5Pencere.focus_set()

    def film6(self):
        self.koltukNumaraları6 = []
        self.film6Pencere = tk.Toplevel(self.pencere)
        self.film6Pencere.configure(bg="#181717")
        self.film6Pencere.title(f"{self.film6dbAdi}")
        self.film6Pencere.geometry("750x700")
        self.film6Pencere.resizable(False, False)
        self.filmAltiKoltuk = ['A','B','C','D','E']
        for i,koltukIsım in enumerate(self.filmAltiKoltuk):
            for j in range(1,11):
                self.koltukButton = tk.Button(self.film6Pencere, text=f"{koltukIsım} {j}",bg="#DC170D",width=5,height=2,command=lambda selftext=f"{koltukIsım}{j}":self.koltuksecmebutonlari(selftext,self.film6Pencere,self.koltukNumaraları6))
                self.koltukButton.grid(row=i, column=j, pady=5)
        self.perde = tk.Label(self.film6Pencere, text="PERDE",bg="white",fg="#181717",width=60,height=2)
        self.perde.grid(row=5, column=0, columnspan=11, pady=10)
        # kapatma butonu
        self.kapatmaButon = tk.Button(self.film6Pencere, text="Kapat",bg="#DC170D",width=10,height=2,command=self.film6Pencere.destroy)
        self.kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        self.koltuklariSilmeButon = tk.Button(self.film6Pencere, text="Koltukları Sil",bg="#DC170D",width=10,height=2,command=lambda :self.koltukSil(self.film6dbAdi))
        self.koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        self.film6TurLabel = tk.Label(self.film6Pencere, text=f"Tür: {self.film6tur}",bg="#DC170D",fg="white",height=2)
        self.film6TurLabel.grid(row=1, column=15, columnspan=2, padx=50)
        self.film6Pencere.grab_set()
        self.film6Pencere.focus_set()
        
        
    def koltuksecmebutonlari(self,butonİsim,hangiPencere,koltuklar):
        self.secilenKoltukEtiket = tk.Label(hangiPencere, text="Seçilen Koltuklar:",font="Arial,20,'bold','underline'",bg="#DC170D",fg="white",width=23,height=2)
        self.secilenKoltukEtiket.place(x=500,y=250)
        self.secilmisKoltuk = tk.Label(hangiPencere, text="",bg="#DC170D",fg="white",width=30,height=2)
        self.secilmisKoltuk.place(x=500,y=300)
        # self.secilmisKoltuk.config(text="Seçilen: "+self.koltukNumaraları)
        if butonİsim in koltuklar:
            koltuklar.remove(butonİsim)
            self.secilmisKoltuk.config(bg="#DC170D")
            self.secilmisKoltuk.config(text=", ".join(koltuklar))
            self.secilmisKoltuk.config(fg="#E6E5D7")
        else:

            koltuklar.append(butonİsim)
            self.secilmisKoltuk.config(text=", ".join(koltuklar))
            self.secilmisKoltuk.config(bg="#DC170D")
            self.secilmisKoltuk.config(fg="#E6E5D7")
        self.butonSeçildi1 = tk.Button(hangiPencere, text="Seçimi Tamamla",bg="#DC170D",fg="white",width=20,height=2,command=lambda:self.seçimiTamamla(hangiPencere,koltuklar))
        self.butonSeçildi1.place(x=500,y=350)
        self.koltukYazdir = tk.Label(hangiPencere, text="Seçilen Koltuklar:",font="Arial,20,'bold','underline'",bg="#181717",fg="#E6E5D7",width=23,height=2)
        self.koltukYazdir.place(x=500,y=250)
        salonAdi = hangiPencere.title()

    def seçimiTamamla(self,hangiPencere,koltuklar):
        # veri tabanına seçilen koltukları kaydetme
        salonAdi = hangiPencere.title()
        self.db.connect()
        self.db.salonKoltukEkle(salonAdi,koltuklar)
        self.db.disconnect()

    def afisler(self):
        # film resimlerini çekme
        self.film1 = tk.PhotoImage(file="film1.jpg")
        self.film2 = tk.PhotoImage(file="film2.jpg")
        self.film3 = tk.PhotoImage(file="film3.jpg")
        self.film4 = tk.PhotoImage(file="film4.jpg")
        self.film5 = tk.PhotoImage(file="film5.jpg")
        self.film6 = tk.PhotoImage(file="film6.jpg")
        self.film1Afis = tk.Label(self.pencere, image=self.film1)
        self.film1Afis.place(x=20,y=20)
        self.film2Afis = tk.Label(self.pencere, image=self.film2)
        self.film2Afis.place(x=20,y=200)
        self.film3Afis = tk.Label(self.pencere, image=self.film3)
        self.film3Afis.place(x=20,y=380)
        self.film4Afis = tk.Label(self.pencere, image=self.film4)
        self.film4Afis.place(x=20,y=560)
        self.film5Afis = tk.Label(self.pencere, image=self.film5)
        self.film5Afis.place(x=400,y=20)
        self.film6Afis = tk.Label(self.pencere, image=self.film6)
        self.film6Afis.place(x=400,y=200)

    def _menu(self,pencere):
        self.menu = tk.Menu(pencere)
        pencere.config(menu=self.menu)
        self.filmMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Hakkında", menu=self.filmMenu)
        self.filmMenu.add_command(label="Tanıtım",command=self.tanıtım)
        self.filmMenu.add_separator()
        self.filmMenu.add_command(label="Çıkış",command=pencere.destroy)

    def tanıtım(self):
        self.tanıtımPencere = tk.Toplevel(self.pencere)
        self.tanıtımPencere.title("Tanıtım")
        self.tanıtımPencere.geometry("600x600")
        self.tanıtımPencere.configure(background="#181717")
        self.tanıtımPencere.resizable(False,False)
        self.tanıtımPencere.grab_set()
        self.tanıtımPencere.focus_set()
        self.tanıtımPencere.transient(self.pencere)
        self.tanıtımPencere.protocol("WM_DELETE_WINDOW", self.tanıtımPencere.destroy)
        icerikText = tk.Text(self.tanıtımPencere, width=50, height=30)
        icerikText.pack()
        icerikText.insert(tk.END, "Bu programda mssql veritabanı kullanılarak sinema otomasyonu yapılmıştır.\n")
        icerikText.insert(tk.END, "Hamza ORTATEPE\n")
        icerikText.insert(tk.END, "No: 90210000172\n")
        icerikText.insert(tk.END, "Veritabanı Final Ödevi")
        icerikText.config(state=tk.DISABLED)
        icerikText.config(bg="#ffffff",fg="#353535")
        self.tanıtımPencere.mainloop()

        
sinema = Sinema()