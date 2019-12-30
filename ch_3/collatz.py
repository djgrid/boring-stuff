# From Chapter 3 of Automate the Boring Stuff.

def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3 * number + 1

print("Enter an integer")
userint = int(input())

result = collatz(userint)
print(result)

while result != 1:
	result = collatz(result)
	print(result)

