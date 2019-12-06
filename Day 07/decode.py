#!/usr/bin/python
#$ ffmpeg -i 3DULK2N7DcpXFg8qGo9Z9qEQqvaEDpUCBB1v.mp4 -vf fps=10 frames/frame%04d.jpg -hide_banner


from PIL import Image
import os.path

def brightness(pix):
    return ((pix[0] + pix[1] + pix[2]) / 3) / 255

bytes = []

i = 1
while True:
    path = "frames/frame%04d.jpg" % i
    if not os.path.isfile(path):
        break

    img = Image.open(path);
    pix = img.load()

    pos = [(343,177), (418,180), (551,166), (626,185),
           (717,169), (788,164), (878,162), (959,165)]

    byte = ""
    for p in pos:
        if brightness(pix[p]) > 0.6:
            byte += "1"
        else:
            byte += "0"

    bytes.append(byte)
    i = i + 1

print("".join(chr(int(x, 2)) for x in bytes))
