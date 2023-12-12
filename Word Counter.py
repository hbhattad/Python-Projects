# Write a program to calculate the number of words in a Sentence

s = input("Enter the sentence:")
mylist = s.split(" ")
n = len(mylist)
print("No. of words : ",n)

#One Liner!!!
print("No. of words : ",len(input("Enter the sentence: ").split(" ")))
