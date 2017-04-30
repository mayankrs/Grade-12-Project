import random
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

z, c, e, y = 0, 0, 0, 0
a, b, d, x, g, u = '', [], ' ', '_', '', ' '

words = ['python','computer','dictionary','monitor','keyboard','television']

while True:
    secret = random.choice(words)
    l = len(secret)
    w = ['Wrong letters:']
    
    for i in range(l):
        if i == 2 or i == 5:
            a = a + secret[i]          
        else:
            a = a + '_ '
    print a
        
    while c < 7:
        let = raw_input('Enter a letter:')
        if let in secret:
            e += 1
            if e == 1:
                for i in range(l):
                    if i == 2 or i == 5 or secret[i] == let:
                        b.append(secret[i])
                    else:
                        b.append(x)
            else:
                for i in range(l):
                    if i == 2 or i == 5 or secret[i] == let:
                        b[i] = secret[i]
                    else:
                        continue        
            f = d.join(b)
            print 
            print f
            f = g.join(b)

            if f == secret:
                break
            else:
                continue
        
                    
        else:
            if let in w:
                print 'This letter is already discarded'
            else:
                print hangman[c]
                c += 1
                w.append(let) 
                print u.join(w)            

    if c != 7:
        print
        print 'You WIN!!!'       
    else:
        print 'You LOSE'
        print 'The word was',secret




    

