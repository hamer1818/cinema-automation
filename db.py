import pypyodbc
from tkinter import messagebox

class dbClass:
    def __init__(self):
        self.server = 'LENOVO\\SQLEXPRESS'  # veritabanı sunucusunun adı
        self.database = 'sinemaDB'  # veritabanının adı
        self.username = 'sa'  # veritabanı kullanıcı adı
        self.password = '123'  # veritabanı parolası

    def connect(self):
        # Veritabanına bağlan
        self.conn = pypyodbc.connect("DRIVER={SQL Server};" + f" Server={self.server};User={self.username};Password={self.password};Database={self.database};")
        self.cursor = self.conn.cursor()

    def filmAdi(self, filmId):
        # Film adını verilen film ID'sine göre getir
        self.sorgu = self.cursor.execute(f"select f.adi from filmler f join sinema s on f.filmlerId = s.filmId where f.filmlerId = {filmId}")
        self.sorgu = self.cursor.fetchall()
        for sütun in self.sorgu:
            return sütun[0]
        return self.sorgu

    def filmKonu(self, filmId):
        # Film konusunu verilen film ID'sine göre getir
        self.sorgu = self.cursor.execute(f"select f.konu from filmler f join sinema s on f.filmlerId = s.filmId where f.filmlerId = {filmId}")
        self.sorgu = self.cursor.fetchall()
        for sütun in self.sorgu:
            self.sorgu = sütun[0]
        self.sorgu = str(self.sorgu)
        plot_lines = self.sorgu.split('.')
        return plot_lines[0] + '.' + '\n' + plot_lines[1] + '.'

    def salonKoltukEkle(self, salonIsim, koltuklar):
        koltuks = [None]
        self.boşkoltuk = [None]
        self.dolukoltuk = []
        for koltuk in koltuklar:
            koltuks.append(koltuk)
            dolumu = self.cursor.execute(f"select * from salonlar where salonlar = '{salonIsim}' and koltuklar = '{koltuk}'")
            dolumu = self.cursor.fetchall()
            if not dolumu:
                self.cursor.execute(f"insert into salonlar (salonlar,koltuklar) values ('{salonIsim}','{koltuk}')")
                print(self.cursor.execute(f"select * from salonlar where salonlar = '{salonIsim}' and koltuklar = '{koltuk}'"))
                print("Salon ve koltuk eklendi")
                self.dolukoltuk.append(f"{salonIsim} ve {koltuk} eklendi")
            else:
                print(f"{koltuk} dolu")
                self.boşkoltuk.append(f"{koltuk} dolu")
        if self.dolukoltuk != []:
            messagebox.showinfo("Dolu koltuk uyarı!", f"{self.dolukoltuk}")
        if self.boşkoltuk != []:
            messagebox.showinfo("Boş koltuk uyarı!", f"{self.boşkoltuk}")
        print(koltuks)
        self.conn.commit()

    def koltuklariSil(self, filmAd):
        # Verilen film adına ait koltukları sil
        self.cursor.execute(f"DELETE FROM salonlar WHERE salonlar = '{filmAd}'")
        self.conn.commit()

    def disconnect(self):
        # Veritabanı bağlantısını kapat
        self.conn.close()

    def turCek(self, filmAd):
        # Verilen film adına ait türü getir
        self.sorgu = self.cursor.execute(f"select tur from filmler where adi = '{filmAd}'")
        self.sorgu = self.cursor.fetchall()
        for sütun in self.sorgu:
            self.turler = sütun[0]
        return self.turler

    def filmKoltukCek(self, filmAd):
        # Verilen film adına ait koltukları getir
        self.sorgu = self.cursor.execute(f"select koltuklar from salonlar where salonlar = '{filmAd}'")
        self.sorgu = self.cursor.fetchall()
        for sütun in self.sorgu:
            self.turler.append(sütun[0])
        return self.turler
