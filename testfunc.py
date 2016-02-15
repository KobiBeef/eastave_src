import random
import string

def rand_key(size):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(size)])

x = rand_key(16)

print (x)