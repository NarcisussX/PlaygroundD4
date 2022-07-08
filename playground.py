# View this in thonny using the debug tool to watch the steps.

def change_name(player_name):
    message = "Your name is " + player_name
    print(message)
    new_name = input("What name do you want? ")
    print("Name now set to " + new_name)
    return new_name

# this defines the function "change name" but does not call it
# this means you need to call this function. The line below is used to 
# call this function. Once this function is called it will run the
# above definition.

change_name("Your name here")

def add(num1,num2):
    result = num1 + num2
    return result

# above is the definition for the function called "add"
# YOU MUST RETURN RESULT or the function will evaluate 
# but will not make a variable for the result.

result2 = add(1, 2)
print(result2)

# OR you can do

print(add(35,100))

# this is because we DEFINED (def) the add function, so we can call it in a print statement
# without defining a new variable for the result
# it can get even larger by putting 2 add functions inside an add function.

print(add(add(1,2), add(3,4)))

# Above is a bit confusing with nested parentheses, however it is one line.
# The 4 lines below give the same result,

sum1 = add(1,2)
sum2 = add(3,4)
result = add(sum1, sum2)
print(result)


# This should take a number as it's argument and return a boolean (true false) if it is even
def is_even(number):            # this is going to define the function "is_even"
    remainder =  number % 2     # defines the variable remainder to be input % 2
    if remainder == 0:          # % 2 gives the remainder of dividing by 2
        return True
    else:
        return False

print(is_even(2))               # this will check if 2 and 3 are even numbers by calling the function 
print(is_even(3))               # and printing the function result (true/false)

# You can also call functions in if statements based on input, and output a print statement.

if is_even(int(input("Type a number:\n"))):  # this is confusing parenthesis. See below for explanation.
    print("The number is even")
else:
    print("the number is not even")

# input always returns a string, we need to define the input as an integer (int)
# by putting an input() module inside an int() module. You can expand this out
# by defining an input variable and then converting that variable to an integer.

number = (input("type a number here:\n"))
number = int(number)

# This is much easier to read and works like the above.

if is_even(number):  
    print("The number is even")
else:
    print("the number is not even")

# this is a new function definition for adding many numbers using loops called add_many

def add_many(*numbers):  # STAR NUMBERS ALLOW YOU TO HAVE UNLIMITED POSITIONAL ARGUMENTS (1,2,3,4,infinity)
    sum = 0
    for many_numbers in numbers:
        sum += many_numbers         # += is the same as (many_number = many_number + 1)
    return sum

print(add_many(1,2,3,4,5,6,7,8))

# THIS IS A STAR KWARGS EXAMPLE
# just like *numbers is any arbitrary numbers, *kwargs is any arbitrary number of keyword arguments
# potional arguments = add(1, 2) ........ keyword arguments = add(num1=30, num2=10)

def example(**kwargs):
    print(type(kwargs))

example(name="hello", fruit="apple", movie="star wars")