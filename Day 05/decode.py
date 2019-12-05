#!/usr/bin/python3

from PIL import Image

img = Image.open("barcode.png");
pix = img.load()
width = img.size[0]

print("Image has", width, "Pixels")

smallestBar = None
barStartedAt = None
bars = []

def findBounds():
    start = None
    end = None

    for x in range(0, width):
        if pix[x,0] != (255,255,255):
            end = x
            if start is None:
                start = x

    return (start,end)

def getBars(bounds):
    start = bounds[0]
    end =  bounds[1]
    lastColor = pix[start,0]
    barStartedAt = start
    bars = []
    for x in range(start+1,end+1):
        if pix[x,0] != lastColor:
            bars.append((barStartedAt, x-1, lastColor))
            barStartedAt = x
            lastColor = pix[x,0]

    return bars

def findBarWidth(bars):
    smallest = None
    for b in bars:
        width = b[1]-b[0]+1
        if smallest is None or width < smallest:
            smallest = width
    return smallest

def getBits(bars, barWidth):
    bits = ""
    for b in bars:
        width = b[1]-b[0]+1
        numBits = width // barWidth
        if b[2] == (255,255,255):
            bits += "0" * numBits
        else:
            bits += "1" * numBits
    return bits

def getColoredBits(bars, barWidth):
    redChannel = ""
    greenChannel = ""
    blueChannel = ""
    for b in bars:
        if b[2] == (255,255,255):
            continue # skip
        else:
            width = (b[1]-b[0]+1) // barWidth
            redChannel += chr(b[2][0])
            greenChannel += chr(b[2][1])
            blueChannel += chr(b[2][2])

    return (redChannel, greenChannel, blueChannel)

bounds = findBounds()
width = bounds[1] - bounds[0] + 1
print("Barcode start x=%d end x=%d width=%d" % (bounds[0], bounds[1], width))

bars = getBars(bounds)
barWidth = findBarWidth(bars)
print("Found %d bars, smallest bar is %d pixels" % (len(bars), barWidth))

# Usual deoding results in "Not the solution", so we have to adjust our getBits method
bits = getBits(bars, barWidth)
print("Bitstring:", bits)

bitsColored = getColoredBits(bars, barWidth)
print("Bitstring", bitsColored)
