import time
import collections
def timedcall(fn,*args):
    """Call function with args; return the time in seconds and result"""
    t0=time.clock()
    result=fn(*args)
    t1=time.clock()
    return t1-t0,result
def prefixes(word):
    """A list of the initial sequences of a word, not including the
    complete word."""
    return [word[:i] for i in xrange(len(word))]
    
def read_wordlist(f):   
    words=set(file(f).read().upper().split())
    
    prefix=set()
    for w in words:
        prefix|=set(prefixes(w))

    return words,prefix
WORDS,PREFIX=read_wordlist("word_list.txt")
POINTS = dict(A=1, B=3, C=3, D=2, E=1, F=4, G=2, H=4, I=1, J=8, K=5, L=1, M=3, 
              N=1, O=1, P=3, Q=10, R=1, S=1, T=1, U=1, V=4, W=4, X=8, Y=4, Z=10, _=0)

class anchor(set):
    "An anchor is where a new word can be placed; has a set of allowable letters."
    
LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ANY = anchor(LETTERS) # The anchor that can be any letter

def transpose(matrix):
    "Transpose e.g. [[1,2,3], [4,5,6]] to [[1, 4], [2, 5], [3, 6]]"
    return map(list, zip(*matrix))
    
def removed(letters,remove):
    """Return a str of letter, with each letter in remove removed once"""
    for l in remove:
        letters=letters.replace(l if l.isupper() else '_','',1)
    return letters
    
def find_words(hand,pre='',results=None):
    "Find all words that can be made from the letters in hand"

    if results is None: results=set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIX:
        for l in hand:
            find_words(hand.replace(l,'',1),pre+l,results)

    return results

cache=collections.defaultdict(set)
def find_prefixes(hand,pre='',results=None):
    "Find all prefixes (of words) that can be made from letters in hand."
    if results is None: results=set()
    if (hand,pre) in cache:
        results|=cache[(hand,pre)]
        return results
    if pre.upper() in PREFIX:
        results.add(pre)
        for l in hand:
            l2=map(str.lower,LETTERS) if l=='_' else [l]
            for ll in l2:
                find_prefixes(hand.replace(ll if ll.upper() else '_',"",1),pre+ll,results) 
        cache[(hand,pre)]=results
    return results

  
def is_letter(sq):
    return isinstance(sq, str) and sq in LETTERS

def is_empty(sq):
    "Is this an empty square (no letters, but a valid position on board)."
    return sq  == '.' or sq == '*' or isinstance(sq, set) 

def add_suffixes(hand, pre, start, row, results, anchored=True):
    "Add all possible suffixes, and accumulate (start, word) pairs in results."
    i = start + len(pre)
    if pre.upper() in WORDS and anchored and not is_letter(row[i]):
        results.add((start, pre))
    if pre.upper() in PREFIX:       
        sq = row[i]
        if is_letter(sq):
            add_suffixes(hand, pre+sq, start, row, results)        
        elif is_empty(sq):        
            possibilities = sq if isinstance(sq, set) else ANY
            for L in hand:
                L2=map(str.lower,LETTERS) if L=='_' else [L]

                for l in L2:
                    if l.upper() in possibilities:
                        add_suffixes(hand.replace(l if l.isupper() else '_', '', 1), pre+l, start, row, results)
    return results

def legal_prefix(i, row):
    """A legal prefix of an anchor at row[i] is either a string of letters
    already on the board, or new letters that fit into an empty space.
    Return the tuple (prefix_on_board, maxsize) to indicate this.
    E.g. legal_prefix(a_row, 9) == ('BE', 2) and for 6, ('', 2)."""
    s = i
    while is_letter(row[s-1]): s -= 1
    if s < i: ## There is a prefix
        return ''.join(row[s:i]), i-s
    while is_empty(row[s-1]) and not isinstance(row[s-1], set): s -= 1
    return ('', i-s)
    
