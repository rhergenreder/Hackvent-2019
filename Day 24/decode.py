BUFFER = list(bytes.fromhex("09BC313A681AAB7247867EE64A1D6F042E74500D78063E"))

with open("rom.bin", "rb") as f:
    BUFFER2 = list(f.read(len(BUFFER)))

print("".join(chr(BUFFER[i] ^ BUFFER2[i]) for i in range(len(BUFFER))))
