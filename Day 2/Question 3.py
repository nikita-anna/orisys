#3.Match dates
import re
date=input("Enter a date: ")
pattern="[01]\d\/[0-3]\d\/[12]\d{3}"
if re.findall(pattern,date)!=[]:
    print(date,"is valid")
else:
    print("Invalid date")
    
