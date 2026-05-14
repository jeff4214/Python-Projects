from unittest import result

password = input("input your password: ")

result = {}

if len(password) >= 8 :
    result["Length"] = True
else :
    result["Length"] = False

digit = False
for i in password :
    if i.isdigit() :
        digit = True

result["Digit"] = digit

upper = False
for i in password :
    if i.isupper() :
        upper = True

result["Upper-case"] = upper

if all(result.values()) :
    print("Password is Strong")
else :
    print("Password is weak")