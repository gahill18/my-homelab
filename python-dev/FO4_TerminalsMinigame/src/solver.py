#!/bin/python3

import random
from words import Word

class Solver:
    def __init__(self, game: Game):
        self.currentGameState = game

    # Attempt to win from the position given in self.currentGameState
    # Returns a list of length 2
    # First item is a list of guesses made
    # Second item is set of remaining possible answers
    # Third item is whether the game can be won (True) or not (False)
    def solve(self) -> List[List[Word], Set[Word], bool]:
        guesses: List[Word] = []
        guess: Word = self.chooseWordToGuess()
        return [guesses, self.currentGameState.remainingWords, False]

    # Make a decision on which word to guess
    # TODO - Make it smarter! Currently just random
    def chooseWordToGuess(self) -> Word:
        word = random.choice(self.currentGameState.wordList)
        return word       
