#4.Remove html tags
import re
html_tag=input("Enter a html tag: ")
print("Removing all html tags:")
print(re.sub(r'<.*?>','',html_tag))