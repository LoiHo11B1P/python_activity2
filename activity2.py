'''Python function called max_num()to find the maximum of three numbers.'''
def max_num(a, b, c):
    number_list = [a,b,c]
    return max(number_list)


print(max_num(3, 2, 1))

'''Python function called mult_list() to multiply all the numbers in a list.'''
import math

def mult_list(list):
    result = math.prod(list)
    return result

print(mult_list([1,2,3,4,5]))

'''function called rev_string() to reverse a string.'''
def rev_string(str):
    rev_str = str[::-1]
    return rev_str

print(rev_string('abcde'))

'''function called num_within() to check whether a number falls in a given range.'''
def num_within(num, begin, end):
    if num in range(begin, end):
        return True
    else:
        return False

print(f'4 is in range of 5 and 6: {num_within(4,5,6)}')
print(f'2 is in range of 1 and 6: {num_within(2,1,6)}')

'''function called pascal() that prints out the first n rows of Pascal's triangle.'''
def pascal(n):
    
    for i in range(n):
       
           print(11**i)

pascal(5)