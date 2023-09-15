# CSCI 1913 Fall 2022
# Author: Brock Bye

# QUESTIONS -- DO THESE LAST.
# Assumptions: assume the letter grid has width W and height H
# Further assume the word parameter has length L (for find) and than the max_len parameter is L (for extract)
# Finally, Assume that concatenating a letter to a string takes time O(1)
# List any other assumptions you make.

# For each question below, answer your questions by filling in the provided multi-line strings.
# (yes it's a bit of a hokey way to do this, but it should work well enough and it keeps the answers in 1 file)
# For each question state any extra assumptions you made, and explain your answer.
# An incorrect answer with no explanation will get no partial credit.

# Question 1: What is the worst-case big-O runtime of your get_size function?
Question1 = '''
O(1), the built in len() func is always Big O runtime O(1)
'''

# Question 2: What is the worst-case big-O runtime of your copy_word_grid function?
Question2 = '''
O(H), assuming concatinating list to list is Big O runtime O(1), 
func is only dependent on given H of word_grid in the number of total iterations.
'''

# Question 3: What is the worst-case big-O runtime of your extract function?
Question3 = '''
O(L), assuming concatinating letter to string is Big O runtime O(1), 
func is only dependent on max_len given in param, in the number of total iterations made. 
'''

# Question 4: What is the worst-case big-O runtime of your find function?
Question4 = '''
O(H*W*L), assuming that the list DIRECTIONS is always length four (Right, Down, Right Up, Right Down) which is Big O runtime O(1) 
but within the DIRECTIONS loop, the extract func is called which has Big O runtime O(L), the func is only dependent on H, W, and L 
dimensions of word_grid, in the number of total iterations made.
'''

### LEAVE THESE LINES ALONE BEGIN:
# So the code I provide at the bottom needs these lines of code.
import random

# This code defines valid directions a word can travel.
# Each direction is a tuple (dx, dy) that says how you change x and y 
# coordinates to go in a given direction.
RIGHT=(1, 0)       # to go right add 1 to x
DOWN=(0,1)         # to go down add 1 to y
RIGHT_DOWN=(1, 1)  # to go right_down add 1 to both x and y
RIGHT_UP=(1,-1)    # to go right_up add 1 to x and subtract 1 from y
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)
# Good use of these direction-tuples makes for much easier programs for this project. assignment.

### LEAVE THESE LINES ALONE END:



def get_size(word_grid):
    """
    

    Parameters
    ----------
    word_grid : List
        The get size function should have a single parameter – a letter grid in the list of letters format. .

    Returns
    -------
    Width & Height of word_grid: Tuple
        The return value of this function should be a tuple with two elements: the width, and height of the grid, in that order..

    """
    return len(word_grid[0]), len(word_grid)


def print_word_grid(word_grid):
    """
    

    Parameters
    ----------
    word_grid : List
        The print word grid function should print the word grid in a “dense” format suitable for an end-user..

    Returns
    -------
    None.
    Note, this function has no return value – it is expected to output directly to the user

    """
    for word in word_grid:
        s = ""
        for char in word:
            s += char
        print (s)


def copy_word_grid(word_grid):
    """
    

    Parameters
    ----------
    word_grid : List
        Letter grid.

    Returns
    -------
    copyLst : List
        Make a copy of a letter grid, modify the letter grid, and have the original remain unmodified..

    """
    copyLst = []
    for word in word_grid:
        copy = []
        copy += word
        copyLst.append(copy)
    return copyLst


def extract(word_grid, position, direction, max_len):
    """
    

    Parameters
    ----------
    word_grid : List
        – a letter grid.
    position : Tuple
        – a location (tuple of two integers x and y).
    direction : Tuple
        – a direction (tuple of two integers as documented earlier).
    max_len : Int
        – an integer.

    Returns
    -------
    s : String
    
        The purpose of the extract function is to extract a string from the grid of letters starting
        at the given position, moving in the given direction containing no more than max len letters.
        If there are max len letters available starting from the provided start location, going in the
        provided direction, then a string of length max len should be returned. However, if the top,
        left, right, or bottom edge of the grid is reached before max len is reached, a shorter string
        should be returned..

    """
    c_position = list(position)          #(x, y)   Need to make a copy of tuple into list, so we can access the directions and position
    c_direction = list(direction)       #(x, y)
    c = 1
    s = ""
    
    #Check If initial position is out of bounds of grid, return s
    if c_position[1] > (len(word_grid) - 1):
        return s
    elif c_position[0] > (len(word_grid[0]) - 1):
        return s
    
    s += word_grid[ c_position[1] ][ c_position[0] ]
        
    while c < max_len:
        #Increment direction to each position
        c_position = [c_position[0] + c_direction[0], c_position[1] + c_direction[1]]
        #Note that -1 case checks to make sure that loop doesn't iterate when restarting to opposite side of word_grid
        if (c_position[1] > (len(word_grid) - 1)) or (c_position[1] == -1):
            return s
        elif c_position[0] > (len(word_grid[0]) - 1):
            return s
        s += word_grid[ c_position[1] ][ c_position[0] ]
        c += 1
    return s
    

