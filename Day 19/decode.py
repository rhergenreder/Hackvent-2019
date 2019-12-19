#!/usr/bin/python

import requests
import subprocess
import sys
import threading
import queue
import time
from bs4 import BeautifulSoup as bs

# get unicode list
print("Downloading full emoji unicode list…")
res = requests.get("https://unicode.org/emoji/charts/full-emoji-list.html")
if res.status_code != 200:
    print("Server returned: %d %s" % (res.status_code, res.reason))
    exit(1)

print("Parsing…")
unicodes = set()
html = bs(res.text, 'lxml')
elements = html.find_all("td", {"class": "chars"})
for e in elements:
    unicodes.add(e.text.encode("UTF-8"))

initialSize = len(unicodes)
print("Loaded %d unicodes" % initialSize)

def tryUnicode(unicode):
    process = subprocess.Popen(["./test"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(unicode)
    process.stdin.write(b'\n')
    process.stdin.flush()
    return process.stdout.read()

queue = queue.Queue()
for u in unicodes:
    queue.put(u)

def doWork():
    while not queue.empty():
        u = queue.get()
        output = tryUnicode(u)
        if not b"Program panicked" in output:
            print()
            print("Input:", u.decode("UTF-8"), "Output:", output.decode("UTF-8").replace("\n", "\\n"))

threads = []
for n in range(10):
    t = threading.Thread(target=doWork)
    t.start()
    threads.append(t)

while not queue.empty():
    sys.stdout.write("\rTrying %04d/%04d" % (initialSize - queue.qsize(), initialSize))
    sys.stdout.flush()
    time.sleep(0.5)
