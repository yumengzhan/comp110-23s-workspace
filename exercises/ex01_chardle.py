"""EX01 - Chardle - A cute step toward Wordle."""
__author__= "730619940"

word_entered: str= input("Enter a 5-character word: ")
if (len(word_entered)==4):
    print("Error: Word must contain 5 characters")
    exit()
if (len(word_entered)==8):
    print("Error: Word must contain 5 characters")
    exit()
your_special_character: str= input("Enter a single character: ")
if (len(your_special_character)==3):
    print("Error: Character must be a single character.")
    exit()
if (len(your_special_character)==0):
    print("Error: Character must be a single character.")
    exit()
print("Searching for "+your_special_character+" in "+  word_entered)
count: int=0


if (your_special_character==word_entered[0]):
    count =count+1
    print(your_special_character+ " found at index 0")
if (your_special_character==word_entered[1]):
    count=count+1
    print(your_special_character+ " found at index 1 ")
if (your_special_character==word_entered[2]):
    count=count+1
    print(your_special_character+ " found at index 2 ")
if (your_special_character==word_entered[3]):
    count=count+1
    print(your_special_character+ " found at index 3 ")
if (your_special_character==word_entered[4]):
    count=count+1
    print(your_special_character+ " found at index 4 ")
count=int(0)
if (word_entered[0]==your_special_character):
    count=count+1
if (word_entered[1]==your_special_character):
    count=count+1
if (word_entered[2]==your_special_character):
    count=count+1
if (word_entered[3]==your_special_character):
    count=count+1
if (word_entered[4]==your_special_character):
    count=count+1
if (count==0):
    print("No instances of "+ your_special_character+" found in "+word_entered)
if (count==1):
    print("1 instance of "+ your_special_character+" found in "+word_entered)
if (count==2):
    print("2 instance of "+ your_special_character+" found in "+word_entered)
if (count==3):
    print("3 instance of "+ your_special_character+" found in "+word_entered)
if (count==4):
    print("4 instance of "+ your_special_character+" found in "+word_entered)







