#7.Extract hashtags
import re
post=input("Enter a social media content: ")
pattern="(#\w*)"
print("Extracting hashtags:")
print(re.findall(pattern,post))
