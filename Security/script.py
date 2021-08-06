import sys
import hashlib
data = sys.argv[1].encode()
salt = "Km5d5ivMy8iexuHcZrsD".encode()
key = hashlib.pbkdf2_hmac('sha512', data, salt, 200000)
print(key.hex())
