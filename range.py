#print every number in the list
my_list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

length_of_mylist1 = len(my_list1)

for number in range(length_of_mylist1):
  print(number)

#print every index and letter in a list
my_list2 = ['a','b','c','d','e','f'',g','h','i','j','k','l','m','n','o','p','q','r','s','t','y','z']

for index in range(len(my_list2)):
  print(index, my_list2[index])
  
#print every index and letter in a word
word = "ScienceFiction"

for index in range(len(word)):
  print(index, word[index])
  
#print evey letter of word taken fron end to beginning
my_word = input("What is your word? ")

for index in range(len(my_word)  -1,-1,-1):
  print(my_word[index])