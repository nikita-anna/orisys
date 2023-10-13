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