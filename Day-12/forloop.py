'''
#str list tuple dict set range()

#for i in seq:
     #stmt

s='codegnan'
for i in s:
    print(i)        

a=input("Enter a word:")
for i in a:
    if i in 'aeiouAEIOU':
        print(i)   
'''   

'''
#list
l=[22,32,12,45,67,89]
for i in l:
    print(i)
a=list(map(int,input("Enter a list of numbers:").split()))
for i in a:
    if i%2==0:
        print(i)
        '''

'''
l=[22,32,12,45,67,89]
for i in l:
    print(i)
sumoftuple=0
a=list(map(int,input("Enter a list of numbers:").split()))
for i in a:
    sumoftuple+=i

print(f"Sum of the tuple:",sumoftuple)    
      
      '''   

'''
l=[22,32,12,45,67,89]
for i in l:
    print(i)

max=0
a=list(map(int,input("Enter a list of numbers:").split()))
for i in a:
    if i>max:
        max=i

print(f"print max of seat:",max)

'''
'''

marks={mysql:45,java:67,c:89,html:90}
for i in marks:
    print(i)

sum=0
marks=list(map(int,input("Enter a list of numbers:").split()))
for i in marks:
    sum+=marks[i]
print(f"Sum of the numbers:",sum)
print(f"total marks:",sum)
'''

'''

for i in range(1,11):
    print(i,end=" ")
for i in range(20,0,-2):
    print(i,end=" ")

for i in range(2,101,2):
    print(i,end=" ")
'''

'''
n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
    '''

'''
#rang

c ='codegnan'
for i in range(len(c)):
    print(c[i],i,end=" ")
'''
'''
sum=0
c=[12,34,45,10,78,43,80]
for i in range(len(c)):
    if c[i]%2==0:
        sum+=c[i]
    print(sum)
'''
'''
for i in range(1,11):
    if i ==5:
        break
        print(i)

for i in range(1,11):
    if i ==5:
        continue
    print(i)        
    '''
for i in range(1,10):
    pass

if True:
    pass
class Booking:
    pass

def fun():
    pass