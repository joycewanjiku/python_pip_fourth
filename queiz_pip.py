
# Write a function that takes an unknown number of arguments and returns their sum.
def unknown_num(numbers):
    sum=0
    if sum in numbers:
        return numbers

# Write a function that takes two arguments, the first being a string and the second
#  being an unknown number of integers. The function should return a new string where
# the integers have been added to the original string.

# Write a function that takes an unknown number of keyword arguments and returns a 
# dictionary where the keys are the argument names and the values are the argument values.
def local(caller_locals,args*):
    filtered={}
    for i in args:
        filtered[i]=caller_locals[i]
        return filtered

# Write a function that takes a function and an unknown number of arguments, and 
# returns the result of calling the function with the arguments.
def fun(a,b):
    print(a,b)
    args=(54,12)
    fun(*args)



# Write a function that takes a list of integers and an unknown number of keyword
#  arguments. The function should return a new list where each integer in 
# the original list has been multiplied by the value of the corresponding
#  keyword argument.
def number_digits(numbers):
    count=0
    while numbers !=0:
        numbers//=10
        return count
    
    print(number_digits(3467))



# Write a function that takes a list of integers and an unknown number of
#  additional integers as arguments. The function should return the index of 
# the first occurrence of the sum of the list and the additional integers
def subtract(*nums):
    first_number=nums[0]
    for num in nums[1:]:
        first_number-=num 
        return first_number

print(subtract(32,56,8,9,7))
print(subtract(12,7))
        


# Write a function that takes an unknown number of keyword arguments, each with a 
# string value. The function should concatenate all the strings and return the
#  resulting string.
def concat(list_args):
    res=""
    for w in list_args:
        result +=w
        return result

print(concat(["a","b","c","d"]))
