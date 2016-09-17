# -*- coding: utf-8 -*-
"""
Exercises 1
"""
###############
##A. match_ends
#Given a list of strings, return the count of the number of strings where the 
#string length is 2 or more and the first and last chars of the string are the 
#same.

def match_ends(words):
    count = 0
    for str in words:
        if len(str) >= 2 and str[0] == str[-1]:
            count += 1
    return count

#test:
match_ends(['ubu', 'pour', 'ele', 'pas', 'aa', 'tot'])

###############
##B. front_x
#Given a list of strings, return a list with the strings in sorted order, 
#except group all the strings that begin with 'x' first.
#e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 
#'aardvark', 'apple', 'mix']

def front_x(words):
    list1 = []
    list2 = []
    for str in words:
        if str[0] == 'x':
            list1.append(str)
        else:
            list2.append(str)
    list = sorted(list1, key=str.lower) + sorted(list2, key=str.lower)
    return list
#test:
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])

###############
##C. sort_last
#Given a list of non-empty tuples, return a list sorted in increasing order by
#the last element in each tuple.

def sort_last(tuples):
    def last_el(t):
        return t[-1]   
    return sorted(tuples, key = last_el)
#test:
sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2), (1, 3, 4)])

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    
    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

main()

###############
##D. remove_adjacent
#Given a list of numbers, return a list where all adjacent == elements have 
#been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may 
#create a new list or modify the passed in list.

def remove_adjacent(nums):
    a = ''
    list = []
    for str in nums:
        if str = a:
            list.append(str)
        a = str      
    return list
#test
remove_adjacent([1, 2, 2, 2, 2, 3, 3, 4, 5, 6])

###############
##E. linear_merge
#Given two lists sorted in increasing order, create and return a merged list of
#all the elements in sorted order. You may modify the passed in lists. Ideally,
#the solution should work in "linear" time, making a single pass of both lists.

def linear_merge(list1, list2):
    return sorted(list1+list2)

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()


