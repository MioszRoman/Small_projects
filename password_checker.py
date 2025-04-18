password = input("Give me a new password: ")

result = {}
digit = False
upper = False

if len(password) > 8:
    result["length"] = True
else:
    result["length"] = False

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
