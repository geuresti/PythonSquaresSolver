"""

This program has a series of functions that help "squares_solver.py" function properly

I added lots of comments to try explaining how it works but to put it in simple terms,

(steps 1, 2, and 5 happen in the squares_solver.py file)

1. We have a 4x4 board of letters.

2. We use an anagrams API to create a list of words that can be made using those letters.

3. We pass those words one at a time into our validate_word() function.

4. The validate_word() function looks for a path between the first and last letters of the word.

    4a. Start at the first letter of the word

    4b. Check if the second letter of the word is adjacent to the first

        If so, repeat until the last letter is reached

        If not, check if are any other paths we can take to reach the last letter

            If so, try the new path

            if not, return False

5. If validate_word() finds a path, return True and add that word to our list of answers.

"""

# Recursive path searching function
def word_validator(board, word, ci, path, visited):

    # There is a path on the board that includes all letters: the word is valid!
    if ci == len(word):
        return True

    # Get a list of all optional routes we can take to create the given word
    options = has_adjacent(board, path[-1], word[ci])

    # Hit a dead end
    if options == []:
        pass
    
    # Try every possible valid path and track which places we've visited
    for op in options:
        if op not in path and op not in visited:
            path.append(op)
            visited.append(op)
            return word_validator(board, word, ci+1, path, visited)

    if len(path) > 1:
        # Backtrack and see if there is a different route to form the word
        return word_validator(board, word, ci-1, path[:-1], visited)
    else:
        # The word is impossible to make using Squares rules
        return False

# This is a helper function for word_validator(). Some words start with a
#   letter that occurs in multiple locations throughout the board so let's
#   check every possible starting point to try validating the word.
def validate_word(board, word):

    # Traverse the board and see if the first letter of "word" matches
    #   any of the letters on the board.
    for key, value in enumerate(board):
        # If there's a match, pass that index to the word_validator() to see
        #   if a path can be drawn from the first letter of "word" to the last.
        if value == word[0]:
            if word_validator(board, word, 1, [key], [key]):
                return True
    return False

# index (location on board)
# character (to look for adjacent)
# returns list of indices of the adjacent character
def has_adjacent(board, index, character):
    # We need to check if the given index is adjacent to the given character.
    if character in board:
        options = []
        # Check the index of every instance of "character" on the board 
        #   and compare that to the given "index" value to check adjacency.
        for key, value in enumerate(board):  
            if value == character:
                if in_range(index, key):
                    # We add this to a list of options rather than returning True/False 
                    # because a given index can have multiple instances of "character" nearby
                    options.append(key)
        if len(options) > 0:
            return options
        else:
            return []
    else:
        print("ERROR: Character does not exist in board")
        return []

# A function that will check if any given two indicies (n1, n2) are adjacent within a 4x4 board
def in_range(n1, n2):

    # Set n1 to be the smaller number
    if n1 > n2:
        temp = n2
        n2 = n1 
        n1 = temp

   # print("Is " + str(n1) + " in range of " + str(n2) + "?\n")
    match n1:
        case 0:
            return True if n2 in [1, 4, 5] else False
        case 1:
            return True if n2 in [0, 2, 4, 5, 6] else False
        case 2:
            return True if n2 in [1, 3, 5, 6, 7] else False
        case 3:
            return True if n2 in [2, 6, 7] else False
        case 4:
            return True if n2 in [0, 1, 5, 8, 9] else False
        case 5:
            return True if n2 in [0, 1, 2, 4, 6, 8, 9, 10] else False
        case 6:
            return True if n2 in [1, 2, 3, 5, 7, 9, 10, 11] else False
        case 7:
            return True if n2 in [2, 3, 6, 10, 11] else False
        case 8:
            return True if n2 in [4, 5, 9, 12, 13] else False
        case 9:
            return True if n2 in [4, 5, 6, 8, 10, 12, 13, 14] else False
        case 10:
            return True if n2 in [5, 6, 7, 9, 11, 13, 14, 15] else False
        case 11:
            return True if n2 in [6, 7, 10, 14, 15] else False
        case 12:
            return True if n2 in [8, 9, 13] else False
        case 13:
            return True if n2 in [8, 9, 10, 12, 14] else False
        case 14:
            return True if n2 in [9, 10, 11, 13, 15] else False
        case 15:
            return True if n2 in [10, 11, 14] else False

# A board for testing purposes
BOARD = [
    'R', 'O', 'C', 'S',
    'I', 'U', 'E', 'C',
    'A', 'N', 'S', 'N',
    'D', 'U', 'R', 'A'
]

# An example of how to test whether a word exists on the board
if __name__ == "__main__":
    word = "COINSURANCES"
    print(validate_word(BOARD, word))
    print(word_validator(BOARD, word, 1, [2], [2]))