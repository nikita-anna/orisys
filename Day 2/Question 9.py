import re
#9.Extracting numbers
text=input("Enter a text: ")
pattern="(\d+)"
print("Extracting numbers:")
print(re.findall(pattern,text))