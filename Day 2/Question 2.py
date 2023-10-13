#2.Extract domain from url
import re
url=input("Enter a url: ")
pattern="[https]+\:\/{2}w{3}\.\w*\.[com]+\/?\w*"
if re.findall(pattern,url)!=[]:
    print("Extracting domain from url")
    pattern2="[https]+\:\/{2}w{3}\.(\w*\.[com]+)\/\w*"
    print(re.findall(pattern2,url))
else:
    print("Invalid url")