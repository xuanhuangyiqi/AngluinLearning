#coding: utf-8

def ask(word):
    ans = raw_input("Is '%s' a word of your language?(y/n)\n"%word)
    if ans[0] == 'y':
        return 1
    else:
        return 0

def add_item(word, R, S, f, charset):
    R.append(word)
    for suffix in S:
        if word+suffix not in f:
            f[word+suffix] = ask(word+suffix)
        for char in charset:
            if word+char not in R and word+char+suffix not in f:
                f[word+char+suffix] = ask(word+char+suffix)
    return

def init():
    charset = raw_input("Enter the charset in a line:\n")
    
    R = []
    S = ['']
    f = {}

    add_item('', R, S, f, charset)
    
    return R, S, f, charset

def isSame(u1, u2, S, f):
    for s in S:
        if f[u1+s] != f[u2+s]:
            return False
    return True

def extend_item(s, R, S, f, charset):
    S.append(s)
    for r in R:
        if r+s not in f:
            f[r+s] = ask(r+s)
        for char in charset:
            if r+char not in R and r+char+s not in f:
                f[r+char+s] = ask(r+char+s)
    return


def automaton(R, S, f, charset):
    Q = []
    start = 0
    delta = {}
    F = []
    for r in R:
        state = 0
        for s in S:
            state = state * 2 + f[r+s]
        if state not in Q:
            Q.append(state)
        if r == '':
            start = state
        for a in charset:
            tstate = 0
            for s in S:
                tstate = tstate * 2 + f[r+a+s]
                delta[(state, a)] = tstate
    
    for r in R:
        q0 = 0
        for s in S:
            q0 = q0 * 2 + f[r+s]
        for s in S:
            if f[r+s] == 1:
                q = q0
                for w in s:
                    q = delta[(q, w)]
                if q not in F:
                    F.append(q)
    return Q, charset, start, delta, F

            

def observation_table(R, S, f, charset):
    print 'Observation Table:'
    print '|R/S',
    for s in S:
        if s == '':
            print '\t|' + 'ϵ',
        else:
            print '\t|' + s,
    print '|'

    for r in R:
        if r == '':
            print '|' + 'ϵ',
        else:
            print '|' + r,
        for s in S:
            print '\t|', f[r+s],
        print '|'

    for r in R:
        for char in charset:
            if r+char not in R:
                if r == '':
                    print '|'+'ϵ'+'.'+char,
                else:
                    print '|'+r+'.'+char,
                for s in S:
                    print '\t|', f[r+char+s],
                print '|'

def star(a):
    if a == '':
        return ''
    else:
        return '(%s)*'%a

def regex(A):
    Q, charset, start, delta, F = A
    N = max(Q) + 1
    L = [['' for i in range(N)] for j in range(N)]
    for q in Q:
        for a in charset:
            L[q][delta[(q, a)]] += a

    rm = [False for x in range(N)]
    for q in Q:
        if q != start and q not in F:
            # remove q
            rm[q] = True
            for i in Q:
                for j in Q:
                    if i != q and j != q and L[i][q] != '' and L[q][j] != '' and not rm[i] and not rm[j]:
                        if L[i][j] != '':
                            L[i][j] += '+'
                        L[i][j] += '(%s)'%(L[i][q]+star(L[q][q])+L[q][j])
                        # print i, j, L[i][j]
                        
    ans = ''
    for x in F:
        if ans != '':
            ans += '+'
        ans += '(%s)'%L[start][x]
        if start == x:
            ans += '*'

    return ans

def output(R, S, f, charset):
    observation_table(R, S, f, charset)
    A = automaton(R, S, f, charset)
    print 'Regex: ', regex(A)
    
def isRight():
    ans = raw_input("Is the result right?(y/n)")
    if ans[0] == 'y':
        return True
    return False

def main():
    R, S, f, charset = init()

    while True:
        while True:
            change = False
            # check closed:
            for u in R:
                for a in charset:
                    found = False
                    for r in R:
                        if isSame(u+a, r, S, f):
                            found = True
                    if not found:
                        change = True
                        add_item(u+a, R, S, f, charset)

            # check consistent:
            for u1 in R:
                for u2 in R:
                    if u1 != u2 and isSame(u1, u2, S, f):
                        for char in charset:
                            if not isSame(u1+char, u2+char, S, f):
                                for s in S:
                                    if f[u1+char+s] != f[u2+char+s]:
                                        change = True
                                        extend_item(s+char, R, S, f, charset)
                                        break

            if not change: break
        output(R, S, f, charset)
        if isRight(): break
        counter = raw_input("Can you give a counter example?")
        for i in range(len(counter)):
            word = counter[:i+1]
            if word not in R:
                add_item(word, R, S, f, charset)

if __name__ == "__main__":
    main()
