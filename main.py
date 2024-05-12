import random
#random is the libary we use for generating random words

name = input('What is your name?')
# asking the user to enter their name

print("Good luck!", name)

words = ["'rainbow', 'computer', 'programming', 'python', 'science', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'amazing' "]
# the random function will chose one random word from the list of words
word = random.choice(words)

print("Guess the charadters of each word")
guesses = ""
turns = 4

while turns > 0:
  failed = 0  #the number of times the user fails

for char in word:
  if char  in guesses:
     print(char, end="")
  else:
     print("_")
     failed += 1
if failed == 0:
   print("You Win")
   print("The word is:",word)

print("")
guess = input("guess a character")
guesses += guess

if guess not in word:
   turns = -1
   print("Wrong") 
   print("You have", +turns,"more guesses")

if turns == 0:
   print("you lose")





