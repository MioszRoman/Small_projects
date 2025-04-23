import string
import random
import os


if not os.path.exists("../password.txt"):
    with open("../password.txt", "w") as passwords_file:
        pass


def generate_password(pass_len: int) -> str:
    """This function will generate a password"""
    return ''.join([
        random.choice(string.printable)
        for _ in range(int(pass_len))
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


def main(number):
    return generate_password(number)

if __name__ == '__main__':
    what_for = input("For what do you need a password: ")
    len_of_password = input("Give me a number of amount for your password: ")
    passwords = get_password()
    password = main(len_of_password)
    full_info = f"{what_for}: {password}\n"
    passwords.append(full_info)
    print(full_info)
    write_password(passwords)

