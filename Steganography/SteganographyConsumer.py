import sys
from PySide.QtCore import *
from PySide.QtGui import *
from SteganographyGUI import *
from scipy.misc import imread
from scipy.misc import imsave
from pprint import pprint as pp
from Steganography import Payload as pl
from Steganography import Carrier as car

class Consumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.embedCompression = -1
        self.payloadOverride = False
        self.CarrierGiven = False
        self.PayloadGiven = False
        self.saveValue = -1

        # Carrier Received for Embedding
        self.viewCarrier1 = DisplayImg(self.grpCarrier1, self)
        self.viewCarrier1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier1.setObjectName("Carrier 1")
        self.viewCarrier1.img.connect(self.CarrierEmbed)

        # Payload Received for Embedding
        self.viewPayload1 = DisplayImg(self.grpPayload1, self)
        self.viewPayload1.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewPayload1.setObjectName("Payload 1")
        self.viewPayload1.img.connect(self.PayloadEmbed)

        # Carrier Received for Extracting
        self.viewCarrier2 = DisplayImg(self.grpCarrier2, self)
        self.viewCarrier2.setGeometry(QtCore.QRect(10, 40, 361, 281))
        self.viewCarrier2.setObjectName("Carrier 2")
        self.viewCarrier2.img.connect(self.CarrierExtract)

        # Apply Compression
        self.chkApplyCompression.stateChanged.connect(self.compressionApply)

        # Compression Change
        self.slideCompression.valueChanged.connect(self.embedCompressionChange)

        # Override Payload
        self.chkOverride.stateChanged.connect(self.override)

        # Save image
        self.btnSave.clicked.connect(self.saveImg)

        # Extract Payload
        self.btnExtract.clicked.connect(self.extractPayload)

        # Clean Image
        self.btnClean.clicked.connect(self.cleanCarrier)

    def cleanCarrier(self):
        self.carrierCleaned = self.extractCarrier.clean()
        imsave(self.viewCarrier2.path, self.carrierCleaned)
        self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
        self.btnClean.setEnabled(False)
        self.btnExtract.setEnabled(False)
        self.displayCarrier()

    def displayCarrier(self):
        scn = QtGui.QGraphicsScene()
        pixMap = QtGui.QPixmap(self.viewCarrier2.path)
        item = scn.addPixmap(pixMap)
        self.viewCarrier2.setScene(scn)
        self.viewCarrier2.fitInView(item, Qt.KeepAspectRatio)
        self.show()

    def extractPayload(self):
        self.payloadExtracted = self.extractCarrier.extractPayload()
        imsave('temp.png', self.payloadExtracted.img)
        self.displayImage()

    def displayImage(self):
        scn = QtGui.QGraphicsScene()
        pixMap = QtGui.QPixmap('temp.png')
        item = scn.addPixmap(pixMap)
        self.viewPayload2.setScene(scn)
        self.viewPayload2.fitInView(item, Qt.KeepAspectRatio)
        self.show()

    def saveFileEnable(self):
        self.btnSave.setEnabled(False)
        if self.PayloadGiven and self.CarrierGiven:
            if int(len(self.embedCarrier.img) * len(self.embedCarrier.img[0])) >= int(len(self.embedPayload.content)):
                if self.embedCarrier.payloadExists():
                    if self.payloadOverride:
                        self.btnSave.setEnabled(True)
                else:
                    self.btnSave.setEnabled(True)

    def embedSave(self, path):
        finalImg = self.embedCarrier.embedPayload(self.embedPayload, override=self.payloadOverride)
        imsave(path, finalImg)

    def saveImg(self):
        filePath, _ = QFileDialog.getSaveFileName(self, caption='Save image file to...')

        self.embedSave(filePath)

    def override(self):
        if self.chkOverride.isChecked():
            self.payloadOverride = True
            print("Override Enabled")
        else:
            self.payloadOverride = False
            print("Override Disabled")
        self.saveFileEnable()

    def embedCompressionChange(self):
        print("Compression level changed")
        self.embedCompression = self.slideCompression.value()
        print("Compression = ", self.embedCompression, '\n')
        self.txtCompression.setText(str(self.embedCompression))
        self.PayloadEmbed()

    def compressionApply(self):
        if self.chkApplyCompression.isChecked():
            print("User wants Compression")
            self.enableSlider()
            if self.saveValue == -1:
                self.embedCompression = 0
            else:
                self.embedCompression = self.saveValue
        else:
            print("User does not want Compression")
            self.embedCompression = -1
            self.disableSlider()
        self.PayloadEmbed()
        print("Compression = ", self.embedCompression)

    def CarrierEmbed(self):
        print("Carrier Received for Embedding\n")
        self.embedCarrier = car(self.viewCarrier1.imgArr)
        print(type(self.embedCarrier))
        self.txtCarrierSize.setText(str(len(self.embedCarrier.img) * len(self.embedCarrier.img[0])))
        if self.embedCarrier.payloadExists():
            self.payloadOverride = False
            self.lblPayloadFound.setText(">>>>Payload Found<<<<")
            self.chkOverride.setEnabled(True)
        else:
            self.lblPayloadFound.setText("")
        self.CarrierGiven = True
        if self.CarrierGiven and self.PayloadGiven:
            self.saveFileEnable()

    def PayloadEmbed(self):
        print("Payload Received for Embedding\n")
        self.embedPayload = pl(img=self.viewPayload1.imgArr, compressionLevel=self.embedCompression)
        print(type(self.embedPayload))
        self.txtPayloadSize.setText(str(len(self.embedPayload.content)))
        self.PayloadGiven = True
        if self.CarrierGiven and self.PayloadGiven:
            self.saveFileEnable()

    def CarrierExtract(self):
        print("Carrier Received for Extracting\n")
        self.extractCarrier = car(self.viewCarrier2.imgArr)
        print(type(self.extractCarrier))
        if not self.extractCarrier.payloadExists():
            self.lblCarrierEmpty.setText(">>>>Carrier Empty<<<<")
        else:
            self.lblCarrierEmpty.setText("")
            self.btnClean.setEnabled(True)
            self.btnExtract.setEnabled(True)
        self.carrier2received = True

    def enableSlider(self):
        self.slideCompression.setEnabled(True)
        self.lblLevel.setEnabled(True)
        self.txtCompression.setEnabled(True)

    def disableSlider(self):
        self.saveValue = self.slideCompression.value()
        self.slideCompression.setEnabled(False)
        self.lblLevel.setEnabled(False)
        self.txtCompression.setEnabled(False)

class DisplayImg(QGraphicsView):
    img = Signal(str)
    def __init__(self, title, parent):
        super(DisplayImg, self).__init__(title, parent)

        self.setAcceptDrops(True)
        self.imgArr = None
        self.path = None

    def checkExtension(self, extension):
        if extension == '.png':
            return True
        return False

    def dragEnterEvent(self, event):
        event.accept()

    def dragMoveEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        self.path = event.mimeData().imageData()
        self.path = str(event.mimeData().urls())
        self.path = self.path.split(":")
        self.path = self.path[1][2:-3]
        print(self.path[-4:])
        if self.checkExtension(self.path[-4:]):
            scn = QtGui.QGraphicsScene()
            pixMap = QtGui.QPixmap(self.path)
            item = scn.addPixmap(pixMap)
            self.setScene(scn)
            self.fitInView(item, Qt.KeepAspectRatio)
            self.show()
            event.accept()
            self.imgArr = imread(self.path)
            self.img.emit('signal')

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()
    currentForm.show()
    currentApp.exec_()