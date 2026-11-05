'''
pin = int(input("Set the pin: "))

for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("login Succesfully")
        break
    else:
        print("Invalid pin")   

else:
    print("maximum attempts reached! try after 30 seconds")
    '''
'''
l=[2,4,6,7,24,90,24,45,34,56,40]
search=int(input("Enter the number: "))

for i in range(len(l)):
    if l[i]==search:
        print(f"{search} is found at index {i}")
        break
else:
    print(f"{search} is not found ")
    '''
'''
c={1,2,3,4,5,567,58}
for i in enumerate(c):
    print(i[0], i[1])
'''
'''
c={"k1":"v1","k2":"v2","k3":"v3"}
for i in c.items():
    print(i[0], i[1],c[i[0]])
'''