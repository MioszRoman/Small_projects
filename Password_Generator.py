import string
import random

def generate_password(pass_len: int) -> str:
    return ''.join([
        random.choice(string.printable)
        for _ in range(pass_len)
    ])

