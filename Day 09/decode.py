#!/usr/bin/python

from PIL import Image
import numpy

im = Image.open("qr.png")
input = im.load()

# QR Version 4
size = 33
pixelSize = im.size[0] // size

# rule 30
codes = {
    "111": 0,
    "110": 0,
    "101": 0,
    "100": 1,
    "011": 1,
    "010": 1,
    "001": 1,
    "000": 0
}


def translatePos(pos):
    x = pos[0] * pixelSize + pixelSize // 2
    y = pos[1] * pixelSize + pixelSize // 2
    return (x, y)

def fillPixel(pos, bit, pix):
    color = (0,0,0) if bit == 1 else (255,255,255)
    for x in range(5):
        for y in range(5):
            pix[pos[0]*pixelSize+x,pos[1]*pixelSize+y] = color

def readPos(pos, pix, size):
    if pos[0] < 0 or pos[0] >= size[0] or pos[1] < 0 or pos[1] >= size[1]:
        return 0

    translated = translatePos(pos)
    return 0 if pix[translated] == 255 else 1

def readBufPos(pos, buf):
    x = pos[0]
    y = pos[1]

    if x < 0 or x >= buf.shape[0] or y < 0 or y >= buf.shape[1]:
        return 0

    return int(buf[x,y])

def rule30decode(x, y, buf):
    bits = "".join([str(readBufPos(p, buf)) for p in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]])
    return codes[bits]


# Used to save rule30 pyramid for visualization
def bufToImage(buf, filename, pixelSize = 5):
    imgSize = (buf.shape[0] * pixelSize, buf.shape[1] * pixelSize)
    outImage = Image.new('RGB', imgSize, 255)
    outPixel = outImage.load()
    for x in range(0, buf.shape[0]):
        for y in range(0, buf.shape[1]):
            color = (0,0,0) if int(buf[x,y]) == 1 else (255,255,255)
            for i in range(pixelSize):
                for j in range(pixelSize):
                    outPixel[x*pixelSize+i,y*pixelSize+j] = color

    outImage.save(filename)

# 33 + 33/2 + 2
bufSize = 51
buf = numpy.zeros(shape=(bufSize,bufSize))
buf[buf.shape[0]//2,0] = 1

for y in range(1,buf.shape[1]):
    for x in range(0,buf.shape[0]):
        buf[x,y] = rule30decode(x,y,buf)

# bufToImage(buf, "rule30.png")

offsetX = (bufSize-33)//2-1
offsetY = 0

outImage = Image.new('RGB', im.size, 255)
outPix = outImage.load()
for x in range(size):
    for y in range(size):
        bit1 = readPos((x,y), input, im.size)
        bit2 = int(buf[offsetX+x,offsetY+y])
        bit = bit1 ^ bit2
        fillPixel((x,y), bit, outPix)
outImage.save("decoded.png")
