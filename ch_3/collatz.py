# From Chapter 3 of Automate the Boring Stuff.
#
# This program implements the Collatz sequence. 
#

# The book wanted me to print from the function but that 
# did not sit well with me so instead I just return the
# value and print it in the main program.
#
# If my knowledge wasn't so rusty I could probably make this
# a recursive function and just call it once from within main.
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

# Using exception handling for input validation seems
# kinda clunky but I can't think of another way to do it
# 
# There is probably a better way to do this.
userint = " "
while not isinstance(userint, int):
    print("Enter an integer")
    try:
        userint = int(input())
    except ValueError:
        print("No, an integer. Want to try again?")


result = collatz(userint)
print(result)

while result != 1:
    result = collatz(result)
    print(result)

