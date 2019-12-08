#!/usr/bin/python

import base64
import operator

strings = [
    b'SlQRUPXWVo\Vuv_n_\\ajjce',
    b'QVXSZUVY\ZYYZ[a',
    b'QOUW[VT^VY]bZ_',
    b'SPPVSSYVV\YY_\\\\]',
    b'RPQRSTUVWXYZ[\]^',
    b'QTVWRSVUXW[_Z`\\b'
]

def decodeChar(c, i = 0):
    return chr((int(c) - 30 - i) % 256)

for s in strings:
    decoded = "".join([decodeChar(s[i], i) for i in range(len(s))])
    print(decoded)
