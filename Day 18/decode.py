from Crypto.Cipher import Salsa20

KEY       = bytearray.fromhex("0320634661B63CAFAA76C27EEA00B59BFB2F7097214FD04CB257AC2904EFEE46")
NONCE     = bytearray.fromhex("B132D0A8E78F4511")[::-1]
ENCRYPTED = bytearray.fromhex("096CD446EBC8E04D2FDE299BE44F322863F7A37C18763554EEE4C99C3FAD15")

cipher = Salsa20.new(key=KEY, nonce=NONCE)
plaintext = cipher.decrypt(ENCRYPTED)
print(plaintext.decode("UTF-8"))
