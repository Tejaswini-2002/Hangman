import random
import sys
car_brands = ["Vauxhall","Ferrari","Jaguar","Audi","Lamborghini","Renault","Ford","Bentley","Volkswagen"]
word = random.choice(car_brands)
word = word.lower()
word_split = []
word_split[:0] = word
letters = []
string = "(" + ("-"*len (word)) + ")"
turns = 5
while turns > 0 :
  letter = input(string + " You have " + str(turns) + " guesses left, enter a letter: ")
  letter = letter.lower()
  if letter not in word_split:
     print ("Incorrect!!")
     turns -= 1
     if turns == 0:
       print("You lose! The word was " + str(word))
       sys.exit
  if letter in word_split:  #please enter the letter only once if the letter is not repeated (you will get to know whether it is repeated or not)
    print("Correct!!")
    letters.append(letter)   #if letter is repeated ,then please type it again (you will get to know whether it is repeated or not)
    if len("".join(letters)) == len(word_split):
       print("You win! The word was " + str(word))
       break
    string = ("".join([x if x == letter else "-" for x in word]))