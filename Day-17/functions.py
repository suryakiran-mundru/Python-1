#to print multiple times
'''def numbers():
    for i in range(1,11):
        print(i)


numbers()
numbers()
numbers()
numbers()'''

#prime numbers

'''def factors(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        print("Not Prime Numbers")
    else:
        print("prime numbers")
factors(int(input("enter the numbers:")))            

'''

#
'''def isprime(n):
    for i in range(n,n+1):
        if n%i==0:
            return "Not a prime number"
    return "prime number"
    print(isprime(int(input("Enter the Number:"))))'''




'''def sumofdigs(n):
   sum =0 
   while n>0:
      sum+= n%10
      n//=10
      return sum
print(sumofdigs(34567))
print(sumofdigs(12345))   '''


'''
def revs(n):
    sum =0
    while n>0:
        sum = (sum*10)+n%10
        n//=10
    return sum 
print(revs(34567))
print(revs(12345))    
      '''



'''
def display(name,email,password):
    print("name",name)
    print("email",email)
    print("password",password)
display("surya","suryakiran@gmail.com","1234") 
display("suryakiran@gmail.com","surya","1234")
display("1234","surya","suryakiran@gmail.com")
'''
#key word arguments
'''
def display(name,email,password):
    print("name",name)
    print("email",email)
    print("password",password)
display(name="surya",email="suryakiran@gmail.com",password="1234") 
display(email="suryakiran@gmail.com",name="surya",password="1234")
display(password="1234",name="surya",email="suryakiran@gmail.com")
'''
#default arugument

'''
def display(name,email,password,phNo=None):
    print("name",name)
    print("email",email)
    print("password",password)
    print("phNo",phNo)
display("surya","suryakiran@gmail.com","1234")
display("suryakiran@gmail.com","surya","1234",9848472789)
'''

#
'''def display(*n):
    print(n)

display(1,2,3,4,) 
display(1,2,3) 
display(1,2,3,4,5,6)  '''


#
'''def display(**n):
    print(n)

display(n1=1,n2=2,n3=3,n4=4,) 
display(n1=1,n2=2,n3=3) 
display(n1=1,n2=2,n3=3,n4=4,n5=5,n6=6)'''


#higestmark
'''
def highestmark(data):
    res, marks = max(data.items(), key=lambda item: item[1])
    print(f"Highest marks {res}:{marks}")
data={}

for i in range(3):
    name=input("enter the name:")
    marks=int(input("enter the markes:"))
    data[name]=marks
highestmark(data)
'''

