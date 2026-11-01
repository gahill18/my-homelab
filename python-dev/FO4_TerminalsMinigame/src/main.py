#!/bin/python3

from game import Game
from solver import Solver, Result
import words

# Determine how many parenthesis/bracket/brace pairs are in a string
def numOpenClosePairs(line: str) -> int:
    prs,brks,brcs = 0,0,0
    ans = 0
    for char in line:
        if char.isalpha():
            prs,brks,brcs = 0,0,0
        match char:
            case '(':
                prs += 1
            case ')':
                ans += prs
                prs = 0
            
            case '{':
                brks += 1
            case '}':
                ans += brks
                brks = 0
            
            case '<':
                brcs += 1
            case '>':
                ans += brcs
                brcs = 0
    return ans

def getConfigFromUser() -> List[int]:
    # TODO - User tweaks/"cheat codes"?
    remainingGuesses = 4
    wordLength = 4
    wordPoolSize = 20
    
    print(f'\n---- Settings/Configuration----')
    print(f'Remaining guesses set to {remainingGuesses}')
    print(f'Word length set to {wordLength}')
    print(f'Initial word pool size set to {wordPoolSize}')
    print(f'---- End ----\n')
    return [remainingGuesses,wordLength,wordPoolSize]

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
