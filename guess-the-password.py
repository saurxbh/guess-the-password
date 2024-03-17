import random, sys

# Set up the constants
# Garbage filler characters for the 'computer memory' display
GARBAGE_CHARS = '~!@#$%^&*()_+-=\{\}[]|;:,.<>?/'

# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline
    WORDS[i] = WORDS[i].strip().upper()


def getOneWordExcept(blocklist=None):
    '''Returns a random word from WORDS that isn't in blocklist'''
    if blocklist == None:
        blocklist = []

    while True:
        randomWord = random.choice(WORDS)
        if randomWord not in blocklist:
            return randomWord


def getWords():
    '''Return a list of 12 words that could possibly be the password.
    The secret password will be the first word in the list. To make the game fair, 
    we ensure that there are words with a range of matching numbers of letters 
    as the secret word.'''
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two words, these have zero matching letters
    # We us '< 3' because the secret password is already in words
    while len(words) < 3:
        randomWord = getOneWordExcept(words)



def main():
    print('''
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press Enter to begin...')

    gameWords = getWords()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
