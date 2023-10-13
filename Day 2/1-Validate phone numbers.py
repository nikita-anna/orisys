#1.Phone number verification
import re
phno=input("Enter your phone number: ")
pattern="^\(\d{3}\)-\d{3}-\d{4}$"
if re.findall(pattern,phno)!=[]:
    print(phno,"is valid")
else:
    print(phno,"is invalid")
    print("Checking for country code")
    pattern2="\+\d\d\d?\(\d{3}\)-\d{3}-\d{4}"
    if re.findall(pattern2,phno)!=[]:
        print(phno,"is valid")
    else:
        print("Invalid phone number")
