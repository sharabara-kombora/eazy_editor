from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit, QInputDialog, QFileDialog
import os
from PIL import Image, ImageEnhance
from PyQt5.QtGui import QPixmap

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.name = None
        self.save = 'mod/'
    def loadImage(self, filename):
        self.name = filename
        image_path = os.path.join(workdir, filename)
        self.image = Image.open(image_path)
    def showImage(self, path):
        nadpis.hide()
        pixmapimage = QPixmap(path)
        w, h = nadpis.width(), nadpis.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        nadpis.setPixmap(pixmapimage)
        nadpis.show()
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
    def do_r(self):
        self.image = ImageEnhance.Contrast(self.image)
        self.image = self.image.enhance(1.5)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
    def do_z(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save, self.name)
        self.showImage(image_path)
    def saveImage(self):
        path = os.path.join(workdir, self.save)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.name)
        self.image.save(image_path)

workdir = ''
workimage = ImageProcessor()
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result
def showFilenamesList():
    chooseWorkdir()
    rasshireniya = ['.png', '.jpg', '.jpeg', '.bmp','.gif']
    files = os.listdir(workdir)
    spisok_f = filter(files, rasshireniya)
    spisok.clear()
    spisok.addItems(spisok_f)

def showChosenImage():
    if spisok.currentRow() >= 0:
        filename = spisok.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, filename)
        workimage.showImage(image_path)


app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Easy Editor')
mw.resize(800, 500)

nadpis = QLabel('Картинка')
knopka_papka = QPushButton('Папка')
kn_levo = QPushButton('Лево')
kn_pravo = QPushButton('Право')
kn_zerkalo = QPushButton('Зеркало')
kn_rezkost = QPushButton('Резкость')
kn_chb = QPushButton('Ч/Б')
spisok = QListWidget()

knopki_line = QHBoxLayout()
knopki_line.addWidget(kn_levo)
knopki_line.addWidget(kn_pravo)
knopki_line.addWidget(kn_zerkalo)
knopki_line.addWidget(kn_rezkost)
knopki_line.addWidget(kn_chb)
papka_line = QVBoxLayout()
papka_line.addWidget(knopka_papka)
papka_line.addWidget(spisok)
kartinka_line = QVBoxLayout()
kartinka_line.addWidget(nadpis)
kartinka_line.addLayout(knopki_line)
main_line = QHBoxLayout()
main_line.addLayout(papka_line, 20)
main_line.addLayout(kartinka_line, 80)
mw.setLayout(main_line)

knopka_papka.clicked.connect(showFilenamesList)
spisok.currentRowChanged.connect(showChosenImage)
kn_chb.clicked.connect(workimage.do_bw)
kn_levo.clicked.connect(workimage.do_left)
kn_pravo.clicked.connect(workimage.do_right)
kn_rezkost.clicked.connect(workimage.do_r)
kn_zerkalo.clicked.connect(workimage.do_z)

mw.show()
app.exec_()