import random
def end():
	print('Congratulations, you won!')
	exit()
print('Welcome to guess the number game! You will have 1% chance to win in every trial and you can try 20 times. Lets Start')
print('\n\tGuess the number from 1 to 100' )
guess = None
o = 20
while o > 0:
	n = random.randint(1, 100)
	guess = int(input(f'\t[{o}] Your try: '))
	if guess > n:
		print(f'\n\t=> High. \n\tThe number was {n}\n')
	elif guess == n:
		print(n)
		end()
	else:
		print(f'\n\t=> LOW \n\tThe number was {n}\n')
	o -= 1
	
print('\nYou have reached maximum trial. Better luck next time')