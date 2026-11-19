#local scop that will acces only inside 
#globle scop that will access any where and we should not 
#nonlocal is when need only outside function
#build scop


#global
'''def display():
    global n
    n=10
    print("inside:",n)

display()
print("outside:",n)'''

#nonlocal
'''
def display():
    course ="JFS"
    print("Starting:",course)
    def update():
        nonlocal course
        course ="PFS"
        print("update:",course)
    update()
    print("final:",course) 

display()  
 '''
# build scope
'''s="codegnan"

print(max(s))

'''