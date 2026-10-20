#!/bin/python3

import random
from words import Word

class Solver:
    def __init__(self, game: Game):
        self.currentGameState = game

    # Attempt to win from the position given in self.currentGameState
    # First item is a list of guesses made
    # Second item is set of remaining possible answers
    # Third item is whether the game can be won (True) or not (False)
    def solve(self) -> List[List[Word], Set[Word], bool]:
        guesses: List[Word] = []

        while not self.currentGameState.isGameOver():
            guess: Word = self.chooseWordToGuess()
            guesses.append(guess)
            self.currentGameState.submitGuess(guess)

        winnable = self.currentGameState.gameOver()
        return [guesses, self.currentGameState.remainingWords, winnable]

    # Make a decision on which word to guess
    # TODO - Make it smarter! Currently just random
    def chooseWordToGuess(self) -> Word:
        word = random.choice(self.currentGameState.wordList)
        return word       
