#1

def even_check(num):
    sum = 0
    for i in range(num):
        if i % 2 == 0:
            sum += i
    return sum
    
print(even_check(21))

#2
def even_odd(num):
    if num % 2 == 0:
        print("This number is even")
    elif num != 0:
            print("This number is odd")
    return(num)

even_odd(19)

#3

def easy_hard(number):
     if number % number == 1 and number % 1 == number:
          print("This number is easy")
     else:
          print("This number is hard")
          return(number)

easy_hard(100)



#4

def caps_write(lstofnames):
    capslock = [name.capitalize() for name in lstofnames]
    return capslock
print(caps_write(['lebron', 'random', 'goaisbest']))

#5


def evenOr_odd(numbers):
    for nums in numbers:
        if nums % 2 == 0:
            print(nums / 2)
        else:
            print(nums * 2)
print(evenOr_odd([1,2,3,4,5,6,7])) 