def row_plays(hand, row):
    "Return a set of legal plays in row.  A row play is an (start, 'WORD') pair."
    results = set()
    ## To each allowable prefix, add all suffixes, keeping words
    for (i, sq) in enumerate(row[1:-1], 1):
        if isinstance(sq, set):
            pre, maxsize = legal_prefix(i, row)
            if pre: ## Add to the letters already on the board
                start = i - len(pre)
                add_suffixes(hand, pre, start, row, results, anchored=False)
            else: ## Empty to left: go through the set of all possible prefixes
                for pre in find_prefixes(hand):
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(removed(hand, pre), pre, start, row, results,
                                     anchored=False)
    return results
    
def find_cross_word(board, i, j):
    """Find the vertical word that crosses board[j][i]. Return (j2, w),
    where j2 is the starting row, and w is the word"""
    sq = board[j][i]
    w = sq if is_letter(sq) else '.'
    for j2 in range(j, 0, -1):
        sq2 = board[j2-1][i]
        if is_letter(sq2): w = sq2 + w
        else: break
    for j3 in range(j+1, len(board)):
        sq3 = board[j3][i]
        if is_letter(sq3): w = w + sq3
        else: break
    return (j2, w)

def neighbors(board, i, j):
    """Return a list of the contents of the four neighboring squares,
    in the order N,S,E,W."""
    return [board[j-1][i], board[j+1][i],
            board[j][i+1], board[j][i-1]]

def set_anchors(row, j, board):
    """Anchors are empty squares with a neighboring letter. Some are resticted
    by cross-words to be only a subset of letters."""
    for (i, sq) in enumerate(row[1:-1], 1):
        neighborlist = (N,S,E,W) = neighbors(board, i, j)
        # Anchors are squares adjacent to a letter.  Plus the '*' square.
        if sq == '*' or (is_empty(sq) and any(map(is_letter, neighborlist))):    
            if is_letter(N) or is_letter(S):   
                # Find letters that fit with the cross (vertical) word
                (j2, w) = find_cross_word(board, i, j)
                row[i] = anchor(L for L in LETTERS if w.replace('.', L) in WORDS)
            else: # Unrestricted empty square -- any letter will fit.
                row[i] = ANY
                
def calculate_score(board, pos, direction, hand, word):
    "Return the total score for this play."
    total, crosstotal, word_mult = 0, 0, 1
    starti, startj = pos
    di, dj = direction
    other_direction = DOWN if direction == ACROSS else ACROSS
    for (n, L) in enumerate(word):
        i, j = starti + n*di, startj + n*dj
        sq = board[j][i]
        b = BONUS[j][i]
        word_mult *= (1 if is_letter(sq) else
                      3 if b == TW else 2 if b in (DW,'*') else 1)
        letter_mult = (1 if is_letter(sq) else
                       3 if b == TL else 2 if b == DL else 1)
        total += POINTS[L if L.isupper() else '_'] * letter_mult
        if isinstance(sq, set) and sq is not ANY and direction is not DOWN:
            crosstotal += cross_word_score(board, L, (i, j), other_direction)
    return crosstotal + word_mult * total
    
def cross_word_score(board, L, pos, direction):
    "Return the score of a word made in the other direction from the main word."
    i, j = pos
    (j2, word) = find_cross_word(board, i, j)
    return calculate_score(board, (i, j2), DOWN, L, word.replace('.', L))    
  
ACROSS, DOWN = (1, 0), (0, 1) # Directions that words can go
def horizontal_plays(hand, board):
    "Find all horizontal plays -- (score, pos, word) pairs -- across all rows."
    results = set()
    for (j, row) in enumerate(board[1:-1], 1):
        set_anchors(row, j, board)
        for (i, word) in row_plays(hand, row):
            score = calculate_score(board, (i, j), ACROSS, hand, word)
            results.add((score, (i, j), word))
    return results


def all_plays(hand, board):
    """All plays in both directions. A play is a (score, pos, dir, word) tuple,
    where pos is an (i, j) pair, and dir is a (delta-_i, delta_j) pair."""
    hplays = horizontal_plays(hand, board)
    vplays = horizontal_plays(hand, transpose(board))
    return (set((score, (i, j), ACROSS, w) for (score, (i, j), w) in hplays) |
            set((score, (i, j), DOWN, w) for (score, (j, i), w) in vplays))                
