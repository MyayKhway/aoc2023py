def scanNumber(i,j):
    if i>len(board) or j >len(board[0]) or i < 0 or j < 0 or (i,j) in seenAlready: return 0
    if not board[i][j].isnumeric(): return 0
    digits = board[i][j]
    seenAlready.append((i,j))
    # scan left
    lj = j - 1
    while lj >= 0:
        if not board[i][lj].isnumeric(): break
        digits = board[i][lj] + digits
        seenAlready.append((i,lj))
        lj -= 1
    # scan right
    rj = j + 1
    while rj < len(board[0]):
        if not board[i][rj].isnumeric(): break
        digits = digits + board[i][rj]
        seenAlready.append((i,rj))
        rj += 1
    print(digits)

    return int(digits)
    

def getAdjacentNumbers(i,j):
    seenAlready = []
    nw = scanNumber(i-1,j-1)
    n = scanNumber(i-1,j)
    ne = scanNumber(i-1,j+1)
    w = scanNumber(i,j-1)
    e = scanNumber(i,j+1)
    sw = scanNumber(i+1,j-1)
    s = scanNumber(i+1, j)
    se = scanNumber(i+1, j+1)
    adj = [nw,n,ne,w,e,sw,s,se]
    adj = [x for x in adj if x > 0]
    return adj[0]*adj[1] if len(adj)==2 else 0
    #return nw+n+ne+w+e+sw+s+se
    

board = []
seenAlready = []
total = 0
with open("input3.txt", 'r') as f: board = [[c for c in line.rstrip()] for line in f]
for i, line in enumerate(board):
    for j,c in enumerate(line):
        if c == '*':
            # symbol hit
            total += getAdjacentNumbers(i,j)
print(total)