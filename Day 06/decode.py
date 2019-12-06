#!/usr/bin/python

ciphertext = ""

with open("input.html") as f:
    data = f.read().strip()
    for c in [",","."," ","\n"]:
        data = data.replace(c, "")
    while len(data) > 0:
        i = data.find("<em>")
        if i == -1: # end
            ciphertext += (5 - (len(ciphertext) % 5)) * "0"
            break
        elif i == 0:
            j = data.find("</em>")
            ciphertext += (j - 4) * "1"
            data = data[j+5:]
        else:
            ciphertext += i * "0"
            data = data[i:]

chunks = []
chunks_decoded = []

for i in range(0, len(ciphertext), 5):
    chunk = ciphertext[i:i+5]
    num = int(chunk, 2)
    chunks.append(num)
    if num < 26:
        chunks_decoded.append(chr(num + ord('A')))
    else:
        chunks_decoded.append("?")

print("".join(chunks_decoded))
