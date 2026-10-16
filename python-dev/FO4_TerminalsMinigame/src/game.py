import copy
import words

class Game:
    def __init__(self, remainingGuesses: int, wordLength: int, wordList: List[str], answer: str):
        self.remainingGuesses = remainingGuesses
        self.wordLength = wordLength
        self.wordList = wordList
        self.remainingWords = set(copy.deepcopy(wordList))
        self.answer = answer

    def printGameState(self) -> None:
        print(f'Remaining guesses: {self.remainingGuesses}')
        print(f'Remaining possible words: {len(self.remainingWords)}')
        
    # Pretty prints some data to the screen in the shape of the Fallout 4 Terminals
    def printTerminalScreen(self) -> None:
        numCols = 2
        numRows = len(self.wordList) // numCols
        for r in range(numRows):
            rowText = hex(r) + f':\t'

            w1 = self.wordList[r*2]
            rowText += w1 if w1 in self.remainingWords else '.'*self.wordLength

            rowText += '\t'
            
            w2 = self.wordList[r*2+1]
            rowText += w2 if w2 in self.remainingWords else '.'*self.wordLength

            print(rowText)
        print('')
            

# Run the game and return a bool indicating whether the player won or not
    def run(self) -> bool:
        # Let the player guess until they run out of guesses
        while self.remainingGuesses > 0:
            # TODO - auto sizing?
            self.printTerminalScreen()
            self.printGameState()
            guess = input(f'\nGuess a word\n')
            print(f'You guessed \'{guess}\'')
    
            # Player wins the game
            if guess == self.answer:
                print('You win!')
                return True
            
            # Filter list of remaining possible answers
            else:
                self.remainingWords = words.narrowRemainingWords(guess,self.answer,self.remainingWords)
                self.remainingGuesses -= 1
    
        
        print('You lose!')
        return False
