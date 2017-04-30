import random

a = [[random.random() for row in range(1000)]for col in range(1000)]
b = [[random.random() for row in range(1000)]for col in range(1000)]

c = [ok for ok in range(1, 76)]
g = ['B', 'I', 'N', 'G', 'O']
u = ['(0-15)', '(16-30)', '(31-45)', '(46-60)', '(61-75)']
r, q, r1, q1 = 0, 0, 0, 0

n1 = ''
n2 = ''

n, m = 0, 15
for i in range(5):
    d = []
    for j in range(5):
        for k in range(n,m):
            d.append(c[k])
            
        z = random.choice(d)
        a[i][j] = z
                
    n += 15
    m += 15

n, m = 0, 15
for i in range(5):
    d = []
    for j in range(5):
        for k in range(n,m):
            d.append(c[k])
            
        z = random.choice(d)
        b[i][j] = z
                
    n += 15
    m += 15

def bingo(a, b, n1, n2):    
    print
    print 'Board 1 :', n1
    for i in range(5):
        print u[i],
    print
    for i in range(5):
        print g[i], '\t',
    print
    print '-' * 35,
    print
        
    for i in range(5):
        for j in range(5):
            print a[j][i], '\t',
        print
        
    print
    print 'Board 2 :', n2
    for i in range(5):
        print u[i],
    print
    for i in range(5):
        print g[i], '\t',
    print
    print '-' * 35,
    print
        
    for i in range(5):
        for j in range(5):
            print b[j][i], '\t',
        print

'''print 'How to play?(Instructions)'
print '1) This is totally based on your luck and no skill is required to play this game'
print '2) There will be 2 boards given and you have to choose if you want to play 2 player or 1 player(against computer)'
print '3) The first one to complete 4 corners or quick 7 wins'
print '4) The computer will generate random numbers between 1-75'
print '5) If the number is there in any of the boards then only they will be shown'
print '6) If the number is not present in any of the boards then the boards will not be shown'
print '7) Hit enter to generate a number'
print'''
print 'Game mode:'
print '1) 1 player'
print '2) 2 player'
ans = raw_input('>>>')
print
if ans == '1':
    n1 = raw_input('Player 1:')
    n2 = 'Computer'
else:
    n1 = raw_input('Player 1:')
    n2 = raw_input('Player 2:')
    
bingo(a, b, n1, n2)

for h in range(25):
    print
    t = raw_input('Hit ENTER to generate a new number')
    s = random.choice(c)
    print
    print 'The number is',s
    y = 0
    for i in range(5):
        for j in range(5):
            #if a[j][i] == s or b[j][i] == s:
            if a[j][i] == s:
                a[j][i] = 'X'
                y += 1
                r1 += 1
            if b[j][i] == s:
                b[j][i] = 'X'
                y += 1
                q1 += 1
            if j in [0, 4] and i in [0, 4]:
                if a[j][i] == 'X':
                    r += 1
                if b[j][i] == 'X':
                    q += 1
            
                
    if y in [1, 2, 3, 4]:
        bingo(a, b, n1, n2)
              
    if r == 4 or r1 == 7:
        print n1, 'wins'
        break
    elif q == 4 or q1 == 7:
        print n2, 'wins'
        break
    
print
print 'Thank you for playing'



