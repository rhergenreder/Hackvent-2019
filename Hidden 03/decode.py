#!/usr/bin/python

import sys
import socket

if len(sys.argv) < 2:
    print("Invalid usage: %s <outfile>" % sys.argv[0])
    exit(1)

OUTFILE = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('whale.hacking-lab.com', 17))

data = ""

while True:
    buf = sock.recv(16)
    if buf:
        data += buf.decode("UTF-8")
    else:
        break

with open(OUTFILE, "a") as f:
    f.write(data.strip())
