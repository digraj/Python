import numpy as np
import PIL
from scipy import misc
from pprint import pprint as pp
import base64
import zlib

class Payload:
    def __init__(self, img=None, compressionLevel=-1, content=None):

        if compressionLevel < -1 or compressionLevel > 9:
            raise ValueError("compressionLevel should be between -1 and 9")
        if img is None and content is None:
            raise ValueError("both image and content cannot be none")
        if not isinstance(img, np.ndarray) and img is not None:
            raise TypeError("img should be of type np.ndarray")
        if not isinstance(content, np.ndarray) and content is not None:
            raise TypeError("content should be of type np.ndarray")

        self.dict64Encode = self.dictDefEnc()
        self.dict64Decode = self.dictDefDec()
        self.redArray = []
        self.blueArray = []
        self.greenArray = []
        if content is None:
            self.img = img
            (self.row, self.col, self.ndim) = self.img.shape

            temp = img.ravel()
            self.redArray = list(temp[0:len(temp):3])
            self.greenArray = list(temp[1:len(temp):3])
            self.blueArray = list(temp[2:len(temp):3])
            self.img = (self.redArray + self.greenArray + self.blueArray)
            self.img = np.array(self.img)

            self.content = []
            self.compressOption = False
            self.compressed = (self.img)
            if compressionLevel >= 0 and compressionLevel <= 9:
                self.compressed = list(zlib.compress(self.img, compressionLevel))
                self.compressOption = True
            self.color = 1
            self.encodedAscii = base64.b64encode(str.encode(self.XMLCreator(), encoding='utf-8'))
            if self.encodedAscii[-2] == 61:
                characters = list(str(self.encodedAscii))[2:-3]
            elif self.encodedAscii[-1] == 61:
                characters = list(str(self.encodedAscii))[2:-2]
            else:
                characters = list(str(self.encodedAscii))[2:-1]
            self.content = np.vectorize(self.dict64Encode.get)(characters)
            self.content = np.array(self.content)
            self.content = np.uint8(self.content)

        elif img is None:
            self.content = np.array(content)
            reconstructedContent = ("".join(np.vectorize(self.dict64Decode.get)(self.content)))
            decodedLen = (len(reconstructedContent))
            if (decodedLen * 3) % 4 == 1:
                reconstructedContent += "="
            elif (decodedLen * 3) % 4 == 2:
                reconstructedContent += "=="
            decoded = str(base64.b64decode(reconstructedContent), 'utf-8')
            decoded = decoded.split(">")
            decoded = decoded[1:-1]
            numbers = decoded[1]
            numbers = numbers.split("<")
            numbers = numbers[0].split(",")
            numbers = list(map(int, numbers))
            decoded = decoded[0].split("\"")
            if decoded[5] == "True":
                self.compressOption = True
            else:
                self.compressOption = False
            color = decoded[1]
            size = decoded[3].split(",")
            self.row = int(size[0])
            self.col = int(size[1])
            if color == "Color":
                self.color = color
            else:
                self.color = "Gray"
            self.decompressed = numbers

            if self.compressOption:
                self.decompressed = list(zlib.decompress(bytearray(numbers)))
            lenOfDecompressed = int(len(self.decompressed) / 3)
            self.redArray = self.decompressed[:lenOfDecompressed]
            self.greenArray = self.decompressed[lenOfDecompressed:lenOfDecompressed * 2]
            self.blueArray = self.decompressed[lenOfDecompressed * 2:lenOfDecompressed * 3]

            rearrangedArray = np.array([self.redArray, self.greenArray, self.blueArray])
            rearrangedArray = np.transpose(rearrangedArray)
            rearrangedArray = np.reshape(rearrangedArray, (self.row, self.col, 3))

            self.img = rearrangedArray
            self.img = np.uint8(self.img)

    def dictDefDec(self):
        encodedDict = self.dictDefEnc()
        return dict(map(reversed, encodedDict.items()))

    def dictDefEnc(self):
        dict64Encode = {'A': 0, 'B': 1, 'C': 2, 'D': 3,	'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,'J': 9,'K': 10,
                        'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30,
                        'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40,
                        'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50,
                        'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60,
                        '9': 61, '+': 62, '/': 63}

        return dict64Encode

    def XMLCreator(self):
        row = str(self.row)
        col = str(self.col)
        newCompressed = list(map(str, self.compressed))
        compressedData = ",".join(newCompressed)

        imgType = "Gray"
        if self.color:
            imgType = "Color"

        xmlStr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        xmlStr += "<payload type=\""+imgType+"\" size=\""+row+","+col+"\" compressed=\""+str(self.compressOption)+"\">"
        xmlStr += compressedData + "</payload>"
        return xmlStr

