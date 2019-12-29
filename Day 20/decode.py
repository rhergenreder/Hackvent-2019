#!/usr/bin/python

import requests
import hashlib
import os

byte_300 = [0xCE, 0x55, 0x95, 0x4E, 0x38, 0x0C5, 0x89, 0x0A5, 0x1B, 0x6F, 0x5E, 0x25, 0x0D2, \
            0x1D, 0x2A, 0x2B, 0x5E, 0x7B, 0x39, 0x14, 0x8E, 0x0D0, 0x0F0, 0x0F8, 0x0F8, 0x0A5]

EXPECTED_HASH = "f86d4f9d2c049547bd61f942151ffb55"
INPUT_FILE = "PS4UPDATE.PUP"
BUFFER_LENGTH = len(byte_300)

def downloadFile():
    print("Downloading file…")
    res = requests.get("https://psarchive.darksoftware.xyz/505Retail.PUP")
    if res.status_code != 200:
        print("Server returned: %d %s" % (res.status_code, res.reason))
        exit(1)

    buffer = res.content
    hash = hashlib.md5(buffer).hexdigest()
    if hash != EXPECTED_HASH:
        print("Hash does not match:", hash)
        exit(1)

    with open(INPUT_FILE, "wb") as f:
        f.write(buffer)

if not os.path.isfile(INPUT_FILE):
    downloadFile()

with open(INPUT_FILE, "rb") as f:

    v29 = byte_300.copy()
    v14 = 4919;

    while True:
        f.seek(v14)
        input = bytes(f.read(BUFFER_LENGTH))
        for i in range(BUFFER_LENGTH):
            v29[i] = (v29[i] ^ input[i])

        v14 += 4919
        if v14 == 24201480: # 4919 times
            break

    print("".join(chr(x) for x in v29))
