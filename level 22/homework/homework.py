#1
word = input("Please enter a word: ")
if len(word) > 3:
    print(word[0:3])
elif len(word) <= 3:
    print(word[0])

#2


list1 = []
for i in range(10, 21):
    list1.append(i)
print(list1[::2])

#3. 

name = input("please enter a word: ")
print(name[::-1])

c = ['$', '£', '€', '¥']
print(c[-3:-1])
    