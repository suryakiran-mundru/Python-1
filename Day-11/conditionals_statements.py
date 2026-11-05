'''
data = ('admin@gmail.com','admin@123')

gmail = input("Enter your gmail: ")
password = input("Enter your password: ")

if (gmail,password) == data:
    print("Login successful")
else:
    print("Invalid login credentials")
    '''

'''
seats={
    's1':'Booked',
    's2':'Available',
    's3':'Booked',
    's4':'Available',   
    's5':'Available',
    's6':'Booked',
}
seatno = input("Enter your seat number: ")
if seatno in seats and seats[seatno] == 'Available':
    seats[seatno] = 'Booked'
    print(f'{seatno}is Available for booking')
else:
    print(f'{seatno} is not available for booking')
'''
'''
products = {
    'laptop': {'price': 50000, 'stock': 10},
    'mobile': {'price': 20000, 'stock': 0},
    'headphones': {'price': 2000, 'stock': 5},
}
search = input("Enter the product name: ")
if search in products and products[search]['stock'] > 0:
    print(f"you can buy{search}at this price{products[search]['price']}")
else:
    print(f"{search} is not available for purchase")
    '''
'''
print("Welcome to the weekend planner!")
budget =int (input("Enter your budget for the weekend: "))

if budget > 10000:
    print("Trip")
elif budget > 5000:
        print("Resort")
elif budget > 2000:
        print("Movie")
elif budget > 1000:
        print("Dinner")
elif budget > 500:
        print("cafe")
else:
        print("Stay home and relax")
        '''
'''
data = {
    'surya':{'status':True,'python':96,'mysql':95,'fastapi':93},
    'raghu':{'status':True,'python':86,'mysql':75,'fastapi':83},
    'chandra':{'status':True,'python':77,'mysql':65,'fastapi':63},
     'sowmya':{'status':True,'python':57,'mysql':51,'fastapi':93},
      'kiran':{'status':True,'python':37,'mysql':25,'fastapi':13},
      'tulasi':{'status':False,'python':None,'mysql':None,'fastapi':None}
}
name = input("Enter your name: ")
if name in data:
    if data[name]['status']:
        if data[name]['status']:
            total = data[name]['python'] + data[name]['mysql'] + data[name]['fastapi']
            average = total / 3
            if average >= 75:
                print(f"{name},congrates you gor the first grade")
            elif average >= 60:
                print(f"{name},Good job ")
            elif average >= 50:
                print(f"{name}, You need to work hard")
            elif average < 50:
                print(f"{name},works hard and try to improve your skills")
            else:
                    print(f"{name}, you failed the exam. Bring your parents")
        else:
            print(f"{name}, didn't attend the exam. Bring your parents")
    else:
        print(f"{name}, is not found in the database")
    '''

                 

    