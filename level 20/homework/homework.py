#1
inp = input("enter string: ")
if (str(inp))[::-1] == str(inp):
    print(True)
else:
    print(False)

#2
user_input1 = int(input("please enter number: "))
user_input2 = int(input("please enter number: "))
user_input3 = int(input("please enter number: "))
user_input4 = int(input("please enter number: "))
user_input5 = int(input("please enter number: "))


list = [user_input1, user_input2, user_input3, user_input4, user_input5]
b = [1,2,3,4,5]
list1 = []

for num in range(len(list)):
    if list[num] == b[num]:
        list1.append(num)
print(list1)



#3. 
input1 = input("please enter a word u silly goose: ")
input2 = input("please enter a word u silly goose: ")
input3 = input("please enter a word u silly goose: ")
input4 = input("please enter a word u silly goose: ")
input5 = input("please enter a word u silly goose: ")
list5 = [input1, input2, input3, input4, input5]
list6 = [input1[0] + input2[0] + input3[0] + input4[0] + input5[0]]

print(list5)
print(list6)

#4. 
list_1 = []
list_2 = []

for int in range(10, 21):
    list_1.append(int)
print(list_1)

for int1 in range(30, 51):
    if int1 % 5 == 0:
        list_2.append(int1)
print(list_2)