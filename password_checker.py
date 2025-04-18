password = input("Give me a new password: ")

result = {}
digit = False
upper = False

if len(password) > 8:
    result["length"] = True
    print("Your password is long enough")
else:
    result["length"] = False
    print("Your password is not long enough")

for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        upper = True

result["digit"] = digit
result["upper"] = upper

if all(result.values()):
    print("You have a strong password!")
else:
    print("You have a weak password!")
