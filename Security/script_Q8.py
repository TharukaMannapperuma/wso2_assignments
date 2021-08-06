import sys
import hashlib
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

data = sys.argv[1].encode()
salt = get_random_string(20).encode()
key = hashlib.sha512(salt+data)
print(key.hexdigest())
