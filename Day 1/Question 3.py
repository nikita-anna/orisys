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
