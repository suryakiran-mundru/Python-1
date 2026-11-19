#recorsion 1to 10
'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)
'''


#recorsion 10 to 1
'''
def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)
'''
#before recorsion and after recorsion

'''
def display(n):
    if n==len(s):
        print()
        return
    print(s[n],end='')
    display(n+1)
    print(s[n],end='')
s='python programming'
display(0)
'''


#To print 0 to n in a increasing order 
#p=s[:1].  p
#p=s[:2].  py
# "  [:3]. pyt.......

'''
def display(n):
    if n==len(s):
        return
    print(s[:n+1])
    display(n+1)
s='python programming'
display(0) 
'''


#To print the output
#cod
#ode
#deg
#egn
#gna
#nan

'''
def display(n,w):
    if n>len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)
s='codegnan'
display(0,3)
'''

#Sum of n numbers
'''def display(n):
    if n < 1:
        return 0
    return n +display(n-1)
print(display(10))
'''
#factorial *
'''
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)
print(factorial(6))
'''
