import random
number=random.randrange(0,50)
guessCheck="tester"
print("Hey, And Welcome To The Number Picker, I absolutely suck at coding and we'll see how I write codes. I made this on 4/11/2021 at 5:37 AM And I'm dead.")

while guessCheck=="tester":
	response=int(input("Please input a number between 0 and 50:"))
	try:
			val=int(response)
	except ValueError:
		print("This is not a valid integer. Please try again")
		continue
	val=int (response)
	if val<number:
		print("This is lower than actual number. Please try again.")
	elif val>number:
		print("This is higher than actual number. Please try again.")
	else:
		print("This is the correct number")
		guessCheck="correct"

print("Thank you for playing the Number Picker. We'll see how my codes improve and I just wanna try new things!")					