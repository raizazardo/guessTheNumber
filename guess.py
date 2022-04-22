from art import logo
from random import randint

EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5

turns = 0

# Function to check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.

def check_answer (guess, answer, turns):
	"""Checks answers against guess. Returns the nuber of turns remaining"""
	if guess > answer: 
		print("Too high")
		return turns - 1
	elif guess < answer:
		print ("Too low")
		return turns - 1
	else: 
		print(f"You got it, the answer was {answer}")

#Function to set difficulty
def set_difficulty():
	level = input("Choose the difficulty, type 'hard' for hard or 'easy' for easy: ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS

#game function 
def game(): 

#Choosing a random number
	print(logo)
	print("Welcome to the guessing game!")
	print ("I'm thinking about a number between 1 and 100, can you guess?")
	answer = randint(1, 100)
	turns = set_difficulty()
	
	#while loop so the player can continue guessing until runs out of turns
	guess = 0
	while guess != answer:
	# Allow the player to submit a guess for a number between 1 and 100.
		print(f"You have {turns} attempts remaining to guess the number")
		guess = int(input("Make a guess: "))
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print(f"You run out of turns, the answer is {answer}")
			return
		elif guess != answer:
			print("Guess again!")

 			
game()












