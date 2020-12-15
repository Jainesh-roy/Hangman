import random
import string
from words import word_list

def get_words():
    random_word = random.choice(word_list)

    return random_word.upper()

def hangman():
    word = get_words()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0 :
        print('\nyou have ', lives, 'Lives left! You have used these letter', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print('Letter is not in word')
        
        elif user_letter in used_letters:
            print('\nYou Have already used that Character. Please retry')
        
        else:
            print('\ninvalid charecter. Please Try again!')

    if lives == 0:
        print(f'Sorry You lost! The word was {word}')
    else:
        print('You guessed the word ', word, '!!')

    
if __name__ == "__main__":
    hangman()