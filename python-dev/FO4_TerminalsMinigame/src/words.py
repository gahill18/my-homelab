import requests

class Word:
    def __init__(text: str):
        self.text = text

    
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

# Return the number of positions with matching characters between string 1 and string 2
def countMatchingChars(s1: str, s2: str) -> int:
    matches = 0
    for i in range(min(len(s1),len(s2))):
        if s1[i] == s2[i]:
            matches += 1
    return matches

# Takes a guess, the correct answer, and a list of remaining words, and returns the list of remaining words after narrowing based on the number of matching chars
def narrowRemainingWords(guess: str, answer: str, remainingWords: Set[str]) -> Set[str]:
    matches = countMatchingChars(guess,answer)
    print(f'{matches} letters correct\n')
    if guess in remainingWords:
        remainingWords.remove(guess)
    remainingWords = {rw for rw in remainingWords if countMatchingChars(guess,rw) == matches}
    return remainingWords
