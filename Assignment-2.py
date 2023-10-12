import re
    
#1.Phone number verification
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

#2.Extract domain from url
url=input("Enter a url: ")
pattern="[https]+\:\/{2}w{3}\.\w*\.[com]+\/?\w*"
if re.findall(pattern,url)!=[]:
    print("Extracting domain from url")
    pattern2="[https]+\:\/{2}w{3}\.(\w*\.[com]+)\/\w*"
    print(re.findall(pattern2,url))
else:
    print("Invalid url")
    
#3.Match dates
date=input("Enter a date: ")
pattern="[01]\d\/[0-3]\d\/[12]\d{3}"
if re.findall(pattern,date)!=[]:
    print(date,"is valid")
else:
    print("Invalid date")
    
#4.Remove html tags
html_tag=input("Enter a html tag: ")
print("Removing all html tags:")
print(re.sub(r'<.*?>','',html_tag))

#5.Valid IP Address
ip=input("Enter an IP Address: ")
pattern="[192]+\.[168]+\.\d\d?\d?\.\d\d?\d?"
if re.findall(pattern,ip)!=[]:
    print(ip,"is valid")
else:
    print("Invalid IP Address")

#6.Valid password
password=input("Enter a password: ")
pattern="^(?=.*[A-Z])(?=.*\d).{8,}$"
if re.findall(pattern,password)!=[]:
    print(password,"is valid")
else:
    print("Invalid password")

#7.Extract hashtags
post=input("Enter a social media content: ")
pattern="(#\w*)"
print("Extracting hashtags:")
print(re.findall(pattern,post))

#8.Find all urls
text=input("Enter a text: ")
pattern="(http[s]?:\/{2}www.[a-zA-Z0-9$-_@&+]*.[com]+)"
print("Extracting urls:")
print(re.findall(pattern,text))

#9.Extracting numbers
text=input("Enter a text: ")
pattern="(\d+)"
print("Extracting numbers:")
print(re.findall(pattern,text))
