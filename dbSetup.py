import pypyodbc

class dbSetup:
    def __init__(self):
        self.server = 'LENOVO\\SQLEXPRESS'  # veritabanı sunucusunun adı
        self.database = 'master'  # önce master veritabanına bağlanıp yeni veritabanı oluşturacağız
        self.username = 'sa'  # veritabanı kullanıcı adı
        self.password = '123'  # veritabanı parolası
        self.conn = None
        self.cursor = None

    def connect(self):
        # Veritabanına bağlan
        self.conn = pypyodbc.connect("DRIVER={SQL Server};" +
                                     f" Server={self.server};User={self.username};Password={self.password};Database={self.database};")
        self.cursor = self.conn.cursor()

    def create_database(self):
        # sinemaDB veritabanını oluştur
        self.cursor.execute("IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'sinemaDB')"
                            " BEGIN CREATE DATABASE sinemaDB END")
        print("Veritabanı oluşturuldu")
        self.conn.commit()

    def create_tables(self):
        # sinemaDB veritabanına geç
        self.cursor.execute("USE sinemaDB")

        # Filmler tablosunu oluştur
        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='filmler' and xtype='U')
        CREATE TABLE filmler (
            filmlerId INT PRIMARY KEY IDENTITY(1,1),
            adi NVARCHAR(100) NOT NULL,
            konu NVARCHAR(MAX) NOT NULL,
            tur NVARCHAR(50) NOT NULL
        )""")

        # Sinema tablosunu oluştur
        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='sinema' and xtype='U')
        CREATE TABLE sinema (
            sinemaId INT PRIMARY KEY IDENTITY(1,1),
            filmId INT FOREIGN KEY REFERENCES filmler(filmlerId),
            salonlar NVARCHAR(100) NOT NULL
        )""")

        # Salonlar tablosunu oluştur
        self.cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='salonlar' and xtype='U')
        CREATE TABLE salonlar (
            salonId INT PRIMARY KEY IDENTITY(1,1),
            salonlar NVARCHAR(100) NOT NULL,
            koltuklar NVARCHAR(10) NOT NULL,
            filmId INT FOREIGN KEY REFERENCES filmler(filmlerId)
        )""")

        print("Tablolar oluşturuldu")
        self.conn.commit()

    def disconnect(self):
        # Veritabanı bağlantısını kapat
        self.conn.close()