class Carrier:
    def __init__(self, img):
        if not isinstance(img, np.ndarray):
            raise TypeError("img should be of type np.ndarray")
        self.img = img
        (self.row, self.col, self.ndim) = self.img.shape

    def payloadExists(self):
        self.dict64Decode = self.dictDefDec()
        toPrint = ((self.img[:1] & 0b11) << [0, 2, 4])
        toPrint = np.bitwise_or.reduce(toPrint, axis=2)
        dataArray = toPrint.flatten()
        reconstructedContent = np.vectorize(self.dict64Decode.get)(dataArray)
        decoded = (base64.b64decode(reconstructedContent[:8]))
        if decoded == b'<?xml ':
            return True
        return False

    def clean(self):
        toPrint = (self.img & 0b11)
        np.random.shuffle(toPrint)
        return (self.img & ~toPrint)

    def embedPayload(self, payload, override=False):
        if type(payload) != Payload:
            raise TypeError
        if (self.col * self.row) < len(payload.content):
            raise ValueError
        if self.payloadExists() and not override:
            raise Exception

        fullImg = self.img.flatten()
        tempImg = fullImg[:len(payload.content) * 3]
        remImg = fullImg[len(payload.content) * 3:]
        redArray = payload.content & 3
        greenArray = (payload.content >> 2) & 3
        blueArray = (payload.content >> 4) & 3

        rearrangedArray = np.array([redArray, greenArray, blueArray])
        rearrangedArray = rearrangedArray.transpose()
        rearrangedArray = rearrangedArray.flatten()

        tempImg = tempImg & 252
        tempImg = tempImg | rearrangedArray
        finalImg = np.concatenate([tempImg, remImg])
        finalImg = np.reshape(finalImg, (self.row, self.col ,3))
        return finalImg

    def extractPayload(self):
        self.dict64Encode = self.dictDefEnc()
        self.dict64Decode = self.dictDefDec()
        toPrint = ((self.img & 0b11) << [0, 2, 4])
        toPrint = np.bitwise_or.reduce(toPrint, axis=2)
        dataArray = toPrint.flatten()
        reconstructedContent = (np.vectorize(self.dict64Decode.get)(dataArray))
        decoded = (base64.b64decode(reconstructedContent))
        decoded = decoded.split(b'</payload>')
        decoded = (str(decoded[0] + b'</payload>'))

        self.encodedAscii = base64.b64encode(str.encode(decoded[4:-1], encoding='utf-8'))
        if self.encodedAscii[-2] == 61:
            characters = list(str(self.encodedAscii))[2:-3]
        elif self.encodedAscii[-1] == 61:
            characters = list(str(self.encodedAscii))[2:-2]
        else:
            characters = list(str(self.encodedAscii))[2:-1]
        content = np.vectorize(self.dict64Encode.get)(characters)
        content = np.array(content)
        content = np.uint8(content)

        return Payload(img=None, content=content)

    def dictDefDec(self):
        encodedDict = self.dictDefEnc()
        return dict(map(reversed, encodedDict.items()))

    def dictDefEnc(self):
        dict64Encode = {'A': 0, 'B': 1, 'C': 2, 'D': 3,	'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,'J': 9,'K': 10,
                        'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                        'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30,
                        'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40,
                        'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50,
                        'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60,
                        '9': 61, '+': 62, '/': 63}

        return dict64Encode

if __name__ == "__main__":
    # img = misc.imread('carrier1.png')
    # Carrier(img)
    #
    img = np.arange(30).reshape(2, 5, 3)
    # cLevel = 3
    encoded = [15, 3, 61, 56, 27, 22, 48, 32, 29, 38, 21, 50, 28, 54, 37, 47, 27, 35, 52, 34, 12, 18, 56, 48, 8, 34, 1,
                37, 27, 38, 13, 47, 25, 6, 37, 46, 25, 51, 52, 34, 21, 21, 17, 6, 11, 19, 32, 34, 15, 51, 56, 60, 28, 6,
                5, 57, 27, 6, 61, 33, 25, 2, 1, 52, 30, 23, 1, 37, 15, 18, 9, 3, 27, 54, 49, 47, 28, 34, 8, 32, 28, 54,
                37, 58, 25, 19, 52, 34, 12, 34, 48, 53, 8, 34, 1, 35, 27, 54, 53, 48, 28, 38, 21, 51, 28, 54, 21, 36, 15,
                18, 9, 20, 28, 39, 21, 37, 8, 35, 56, 49, 12, 35, 0, 44, 14, 19, 16, 44, 14, 19, 36, 44, 14, 19, 24, 44,
                12, 19, 0, 50, 11, 3, 8, 50, 13, 50, 48, 50, 12, 35, 32, 44, 12, 35, 8, 53, 11, 3, 8, 51, 11, 3, 4, 56,
                11, 3, 4, 52, 14, 18, 48, 49, 13, 3, 16, 44, 12, 19, 0, 50, 11, 3, 4, 48, 12, 2, 48, 57, 13, 50, 48, 50,
                12, 51, 4, 44, 12, 35, 8, 54, 11, 3, 8, 49, 11, 3, 4, 54, 11, 3, 8, 50, 11, 3, 4, 52, 13, 50, 48, 49, 13,
                3, 32, 44, 14, 19, 28, 44, 14, 19, 32, 44, 12, 35, 8, 57, 11, 3, 8, 50, 13, 2, 48, 50, 12, 51, 0, 44, 12,
                19, 36, 44, 12, 35, 0, 44, 12, 19, 28, 44, 12, 19, 20, 49, 11, 3, 4, 52, 13, 34, 48, 53, 11, 3, 0, 44,
                12, 35, 8, 44, 12, 19, 36, 56, 11, 3, 4, 44, 12, 19, 32, 48, 15, 2, 61, 48, 24, 23, 37, 44, 27, 54, 5,
                36, 15, 32]
    ctn = np.array(encoded)
    # # print(img)
    toHideImg = Payload(img, 5, None)
    # toHideContent = Payload(img=None, compressionLevel=5, content=ctn)
    #
    # # print(toHideImg.img)
    # # print(toHideImg.content)
    #
    img = np.arange(30, 60).reshape(2, 5, 3)
    # # print()
    # # print(img)
    img = misc.imread('result1_9.png')
    shapeOfYou = Carrier(img)
    payload = shapeOfYou.extractPayload()
    shapeOfYou.embedPayload(payload=payload, override=True)
    # print(type(shapeOfYou))
    # # shapeOfYou.embedPayload(toHideImg, False)