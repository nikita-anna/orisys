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



    
    
    
    
