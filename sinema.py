import tkinter as tk
from tkinter import messagebox
import db as db
import dbSetup as dbSetup

class Sinema():
    def __init__(self):
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
        self.db.connect()
        # Retrieve film data and store in lists
        self.filmAdlari = [self.db.filmAdi(i) for i in range(1,7)]
        self.filmKonulari = [self.db.filmKonu(i) for i in range(1,7)]
        self.filmTurleri = [self.db.turCek(filmAdi) for filmAdi in self.filmAdlari]
        self.db.disconnect()

    def koltukSil(self, filmAd):
        try:
            self.db.connect()
            self.db.koltuklariSil(filmAd)
            self.db.disconnect()
            messagebox.showinfo("Bilgi", "Bütün Koltuklar Silindi")
        except:
            messagebox.showerror("Hata", "Bir Hata Oluştu")

    def anaPencere(self):
        self.pencere = tk.Tk()
        self.pencere.title("Sinema")
        self.pencere.geometry("750x700")
        self.pencere.configure(background="#181717")
        self.pencere.resizable(False, False)
        self._menu(self.pencere)

        self.filmButonResimleri = [tk.PhotoImage(file=f"{i}.png") for i in range(1,7)]
        positions = [(100,0), (300,0), (500,0), (100,350), (300,350), (500,350)]
        for i in range(6):
            x, y = positions[i]
            filmButon = tk.Button(self.pencere, image=self.filmButonResimleri[i], width=160, height=300, foreground="#181717",bg="#F3F9D2", command=lambda i=i: self.film(i))
            filmButon.place(x=x, y=y)
            filmBaslik = tk.Label(self.pencere, text=self.filmAdlari[i], font=("Arial",12,"bold"), height=2, background="#282927", foreground="white", width=16)
            filmBaslik.place(x=x, y=y+270)
            filmDetayButon = tk.Button(self.pencere, text="Detay", background="#282927", foreground="#BDC4A7", width=5, height=2, command=lambda i=i: self.filmDetay(i))
            filmDetayButon.place(x=x, y=y+3)

    def filmDetay(self, index):
        detayPencere = tk.Toplevel(self.pencere)
        detayPencere.title(f"{self.filmAdlari[index]} Konusu")
        detayLabel = tk.Label(detayPencere, text=self.filmKonulari[index], font=("Arial",10,"bold"), background="#181717", foreground="white")
        detayLabel.pack()
        detayPencere.grab_set()
        detayPencere.focus_set()

    def film(self, index):
        koltukNumaralari = []
        filmPencere = tk.Toplevel(self.pencere)
        filmPencere.configure(bg="#181717")
        filmPencere.title(self.filmAdlari[index])
        filmPencere.geometry("750x700")
        filmPencere.resizable(False, False)

        # Define seat rows based on the film
        seat_rows = {
            0: ['A','B','C','D','E','F','G','H'],
            1: ['A','B','C','D'],
            2: ['A','B','C','D'],
            3: ['A','B','C','D'],
            4: ['A','B','C','D','E'],
            5: ['A','B','C','D','E']
        }
        rows = seat_rows.get(index, ['A','B','C','D'])

        for i, row in enumerate(rows):
            for j in range(1,11):
                koltukButton = tk.Button(filmPencere, text=f"{row} {j}", bg="#DC170D", width=5, height=2,
                    command=lambda btn_text=f"{row}{j}": self.koltuksecmebutonlari(btn_text, filmPencere, koltukNumaralari))
                koltukButton.grid(row=i, column=j, pady=5)
        perde = tk.Label(filmPencere, text="PERDE", bg="white", fg="#181717", width=60, height=2)
        perde.grid(row=len(rows)+1, column=0, columnspan=11, pady=10)

        kapatmaButon = tk.Button(filmPencere, text="Kapat", bg="#DC170D", fg="#E6E5D7", width=10, height=2, command=filmPencere.destroy)
        kapatmaButon.grid(row=10, column=0, columnspan=5, pady=10)
        koltuklariSilmeButon = tk.Button(filmPencere, text="Koltukları Sil", bg="#DC170D", fg="#E6E5D7", width=10, height=2, command=lambda: self.koltukSil(self.filmAdlari[index]))
        koltuklariSilmeButon.grid(row=10, column=5, columnspan=6, pady=10)

        turLabel = tk.Label(filmPencere, text=f"Tür: {self.filmTurleri[index]}", bg="#DC170D", fg="white", height=2)
        turLabel.grid(row=1, column=15, columnspan=2, padx=50)

        filmPencere.grab_set()
        filmPencere.focus_set()

    def koltuksecmebutonlari(self, butonIsim, hangiPencere, koltuklar):
        secilenKoltukEtiket = tk.Label(hangiPencere, text="Seçilen Koltuklar:", font=("Arial", 20, 'bold', 'underline'), bg="#DC170D", fg="white", width=23, height=2)
        secilenKoltukEtiket.place(x=500, y=250)
        secilmisKoltuk = tk.Label(hangiPencere, text="", bg="#DC170D", fg="#E6E5D7", width=30, height=2)
        secilmisKoltuk.place(x=500, y=300)

        if butonIsim in koltuklar:
            koltuklar.remove(butonIsim)
        else:
            koltuklar.append(butonIsim)
        secilmisKoltuk.config(text=", ".join(koltuklar))

        butonSecildi = tk.Button(hangiPencere, text="Seçimi Tamamla", bg="#DC170D", fg="white", width=20, height=2, command=lambda: self.secimiTamamla(hangiPencere, koltuklar))
        butonSecildi.place(x=500, y=350)

    def secimiTamamla(self, hangiPencere, koltuklar):
        salonAdi = hangiPencere.title()
        self.db.connect()
        self.db.salonKoltukEkle(salonAdi, koltuklar)
        self.db.disconnect()

    def _menu(self, pencere):
        menu = tk.Menu(pencere)
        pencere.config(menu=menu)
        filmMenu = tk.Menu(menu)
        menu.add_cascade(label="Hakkında", menu=filmMenu)
        filmMenu.add_command(label="Tanıtım", command=self.tanitim)
        filmMenu.add_separator()
        filmMenu.add_command(label="Çıkış", command=pencere.destroy)

    def tanitim(self):
        tanitimPencere = tk.Toplevel(self.pencere)
        tanitimPencere.title("Tanıtım")
        tanitimPencere.geometry("600x600")
        tanitimPencere.configure(background="#181717")
        tanitimPencere.resizable(False, False)
        tanitimPencere.grab_set()
        tanitimPencere.focus_set()
        icerikText = tk.Text(tanitimPencere, width=50, height=30)
        icerikText.pack()
        icerikText.insert(tk.END, "Bu programda mssql veritabanı kullanılarak sinema otomasyonu yapılmıştır.\nHamza ORTATEPE\n")
        icerikText.config(state=tk.DISABLED, bg="#ffffff", fg="#353535")

sinema = Sinema()