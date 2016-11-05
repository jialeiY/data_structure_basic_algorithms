# -----------------
# User Instructions
# 
# In this problem, you will define a function, boggle_words(), 
# that takes a board as input and returns a set of words that
# can be made from the board according to the rules of Boggle.

def find_neighbors(i,board):
    N=int(len(board)**0.5)
    return [i-1,i+1,i-N,i+N,i-N-1,i-N+1,i+N-1,i+N+1]
def boggle_words(board, minlength=3):
    "Find all the words on this Boggle board; return as a set of words."
    # your code here
    ret=set()
    for i,sq in enumerate(board):
        if sq!='|':
            stack=[(i,"",frozenset())]
            while stack:
                cur,prev_word,visited=stack.pop()
                new_word=prev_word+board[cur]
                if new_word in WORDS and len(new_word)>=minlength:
                    ret.add(new_word)
                if new_word not in PREFIXES:
                    continue
                prev_word=new_word
                visited|=set([cur])
                for n in find_neighbors(cur,board):
                    if board[n]!='|' and n not in visited:
                        stack.append((n,prev_word,visited))
    return ret
        
    
def test():
    b = Board('XXXX TEST XXXX XXXX')
    assert b == '|||||||XXXX||TEST||XXXX||XXXX|||||||'
    assert display(b) == """
||||||
|XXXX|
|TEST|
|XXXX|
|XXXX|
||||||""".strip()

    print boggle_words(b)    
    print boggle_words(Board('PLAY THIS WORD GAME'))

    
def Board(text):
    """Input is a string of space-separated rows of N letters each;
    result is a string of size (N+2)**2 with borders all around."""
    rows = text.split()
    N = len(rows)
    rows = [BORDER*N] + rows + [BORDER*N]
    return ''.join(BORDER + row + BORDER for row in rows)

def size(board): return int(len(board)**0.5)


BORDER = '|'

def display(board):
    "Return a string representation of board, suitable for printing."
    N = size(board)
    return '\n'.join(board[i:i+N] for i in range(0, N**2, N))

# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('word_list.txt')

test()

