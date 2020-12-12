#Step 5

import random
import hangman_words, hangman_art 

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You already selected the letter {guess}")
  else:
    if guess not in chosen_word:
        lives -= 1
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if the game is ended.
  if "_" not in display:
    end_of_game = True
    print("You win.")
  elif lives == 0:
    end_of_game = True
    print(f"You lose.\nThe word was {chosen_word}")
  print(hangman_art.stages[lives])