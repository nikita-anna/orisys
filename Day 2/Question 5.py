#5.Valid IP Address
import re
ip=input("Enter an IP Address: ")
pattern="[192]+\.[168]+\.\d\d?\d?\.\d\d?\d?"
if re.findall(pattern,ip)!=[]:
    print(ip,"is valid")
else:
    print("Invalid IP Address")