#!/usr/bin/python

a = 567195096 + 392339568
v1 = -1427785453 - 951416472
v2 = -1094137130 // 2
v3 = 867218979 * 2
dword_4020B0 = 413388101 + 1404925466
v4 = -1472883113 - 1187586292
v5 = 526158877 * 4

variables = [a, v1, v2, v3, dword_4020B0, v4, v5]

output = ""
for x in variables:
    x = x & 0xFFFFFFFF
    h = hex(x)[2:]
    if len(h) % 2 != 0:
        h = "0" + h

    output += "".join([chr(int(h[i:i+2], 16)) for i in range(0, len(h), 2)])[::-1]

print(output)
