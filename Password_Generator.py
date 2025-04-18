import string
import random

def generate_password(pass_len: int) -> str:
    """This function will generate a password"""
    return ''.join([
        random.choice(string.printable)
        for _ in range(pass_len)
    ])


def write_password(local_password, filepath= "password.txt"):
    """This function will write a password to a file with extension .txt"""
    with open(filepath, "w") as file:
        file.writelines(local_password)

def get_password(filepath = "password.txt"):
    """This function will read a password from a file password.txt"""
    with open(filepath, "r") as file:
        pass_local = file.readlines()
    return pass_local


