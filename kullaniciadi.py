from PyQt6.QtWidgets import *

class loginEkrani(QMainWindow):
    def kontrol(self):
        print("Tiklandi")
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanici adi:"))
        ka = QLineEdit()
        icerik.addWidget(ka)
        icerik.addWidget(QLabel("Şifre:"))
        sf = QLineEdit()
        icerik.addWidget(sf)
        buton1 = QPushButton("Giriş yap")   
        icerik.addWidget(buton1) 
        icerik.addWidget(QLabel("Sonuc: "))
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        buton1.clicked.connect(self.kontrol)

uygulama = QApplication([])
pencere = loginEkrani()
pencere.show()
uygulama.exec()
