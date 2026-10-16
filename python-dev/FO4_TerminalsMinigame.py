#!/bin/python3

import copy
import random
import requests

# Takes a URL pointing to a remotely available plaintext list of words separated by commas or newlines
# and returns it as a list of strings
def pullWordListFromURL(src: str = 'https://www.mit.edu/~ecprice/wordlist.10000') -> List[str]:
        r = requests.get(src)
        assert r.status_code == 200, f'Failed to read word list from {src}'

        rawText = r.text
        wordList = rawText.split()
        first,last = wordList[0],wordList[-1]

        print(f'Dictionary length: {len(wordList)}')
        print(f'First: {first}\nLast: {last}')

        return wordList

# Pretty prints some data to the screen in the shape of the Fallout 4 Terminals
def printTerminalScreen(blockLength: int, numRows: int, numCols: int) -> None:
    for r in range(numRows):
        rowText = hex(r) + f':\t' + '0'*blockLength
        for c in range(numCols-1):
            rowText += f'\t' + '0'*blockLength
        print(rowText)

# Return the number of positions with matching characters between string 1 and string 2
def countMatchingChars(s1: str, s2: str) -> int:
    matches = 0
    for i in range(min(len(s1),len(s2))):
        if s1[i] == s2[i]:
            matches += 1
    return matches

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

# Run the game and return a bool indicating whether the player won or not (True=Win)
def run(remainingGuesses: int, wordLength: int, words: Set[str], answer: str) -> bool: 
    remainingWords = copy.deepcopy(words)
    # Let the player guess until they run out of guesses
    while remainingGuesses > 0:
        
        print(f'Remaining guesses: {remainingGuesses}')
        print(f'Remaining possible words: {len(remainingWords)}')
        if len(remainingWords) <= 20:
            print(remainingWords)
        guess = input(f'\nGuess a word\n')
        # TODO - auto sizing?
        printTerminalScreen(blockLength=8,numRows=16,numCols=2)
        print(f'You guessed \'{guess}\'')

        # Player wins the game
        if guess == answer:
            print('You win!')
            return True
        
        # Filter list of remaining possible answers
        else:
            matches = countMatchingChars(guess,answer)
            print(f'{matches} letters correct\n')
            if guess in remainingWords:
                remainingWords.remove(guess)
            remainingWords = {rw for rw in remainingWords if countMatchingChars(guess,rw) == matches}
            remainingGuesses -= 1

    
    print('You lose!')
    return False

    
def main():
    # # TODO - other word sources
    wordList = pullWordListFromURL() 
    
    remainingGuesses, wordLength, wordPoolSize = getConfigFromUser()
    
    # TODO - pull from wordList
    words = random.sample([w for w in wordList if len(w) == wordLength], wordPoolSize)
    answer = random.choice(words)
    assert answer in words
    assert all([len(w) == wordLength for w in words]), f'All words must be of length {wordLength}'
    
    didPlayerWin = run(remainingGuesses, wordLength, words, answer)
    exit(0) if didPlayerWin else exit(1)
    
main()
