#!/usr/bin/python

import hashlib, binascii, base64
from fastecdsa import keys, curve, point
from Crypto.Cipher import AES
import queue
import threading
import time
import sys

x = 0xc58966d17da18c7f019c881e187c608fcb5010ef36fba4a199e7b382a088072f
y = 0xd91b949eaf992c464d3e0d09c45b173b121d53097a9d47c25220c0b4beb943c

PUBLIC_KEY = point.Point(x, y, curve.P256)
PASSWORD_QUEUE = queue.Queue()

def tryPassword(pw):
    privKey = hashlib.sha256(pw).digest()
    pubKey = keys.get_public_key(int.from_bytes(privKey, "big"), curve.P256)
    if pubKey != PUBLIC_KEY:
        return False

    print("Found possible password:", pw)
    salt = b'TwoHundredFiftySix'
    aesKey = hashlib.pbkdf2_hmac('sha256', pw, salt, 256*256*256)
    cipher = AES.new(aesKey, AES.MODE_ECB)
    encrypted = base64.b64decode(b"Hy97Xwv97vpwGn21finVvZj5pK/BvBjscf6vffm1po0=")

    try:
        decrypted = cipher.decrypt(encrypted)
        print(decrypted.decode('utf-8'))
        exit(0)
        return True
    except Exception as e:
        print(str(e))
        return False

def doWork():
    while not PASSWORD_QUEUE.empty():
        pw = PASSWORD_QUEUE.get()
        tryPassword(pw)


with open("/usr/share/wordlists/SecLists/Passwords/Leaked-Databases/rockyou.txt", "rb") as f:
    for pw in f.readlines():
        pw = pw.strip()
        if len(pw) == 16:
            PASSWORD_QUEUE.put(pw)

initialSize = PASSWORD_QUEUE.qsize()
print("Read %d passwords, starting threads…" % initialSize)
threads = []
for i in range(8):
    t = threading.Thread(target=doWork)
    t.start()
    threads.append(t)

while not PASSWORD_QUEUE.empty():
    sys.stdout.write("\rProgress: %04d/%04d" % (initialSize - PASSWORD_QUEUE.qsize(), initialSize))
    sys.stdout.flush()
    time.sleep(0.5)
