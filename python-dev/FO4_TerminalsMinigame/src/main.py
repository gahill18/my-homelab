#!/bin/python3

from game import Game
from solver import Solver, Result
import words

def mainMenu() -> None:
    # # TODO - other word sources
    wordList = words.pullWordListFromURL() 
    first,last = wordList[0],wordList[-1]
    print(f'Dictionary length: {len(wordList)}')
    print(f'First: {first}\nLast: {last}')

    button: str = ''
    while button != 'Q':
        button: str = input('\n[N]ew Game\n[S]olve Random\n[Q]uit\n').upper()
        if button == 'N':
            # remainingGuesses, wordLength, wordPoolSize = getConfigFromUser()
            gameState = Game.randomGameFromWordList(wordList)
            didPlayerWin = gameState.run()
        elif button == 'S':
            gameState = Game.randomGameFromWordList(wordList)
            solver: Solver = Solver(gameState)
            attemptResult: Result = solver.solve()
            print(attemptResult)
        else:
            print(f'Did not recognize option {button}')

    print('Thanks for playing!')
    exit(1)

mainMenu()
