# -*- coding: utf-8 -*-
"""
Exercises 2
"""
###############
##A. donuts

def donuts(count):
    if count < 10:
        return 'Number of donuts: %d' %(count)
    else: return 'Number of donuts: many'

###############
##B. both_ends

def both_ends(s):
    if len(s) > 2:
        return s[0]+s[1]+s[-2]+s[-1]
    else: return ''

###############
##C. fix_start

def fix_start(s):
    return s[0] + s.replace(s[0],'*')[1:]

###############
##D. MixUp

def mix_up(a,b):
    return b[0:2]+a[2:]+' '+a[0:2]+b[2:]

##TESTS

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

main()

###############
##D. verbing

def verbing(s):
    if len(s) > 2:
        if s[-3:] == 'ing':
            return (s + 'ly')
        else:
            return (s + 'ing')
    else:
        return s

###############
##E. not_bad

def not_bad(s):
    if s.find('not') < s.find('bad'):    
        return s.replace(s[s.find('not'):s.find('bad')+3], 'good')
    else:
        return s

###############
##F. front_back

def front_back(a,b):
    half_a = len(a)//2+len(a)%2
    half_b = len(b)//2+len(b)%2
    return a[0:half_a] + b[0:half_b] + a[half_a:] + b[half_b:]

##TESTS
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

main()


