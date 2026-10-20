from words import Word
import copy
import random
import words

class Game:
    def __init__(self, remainingGuesses: int, wordLength: int, wordList: List[Word], answer: Word, wordPoolSize: int):
        self.remainingGuesses = remainingGuesses
        self.wordLength = wordLength
        self.wordList = wordList
        self.wordPoolSize = wordPoolSize
        self.answer = answer

        self.remainingWords = set(copy.deepcopy(wordList))

    def randomGameFromWordList(wordList: List[Word]) -> Game:
        remainingGuesses = 4
        wordLength = 4
        wordPoolSize = 20
        randomWordList = random.sample([w for w in wordList if len(w) == wordLength], wordPoolSize)
        answer = random.choice(randomWordList)
        assert answer in randomWordList
        assert all([len(w) == wordLength for w in randomWordList]), f'All words must be of length {wordLength}'

        gameState = Game(
            remainingGuesses,
            wordLength,
            randomWordList,
            answer,
            wordPoolSize
        )
        
        return gameState
        
    def submitGuess(self, guess: Word) -> None:
        print(f'You guessed \'{guess}\'')
        # Filter list of remaining possible answers
        self.remainingWords = words.narrowRemainingWords(guess,self.answer,self.remainingWords)
        self.remainingGuesses -= 1

    def hasPlayerLost(self) -> bool:
        return self.remainingGuesses == 0

    def hasPlayerWon(self) -> bool:
        return len(self.remainingWords) <= 1

    def isGameOver(self) -> bool:
        return self.hasPlayerLost() or self.hasPlayerWon()

    def gameOver(self) -> None:
        print('You win!' if len(self.remainingWords) == 0 or self.remainingGuesses > 0 else 'You lose!')
        _ = input('Press enter to return to the main menu')
        return

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
        while not self.hasPlayerLost():
            # TODO - auto sizing?
            self.printTerminalScreen()
            self.printGameState()
            guess = input(f'\nGuess a word\n')
            if self.submitGuess(guess):
                return self.gameOver()
        
        return self.gameOver()