def find(word_grid, word):
    """
    

    Parameters
    ----------
    word_grid : List
        Letter grid.
    word : String
        Target word.

    Returns
    -------
    pos : Tuple
        Position of first letter in word.
    k : Tuple
        Direction of word.
    None:
        If the word cannot be found in the given grid
        
        The find function should take a letter grid and a word. If the word can be found in the grid,
        then the location, and direction, at which the word can be found should be returned as the
        solution.
        
    """
    pos = ()
    
    for i in range(len(word_grid) - 1):
        for j in range(len(word_grid[i]) - 1):
            for k in DIRECTIONS:
                # Check all directions
                s = extract(word_grid, (i, j), k, len(word))
                if word in s:
                    pos = (i, j)
                    
                    return (pos, k)
    if pos == ():
        return None
                

def show_solution(word_grid, word): 
    """
    

    Parameters
    ----------
    word_grid : List
        letter grid.
    word : String
        Target word.

    Returns
    -------
    None.
    
    If the word cannot be found in the word grid, a simple message saying the word could
    not be found should be printed
    
    Alternatively, if the word is in the word grid, the word should be capitalized, and then the
    grid should be printed. (Note, this should not modify the grid provided, you may find it
    useful to make a copy of the grid in this function)

    """
    #Check if Word isn't in word_grid
    if find(word_grid, word) != None:
        #Make copy of grid in order to not modify orginal word_grid
        c_grid = copy_word_grid(word_grid)
        pos, direction = find(c_grid, word)
        
        for i in range(len(word)):
            #Change letter case to Upper
            c_grid[pos[1]] [pos[0]] = word[i].upper()
            pos = [pos[0] + direction[0], pos[1] + direction[1]]
        
        print(word.upper(), 'can be found as below')
        print_word_grid(c_grid)
        
    else:
        print(word, 'is not found in this word search')


def make_empty_grid(width, height):
    """
    

    Parameters
    ----------
    width : Int
        Width of desired grid.
    height : Int
        Height of desired grid.

    Returns
    -------
    grid : List
        Desired grid with given dimensions
        
        Initially, the word-grid should have ’?’ in all positions.

    """
    grid = []
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append('?')
    return grid


def can_add_word(word_grid, word, position, direction):
    """
    

    Parameters
    ----------
    word_grid : List
        grid full of '?'.
    word : String
        Desired word.
    position : Tuple
        Position of first letter in word.
    direction : Tuple
        Direction of word with respect to letter grid and first letter in word.

    Returns
    -------
    bool
        Whether or not word can be added to word_grid.

    This function should check if it is currently possible to add a given word to a given word
    grid, in a given place/direction. The function should return True if the placement is possible
    and False if not.

    """
    c_grid = copy_word_grid(word_grid)
    currWord = extract(c_grid, position, direction, len(word))
    if len(word) > len(currWord):
        #Rule: There must be enough space starting in the given position for the word
        return False
    else: 
        for i in range(len(currWord) - 1):
            #Check for if letter is blank letter '?'
            if currWord[i] != '?':
                if word[i] != currWord[i]:
                    #Rule:  The word cannot conflict with existing word placements
                    return False
                #Given placement would be valid otherwise
        return True
                

def do_add_word(word_grid, word, position, direction):
    """
    

    Parameters
    ----------
    word_grid : List
        word_grid.
    word : String
        Desired word.
    position : Tuple
        Desired position.
    direction : Tuple
        Desired direction.

    Returns
    -------
    word_grid : TYPE
        word_grid with newly added word.

    This function should change the word grid to add the word at the indicated position (in
    the indicated direction). Your function does not have to worry about running out of space,
    or changing letters in an invalid way: this function will only be called with inputs that
    can add word indicates are valid and safe
    
    """
    c_position = list(position)                 
    c_direction = list(direction)
    c = 0
    word_grid[c_position[1]][c_position[0]] = word[c]
    
    while c < (len(word) - 1):
        c_position = [c_position[0] + c_direction[0], c_position[1] + c_direction[1]]
        #Note that 'c' purpose serves as a counter and also as an index
        c += 1
        word_grid[c_position[1]][c_position[0]] = word[c]
        
    return word_grid


def fill_blanks(word_grid):
    """
    

    Parameters
    ----------
    word_grid : List
        word_grid with newly added word.

    Returns
    -------
    None.
    
    It should loop over this word grid and fill each position that currently has the blank letter ’?’ 
    with a random lower-case alphabetical letter.

    """

    randomLetter = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(word_grid)):
        for j in range(len(word_grid[i])):
            if word_grid[i][j] == '?':
                #Change blank letter to random letter in the alphabet
                word_grid[i][j] = random.choice(randomLetter)
                
    return word_grid


####
#
#  PROVIDED CODE -- You shouldn't need to change any of this.
#  (it's not that we didn't think you could write this, it's this stuff is either
#  1) really easy and not worth putting in a 1913 project or
#  2) really, really specific. (it's hard to describe the correct function of
#     these two functions without just telling you exactly how to do it.)
#
#  These are provided to "complete" the project -- I.E. these work with the code you write and allow you to use your
#  functions to generate word-searches for personal use. It is RECOMMENDED that you build a front-end for this behavior
#  so you can more easily use and play-with the finished product.
####
def add_word(word_grid, word):
    ''' Attempts to '''
    width, height = get_size(word_grid)
    for attempt_num in range(50):
        direction = random.choice(DIRECTIONS)
        x = random.randrange(width)
        y = random.randrange(height)
        location = (x, y)
        if can_add_word(word_grid, word, location, direction):
            do_add_word(word_grid, word, location, direction)
            return True
    return False

def generate(width, height, words):
    words_actual = []
    word_grid = make_empty_grid(width, height)
    for word in words:
        if add_word(word_grid, word):
            words_actual.append(word)
    fill_blanks(word_grid)
    return word_grid, words_actual