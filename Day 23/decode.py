#!/usr/bin/python

import subprocess
import re
import datetime
import hashlib
import base64
import requests
import random
import time

# charset = [chr(ord("0")+x) for x in range(10)] + \
#           [chr(ord("A")+x) for x in range(26)] + \
#           [chr(ord("a")+x) for x in range(26)]


# import BeautifulSoup4 as bs4

# def encode(sec):
#     md5 = hashlib.md5(sec.encode("UTF-8")).digest()
#     b64 = base64.b64encode(md5).decode("UTF-8")
#     return b64
#
# password = "cswpWQfUu8fL"
# timestamp = "2019-12-23 11:43"
#
# d = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M" )
# seconds = int(d.timestamp())
# print()
#
# charset = "abcdefghijkmpqrstuvwxyzABCDEFGHJKLMPQRSTUVWXYZ23456789";
# random.seed(0)
# print("".join([random.choice(charset) for i in range(12)])) # [charset[random.randint(0,len(charset) - 1)] for x in range(12)]))

# for s in range(60):
#     for j in range(1000):
#         random.seed(seconds + s)
#         rand_indices = [random.randint(0,len(charset) - 1) for i in range(12)]
#         rand_str = "".join([charset[i] for i in rand_indices])
#         if rand_str == password or rand_str.lower() == password.lower():
#             print(rand_str, rand_indices)

# for i in range(60):
#     for j in range(100):
#         b64 = encode("%d.%02d" % (seconds + i, j))
#         if password in b64:
#             print(b64)

# def getPassword():
#     pass

# charset = []
# pattern = re.compile("<strong>(.*)<\/strong>")
# #
# for i in range(100):
#     res = requests.post("http://whale.hacking-lab.com:23023/archive.php", data={"req[]":"blindball", "username":"test"})
#     if res.status_code == 200:
#         pw = pattern.search(res.text).group(1)
#         print(time.time(), pw)
#         for x in pw:
#             if x not in charset:
#                 charset.append(x)
#
# print("".join(sorted(charset)))

min = 0
max = 2**32 - 1
num_processes = 4
steps = (max-min+1) // num_processes
start = min

procs = []

for i in range(num_processes):
    end = start + steps
    args = ["php", "decode.php", str(i+1), str(start), str(end)]
    print("Starting subprocess:", " ".join(args))
    procs.append(subprocess.Popen(args))
    start = end + 1
    break
    # break

for proc in procs:
    proc.wait()
