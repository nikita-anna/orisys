#6.Valid password
import re
password=input("Enter a password: ")
pattern="^(?=.*[A-Z])(?=.*\d).{8,}$"
if re.findall(pattern,password)!=[]:
    print(password,"is valid")
else:
    print("Invalid password")
