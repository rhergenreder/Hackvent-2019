#!/usr/bin/python

def xor(str1, str2):
    l = min(len(str1), len(str2))
    return "".join(chr(int(str1[i]) ^ int(str2[i])) for i in range(l))

str3 = b"6klzic<=bPBtdvff'y\x7fFI~on//N" # expected input encrypted
str1 = b"AAAAAAAAAAAAAAAAAAAAAAAAAAA"    # input
str2 = b"GFIHKJMLONQPSRUTWVYX[Z]\_^a"    # input encrypted
key = xor(str1, str2).encode("UTF-8")    # key
print("HV19{%s}" % xor(str3, key))
