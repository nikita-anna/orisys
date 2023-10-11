#Question 1
dictionary={}
n=int(input("Enter the number of words in the dictionary: "))
for i in range(n):
    word=input("Enter a word: ")
    meaning=input("Enter the meaning: ")
    dictionary[word]=meaning
    ch=True
while ch:
    wrd=input("Enter the word whose meaning is to be searched: ")
    for i in dictionary:
        if i==wrd:
            print("The meaning of",wrd,"is found as",dictionary[i])
    ch=int(input("Do you want to search the meaning of another word? Enter 1 for yes and 0 for no: "))
    if ch==1:
         ch=True
    else:
         ch=False

#Question 2
def mul_table(num):
    for i in range(1,11):
        print(f"{i}*{num}=",num*i)
        
mul_table(3)

#Question 3
def find():
    str_name=input("Enter a string: ")
    vowel_count=0
    consonant_count=0
    vowels="aeiouAEIOU"
    for i in str_name:
        if i in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
    print("Number of vowels =",vowel_count)
    print("Number of constants =",consonant_count)
            
find()

#Question 4
class calculator():
    def add(self,num1, num2):
        return num1+num2
    def sub(self,num1, num2):
        return(num1-num2)
    def mul(self,num1, num2):
        return(num1*num2)
    def div(self,num1, num2):
        return(num1/num2)
    def exp(self,num1, num2):
        return(num1**num2)
    
def main():
    cal=calculator()
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    while(True):
        print("Menu: 1-Addition,2-Subtraction,3-Multiplication,4-Division,5-Exponent,6-Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            result=cal.add(a, b)
            print("Sum is",result)
        elif ch==2:
            result=cal.sub(a, b)
            print("Difference is",result)
        elif ch==3:
            result=cal.mul(a, b)
            print("Product is",result)
        elif ch==4:
            result=cal.div(a, b)
            print("Quotient is",result)
        elif ch==5:
            result=cal.exp(a, b)
            print("Exponent is",result)
        elif ch==6:
            print("Exited")
            break
    
main()



    
    
