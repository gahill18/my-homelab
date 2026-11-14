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

