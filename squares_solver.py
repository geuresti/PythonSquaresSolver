import requests
from bs4 import BeautifulSoup
from recursion import validate_word

"""
A simple Squares Solver by Gio Euresti

Important Notes:

- This solver isn't perfect, some of the words the Squares considers valid will
    not appear here as valid answers as I'm not sure which dictionary Squares
    references for its puzzles.

- This solver does not differentiate "bonus" words from regular words.

- You can partially fill out the BOARD variable in order to mimic the current 
    state of your solution (for exmaple, if the top left letter is grayed out).

- You can also modify the line "if len(word) > 3:" to a bigger number in order
    to produce words in specific ranges or at a specific length.

"""

# IMPORTANT: Change this board to match the board you see in your Squares game.
BOARD = [
    'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P'
]

letters = ''.join(BOARD).lower()

# Send a request to the anagrammer api in order to create a list of words
#   that can be made using the letters provided in the BOARD variable.
response = requests.get('https://www.anagrammer.com/crossword/answer/' + letters, timeout=5)

status = response.status_code

if status == 200:
    print("200 SUCCESS")
else:
    print("FAILURE: No response from API")

# Break down the response into HTML
soup = BeautifulSoup(response.text, 'html.parser')

# The actual anagrams are in the "pure-list flex-row wrap" class anchors
container = soup.find_all('div', {'class': 'pure-list flex-row wrap'})

words_found = []

for anchor in container:

    # Each anchor might contain several words
    content = anchor.text.split()

    # Valid anagrams words have to be more than three letters
    for word in content:
        if len(word) > 3:
            words_found.append(word)

squares = []

# Check that the words produced from the anagrams api are valid answers by Squares rules
for word in words_found:
    # See "recursion.py"
    if validate_word(BOARD, word):
        squares.append(word)

# Return a list of (most likely) valid answers
print("\nFOUND", len(squares), "VALID WORDS:\n---------------------")
for square in squares:
    print(square)