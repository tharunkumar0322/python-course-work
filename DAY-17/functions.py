'''
syntax
def fuction_name(arg):
    #stsmt
    return(opt)
    
functionname(para)

'''

def gst(price):
    print("Original Price:",price)
    print("Final Price",price+price*0.18)
gst(2000)
gst(1000)
gst(120)


def table(n):
    print(f"{n}-Table")
    print("______________________")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
table(11)


def table(n):
    print(f"{n}-Table")
    print("______________________")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,21):
    table(i)


def isleap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return "Leap Year"
    else:
        return "Not a Leap Year"
print(isleap(2012))
print(isleap(2014))
print(isleap(2006))
print(isleap(2032))

def isprime(n):
    for i in range(2,n//2+1):
        if n% i==0:
            return "Not a Prime Number"
    return "Prime Number"

print(isprime(5))
print(isprime(13))
print(isprime(14))
print(isprime(16))


#positional arg

def display(name,email,pwd):
    print("name",name)
    print("email",email)
    print("pwd",pwd)

display('Tharun','tharun@gmail.com','tharun1234')
display('tharun1234','Tharun','tharun@gmail.com')
display('tharun1234','tharun@gmail.com','Tharun')


#Keyword arg
def display(name,email,pwd):
    print("name",name)
    print("email",email)
    print("pwd",pwd)

display(name='Tharun',email='tharun@gmail.com',pwd='tharun1234')
display(pwd='tharun1234',name='Tharun',email='tharun@gmail.com')
display(pwd='tharun1234',email='tharun@gmail.com',name='Tharun')



#Default arg  ---default arg should be last in the parameters list

def display(name,email,pwd=None):
    print("name",name)
    print("email",email)
    print("pwd",pwd)

display('Tharun','tharun@gmail.com',)
display(pwd='tharun1234',email='tharun@gmail.com',name='Tharun')



#Variable length

def display(*names):  #* displays in a tuple
    print(names)
display("Tharun")
display("Tharun","Nikhil")
display("Tharun","Nikhil","Bunny")
display("Tharun","Nikhil","Bunny","Prasad")



def display(**names): #** displays in a dict
    print(names)
display(n1="Tharun")
display(n1="Tharun",n2="Nikhil")
display(n1="Tharun",n2="Nikhil",n3="Bunny")
