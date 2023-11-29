# pythagoras

from math import pow, sqrt

def calc_hypotenuse(a, b):
    c = sqrt(pow(a, 2) + pow(b, 2))
    return c

print("{:.2f}".format(calc_hypotenuse(10, 20)))


# schrikkel

def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

print(is_leap_year(1900))  
print(is_leap_year(1996))
print(is_leap_year(2000))


# integraal

def benader_integraal(a, b, f, n):
    delta = (b - a) / n
    opp = 0
    for i in range(1, n + 1):
        xi = a + (i - 0.5) * delta
        opp += f(xi) * delta
        
    return opp

ff = lambda x : x * x
print(benader_integraal(-3, 3, ff, 10))


# decorator

def check_type(func):
    def execute(getal):
        if type(getal) is int:
            return func(getal)
        else:
            print("Onjuist type argument")
            return None
    return execute
    
@check_type  
def verdubbelen(getal):
    return 2 * getal

print(verdubbelen(16))
print(verdubbelen("zestien"))


# mph

from afstand import mile_to_km as mijls_km

def mph_naar_ms(mph):
    kph = mijls_km(mph)
    return 1000 * kph / 3600

print(mph_naar_ms(10))


# kapper

import re

tekst = "Kapper Knap, de knappe kapper, knipt en kapt heel knap, maar de knecht van kapper Knap, de knappe kapper, knipt en kapt nog knapper dan kapper Knap, de knappe kapper."

words = re.split("[ ,]", tekst);
print(words)
knaps = [w for w in words if "knap" == w.lower()]
print(knaps)
print(len(knaps))

# bke

board = [["O", "X", "O"], ["X", "O", "X"], ["X", "X", "O"]]

def check_winner(board):
    winner = None
    
    # horizontal
    for r in board:
        if r[0] == r[1] and r[1] == r[2]:
            winner = r[0]
            
    # columns
    for ci in range(len(board)):
        if board[0][ci] == board[1][ci] and board[1][ci] == board[2][ci]:
            winner = board[0][ci]
    
    # diagonals
            
    if winner is None:
        print("No winner found...")
    else:
        print("Winner is", winner)

check_winner(board)


# dict verwissel 1

d1 = { 'Piet': 100, 'Jan' : 101, 'Klaas' : 102 }

def verwissel_in_dict(dict):
    d2 = {}
    for key, value in dict.items():
        d2[value] = key
    return d2
        
print(verwissel_in_dict(d1))


# dict wissel 2

schoenmaten = { 'Adam' : 44, 'Bram' : 43, 'Cas' : 42, 'Daan' : 45, 'Elias' : 42, 'Floris' : 43, 'Gijs' : 44, 'Hugo' : 40, 'Ivan' : 42, 'Jesse' : 42}

def verwissel_in_dict(d):
    d2 = {}
    for key, value in d.items():
        d2.setdefault(value, []).append(key)
    return dict(sorted(d2.items()))
        
print(verwissel_in_dict(schoenmaten))


# tdd

import doctest

def calc_magic(x):
    """
    >>> calc_magic(123)
    124
    """
    return x + 1

doctest.testmod()


# 7: add vectors

import doctest

def add_vectors(u, v):
    '''
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
    '''
    
    # with list comprehension
    return [u[i] + v[i] for i in range(len(u))]
    
doctest.testmod()


# 8: scalar mult

import doctest

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    
    # with list comprehension
    return [s * v[i] for i in range(len(v))]

doctest.testmod()


# 9: dot product

import doctest

def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    
    return sum([i*j for i,j in zip(u, v)])

doctest.testmod()