''' Author: @anuskrishnav
Problem : https://www.hackerrank.com/challenges/the-minion-game/problem
'''
def minion_game(string):
    vowelsli =['A','E','I','O','U']
    STUART, KEVIN=0, 0
    for i in range(len(string)):
        if string[i] in vowelsli:
            KEVIN+= len(string)-i
        else:
            STUART+=len(string)-i
    if STUART>KEVIN:
        print("Stuart"+" "+ "%d" % STUART)
    elif KEVIN>STUART:
        print("Kevin"+" "+'%d' % KEVIN)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)