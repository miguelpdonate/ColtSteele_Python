""" Bank Robbery Exercise
I just robbed a bank with some of my friends. 
We got away with $19,867,324,678,987.99, and now we have to split it up 5 ways. 
Using the cash  variable I've already defined for you, print out the dollar amount each robber gets to keep. 
(divide cash  by 5 and print the answer out)

p.s. I haven't actually robbed a bank.  Yet."""

cash = 19867324678987.99  # DON'T CHANGE THE CASH VARIABLE

# ADD YOUR CODE BELOW:
print(cash / 5)




"""Make Some Variables!
Now that we've learned about variables and data types, let's get some practice.  Or, skip this! Totally up to you!

Define a variable named city  and set it equal to any string
Define a variable named price  and set it equal to any float
Define a variable named high_score  and set it equal to any int
Define a variable named is_having_fun  and set it to a boolean value
You do not need to print them out, but can if you want."""


# Define a variable named city and set it equal to any string

# Define a variable named price and set it equal to any float

# Define a variable named high_score and set it equal to any int

# Define a variable named is_having_fun and set it to a Boolean value
city = "New York"
price = 5.6
high_score = 7
is_having_fun = True





"""Escape Sequence Practice
Get some practice with escape sequences!  
NO need to create new variables, 
just use the existing variables we have created for you and follow the instructions. :) """


 # Set the message variable equal to any string containing a new-line escape sequence
message = "Hello \n goodbye"
 
# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
 
mountains = "/\\/\\/\\"
 
 
# Set the quotation variable to any string that contains an escaped double quotation mark
quotation = "My cat said \"meow\""





"""String Concatenation Exercise
Set the variable called greeting  to some greeting, e.g. "hello".

Set the variable called name  to some name, e.g. "Heisenberg".

Then set the variable called greet_name  so that it concatenates greeting , name , and a space " " between them."""

greeting = "Hi"
name = "Miguel"
greet_name = greeting + " " + name



"""Formatting Strings
Set the variable called first  to your first name.

Set the variable called last  to your last name.

Then set the variable called formatted  to a new string that interpolates both values (from the first and last variables) using f-strings or the .format()  method.  Make sure you follow this exact pattern for the new string that you store to the formatted variable (pay attention to capital/lowercase letters, spaces, commas, etc):

"First Name: Colt, Last Name: Steele"""

first = "Miguel"
last = "Perez"

formatted = f"First Name: {first}, Last Name: {last}"


"""Lucky Number 7
At the top of the file is some starter code that randomly picks a number between 1 and 10, and saves it to a variable called choice. 
Don't touch those lines! (please)

Your job is to write a simple conditional to check if choice  is 7.
  If choice  is 7, print out "lucky".  Otherwise, print out "unlucky"."""


# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print('lucky')
else:
    print('unlucky')



"""Number is Odd
You will be provided with a random number in a variable called num .

Use a conditional statement to check if the number is odd. If num  is odd, 
print "odd". Otherwise print "even". 

Hint: use modulus %  to figure out if the number is odd!"""


# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================



# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

if num % 2 == 1:
  print('odd')
else:
  print('even')



# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^








"""Positive or Negative Checking
In this exercise x  and y  are two random variables.  The code at the top of the file randomly assigns them (we'll learn how it works later on).  For now, just leave it alone :)

If both are positive numbers, print "both positive". 
If both are negative, print "both negative". 
Otherwise, tell us which one is positive and which one is negative, e.g. "x is positive and y is negative"
The print statements are filled in for you, just add logic. 

For the tests to pass, don't change the print statements!"""


# NO TOUCHING ======================================
from random import randint
x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING ======================================
 
# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")




"""Calling in Sick
In this exercise you will be given a few variables that will be set randomly to Boolean values (True  or False ):

actually_sick  - when you legit have the flu!

kinda_sick  - you're feeling under the weather and it's enough to treat yoself with a day off if you can spare it

hate_your_job  - work sucks, I know... 

You're also given a random number of sick_days between 0 and 10.

Finally, there is a variable called calling_in_sick  that you must set to True  or False  based on the following scenarios:

Set to True if: 

you're actually_sick  and you have sick_days  remaining

you're kinda_sick  and hate_your_job  and you have sick_days  remaining

Otherwise, set to False.

The tests check that the value of calling_in_sick  is correct based on the conditions specified above."""



# NO TOUCHING ======================================
from random import choice, randint
 
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING ======================================
 
 
calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!
 
# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean
 
if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False








"""For Loop and Range Exercise
Use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in the variable x .  

You could cheat and just figure this out using a calculator, but...that would defeat the whole point of this course.

Can I put emoji in here? Let's see...🤗 It works!!!"""


# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:

for number in range(10, 21):
    if number % 2 == 1:
        x = x + number




"""
While Loop Exercise
While loops are really hard for me to write tests for(until we learn about things like lists), so this exercise is a bit tricky to explain. :( 
Here's the main idea:

Use a while loop to generate a random number between 1 and 10 until you get the number 5. 
Every time the loop runs, increment the variable i .

Here are more detailed steps:

Generate a random number between 1 and 10 using randint(1, 10) ,
storing the result in the number variable
Write a while loop to keep regenerating a new random number between 1 and 10
while the random number is not equal to 5.
In order for my tests to work, please add 1 to i  each time through the loop. 
 My tests use this variable to check how many times your loops runs."""

from random import randint  # use randint(a, b) to generate a random number between a and b
 
number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration
 
while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10) #update number to be a new random int from 1-10



