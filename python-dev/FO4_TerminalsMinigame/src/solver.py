#!/bin/python3

import random
from words import Word, charIndexFrequencies

class Result:
    def __init__(self, guesses: List[Word], remainingWords: Set[Word], winnable: bool):
        self.guesses = guesses
        self.remainingWords = remainingWords
        self.winnable = winnable

    def __str__(self) -> str:
        return f'Result(guesses: {self.guesses}, remainingWords: {self.remainingWords}, winnable: {self.winnable})'
        
class Solver:
    def __init__(self, game: Game):
        self.currentGameState = game

    # Attempt to win from the position given in self.currentGameState
    # First item is a list of guesses made
    # Second item is set of remaining possible answers
    # Third item is whether the game can be won (True) or not (False)
    def solve(self) -> Result:
        guesses: List[Word] = []

        while not self.currentGameState.isGameOver():
            self.currentGameState.printTerminalScreen()
            guess: Word = self.bestSingleTurn()
            guesses.append(guess)
            self.currentGameState.submitGuess(guess)

        winnable = self.currentGameState.gameOver()
        return Result(guesses, self.currentGameState.remainingWords, winnable)

    # Make a decision on which word to guess
    # TODO - Make it smarter! Currently just random
    def chooseWordToGuess(self) -> Word:
        word = random.choice(self.currentGameState.wordList)
        return word       

    def bestSingleTurn(self) -> Word:
        cif = charIndexFrequencies(self.currentGameState.remainingWords)
        print(f'cif: {cif}')
        numRemaining = len(self.currentGameState.remainingWords)
        halved = numRemaining // 2
        bisect = min([(abs(freq-halved), char) for ((char,ind),freq) in cif])
        print(f'bisect: {bisect}')

        
        
        word = random.choice(self.currentGameState.wordList)
        return word       
