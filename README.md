# Hangman

This is a Python script that implements a simple game where the player tries to guess a randomly selected car brand name. The script uses basic input/output and randomization functions.

# Description

The game starts by importing the necessary modules: random and sys. The random module is used to select random car brands from a pre-defined list, while the sys module allows exiting the game.

A list of car brands is described, including a variety of popular models. The script randomly selects a car brand from this list and converts it to lowercase letters for comparison with non-absurd lowercase letters.

The script initializes variables to monitor the progress of the game. The word_split list is used to store the individual characters of the selected car brand. The list of characters maintains a well thought out character. A string variable is used to indicate the current status of the evaluated word, with dashes representing unknown characters. The turns variable controls the number of guesses left.

The main game begins, allowing the player to enter their guesses until they win or finish again. At each iteration of the loop, the script prompts the player to enter a letter and displays the current status of the word and the number of turns remaining.

If the inserted characters are not in the word_split list, the guess is invalid. The script notifies the player and reduces the remaining turns. When the turn reaches zero, the player loses, revealing the correct name of the car before exiting the script.

If the inserted characters are in the word_split list, the guess is correct. The script notifies the player and adds the letter to the letter list. If the length of the combined characters is the same as the length of the word_split list, the player has guessed all the characters.