def a_board():
    return map(list, ['|||||||||||||||||',
                      '|J............I.|',
                      '|A.....BE.C...D.|',
                      '|GUY....F.H...L.|',
                      '|||||||||||||||||'])    

def bonus_template(quadrant):
    "Make a board from the upper-left quadrant."
    return mirror(map(mirror, quadrant.split()))

def mirror(sequence): return sequence + sequence[-2::-1]

SCRABBLE = bonus_template("""
|||||||||
|3..:...3
|.2...;..
|..2...:.
|:..2...:
|....2...
|.;...;..
|..:...:.
|3..:...*
""")

WWF = bonus_template("""
|||||||||
|...3..;.
|..:..2..
|.:..:...
|3..;...2
|..:...:.
|.2...3..
|;...:...
|...:...*
""")

BONUS = WWF

DW, TW, DL, TL = '23:;'   

def show(board):
    "Print the board."    
    for i,row in enumerate(board):
        print" ".join([sq if is_letter(sq) or sq=='|' else BONUS[i][j] 
        for j,sq in enumerate(row)])

def make_play(play, board):
    "Put the word down on the board."
    (score, (i, j), (di, dj), word) = play

    for w in word:
        board[j][i]=w
        i+=di
        j+=dj
    return board     
def best_play(hand, board):
    "Return the highest-scoring play.  Or None."
    ret=sorted(all_plays(hand, board),key=lambda x:x[0])
    if ret:
        return ret[-1]
    else:
        return None    
def show_best(hand,board):
    print 'Current board:'
    show(board)
    play=best_play(hand,board)
    if play:
        print 'New word: %r scores %d'%(play[-1],play[0])
        show(make_play(play,board))
    else:
        print 'Sorry, no legal plays'
def word_score(word):
    "The sum of the individual letter point scores for this word."
    return sum(POINTS[w] for w in word)    

def test():
    
    assert prefixes("APPLE")==['','A','AP','APP','APPL']
    assert 'THE' in WORDS
    assert '' in PREFIX
    assert find_words("HTABE")==set(['BE', 'BAT', 'ATE', 'BA', 'HT', 
    'BATH', 'BT', 'B', 'HB', 'E', 'HA', 'HATE', 'BET', 'HE', 'TEA', 
    'EH', 'TAB', 'H', 'TE', 'TB', 'EAT', 'TA', 'A', 'AB', 'AE', 'TH', 
    'BEAT', 'AH', 'EA', 'HEAT', 'T', 'ET', 'THE', 'BETH', 'HAT', 'BETA', 
    'TBA', 'AT'])
    
    assert find_prefixes('ADEQUAT')==set(['', 'AA', 'TEA', 'QAT', 'DE', 'DET', 
    'DEU', 'DA', 'QATA', 'EQUAT', 'DATE', 'DEA', 'DT', 'DU', 'DATA', 'DEAT', 
    'D', 'AQU', 'QUA', 'ADEQUA', 'DETA', 'EQ', 'TU', 'TED', 'DAT', 'DAU', 
    'EQU', 'ED', 'TE', 'E', 'EAT', 'TA', 'A', 'ADU', 'AE', 'AD', 'TAU', 'DUA', 
    'UT', 'EA', 'UTA', 'AQ', 'ADE', 'AU', 'AT', 'ADA', 'EU', 'ET', 'DUT', 
    'DEUT', 'ADEQ', 'Q', 'QU', 'QT', 'AUD', 'EQUA', 'AQUAT', 'AQUA', 'T', 'QA',
    'ADEQU', 'QUE', 'EDU', 'U', 'ADEQUAT', 'TUE', 'AUT'])
    
    #show_best('ADEQUAT',a_board())
    
    t, results = timedcall(find_prefixes,'ADEQUAT')
    show_best('_BCEHKN',a_board())  
    
    print 'tests pass'

test()