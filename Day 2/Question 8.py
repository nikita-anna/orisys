#8.Find all urls
import re
text=input("Enter a text: ")
pattern="(http[s]?:\/{2}www.[a-zA-Z0-9$-_@&+]*.[com]+)"
print("Extracting urls:")
print(re.findall(pattern,text))