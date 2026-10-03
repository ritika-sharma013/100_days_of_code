import random 

HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [ 'FRUITS', 'VEGETABLES', 'ANIMALS', 'COUNTRIES', 'CITIES', 'SPORTS', 'MOVIES', 'MUSIC', 'BOOKS', 'GAMES' 
        'PYTHON', 'CATCH', 'HANGMAN', 'PROGRAMMING', 'DEVELOPER', 'COMPUTER', 'KEYBOARD', 'MONITOR', 'PRINTER', 'LAPTOP'
         ]

class Hangman: 
    """
    The hangman game is basically a guessing game where 
    the player has to guess the word by suggesting letters within a 
    certain number of guesses.
    """

    def __init__(self, words_to_guess):
        self.failed_attempts = 0
        self.words_to_guess = words_to_guess
        self.game_progress = list('_' * len(words_to_guess))


    # creating a function to find indexes

    def find_indexes(self, letter):
        """
        This function finds the indexes of the letter in the word to guess.
        :param letter: The letter to find the indexes of.
        :return: A list of indexes where the letter is found in the word to guess.
        """
        indexes = []
        for index, char in enumerate(self.words_to_guess):
            if char == letter:
                indexes.append(index)
        return indexes

    def is_invalid_letter(self, input_letter):
        """
        This function checks if the input letter is invalid.
        :param input_letter: The letter to check.
        :return: True if the letter is invalid, False otherwise.
        """
        if len(input_letter) != 1 or (not input_letter.isalpha() and not input_letter.isdigit()):
            return True
        return False

    def print_game_progress(self):

        """ 
        This function prints the current progress of the game, 
        including the hangman figure and the guessed letters.
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(''.join(self.game_progress))

    def update_progress(self, letter, indexes):

        """
        This function updates the game progress with the guessed letters
        :parameter letter: Letter to be added to the game progress
        :parameter indexes: list of indexes where the letter is found in the word to guess

        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\n Please enter a letter:')
        return user_input

    def play(self):

         """
        Method to play the game, it prompts the user for a letter and plays
        the game until the user guesses the word or lose his attempts
        """
         while self.failed_attempts < len(HANGMAN):
            self.print_game_progress()
            user_input = self.get_user_input()

            # Validate the user input
            if self.is_invalid_letter(user_input):
                print('¡The input is not a letter!')
                continue
            # Check if the letter is not already guessed
            if user_input in self.game_progress:
                print('You already have guessed that letter')
                continue

            if user_input in self.words_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                # If there is no letter to find in the word
                if self.game_progress.count('_') == 0:
                    print('\n¡Yay! You win!')
                    print('The word is: {0}'.format(self.words_to_guess))
                    quit()
            else:
                self.failed_attempts += 1
         print("\n¡OMG! You lost!")

if __name__ == '__main__':
    words_to_guess = random.choice(WORDS)
    hangman = Hangman(words_to_guess)
    hangman.play()


        



