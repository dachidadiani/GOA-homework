

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        
    return sum
            

def solution(string, ending):
    return string.endswith(ending)



def to_jaden_case(string):
    words = string.split()
    a = []
    for i in words:
        capitalized = i.capitalize()
        a.append(capitalized)
    sentence = ' '.join(a)

    return sentence




def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
   



def find_smallest_int(arr):
    return min(arr)
  