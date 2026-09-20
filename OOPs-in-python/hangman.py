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

    def __init__(self, word_to_guess):
        self.failed_attempts = 0
        self.words_to_guess = word_to_guess
        self.game_progress = list('_' * len(word_to_guess))


    # creating a function to find indexes

    def find_indexes(self, letter):
        """
        This function finds the indexes of the letter in the word to guess.
        :param letter: The letter to find the indexes of.
        :return: A list of indexes where the letter is found in the word to guess.
        """
        indexes = []
        for index, char in enumerate(self.word_to_guess):
            if char == letter:
                indexes.append(index)
        return indexes


