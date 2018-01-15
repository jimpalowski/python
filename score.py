def letterGrade(score):
    '''int -> string
 
    Return a letter grade when given an exam score provided by the user.
 
    >>> letterGrade(2)
    'D'
    >>> letterGrade(3)
    'C'
    >>> letterGrade(4)
    'B'
    >>> letterGrade(5)
    'A'
    '''
 
    if score == 5:
        letter = 'A'
    elif score == 4:
        letter = 'B'
    elif score == 3:
        letter = 'C'
    elif score == 2:
        letter = 'D'
    else:
        letter = 'F'
    return letter
 
def main():
    x = input('Enter a numerical grade: ')
    letter = letterGrade(x)
    print 'Your grade is %s.' % letter
main()
 
