unk_100007F50 = [0x03, 0x20, 0x63, 0x46, 0x61, 0xB6, 0x3C, 0xAF, 0xAA, 0x76, 0xC2, 0x7E, 0xEA, 0x00, 0xB5, 0x98]
a4 = -5678246756302764783

# input = "096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15"
# print(len(input), len(unk_100007F50))

def dance_words():
    pass

def dance_block(buf, unk, const, num):
    pass

def dance(input):
    if len(input) > 0:
        v4 = -567824675630276478
        v5 = unk_100007F50
        v6 = len(input)
        v7 = input
        v8 = 0
        v9 = [0] * 64

        while True:

            if v8 == 0:
                dance_block(v9, v5, v4, 0)

            v7[v8] = ord(v7[v8]) ^ v9[0]
            v8 = v8 + 1
            if v6 == v8:
                break

        return v7

input = ["0"] * 32
output = dance(input)
print(output)
