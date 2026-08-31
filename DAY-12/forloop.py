'''
syntax
for var in seq:
    #stmts
'''

s='python programming'
for i in s:
    print(i)

l=[1,2,3,4]
for num in l:
    print(num)

prices=(123,321,673,987)
for price in prices:
    print(price)

names=['john','james','jack','jill']
for name in names:
    print(name) 

d={'a':1,'b':2,'c':3}
for key in d:
    print(key,d[key])


# range(start,stop+1,step)
# it used to generate a sequence of numbers
 
for i in range(1,11):
    print(i)  

for i in range(1,11,2):
    print(i) 

for i in range(2,11,2):
    print(i)    
    
for i in range(4,101,4):
    print(i) 


#index printing
s="python programming"
for i in range(len(s)):
    print(i,s[i])

s=(123,321,673,987 )
for i in range(len(s)):
    print(i,s[i])

s=(123,321,673,987 )
for i in enumerate(s):
    print(i)

s=(123,321,673,987 )
for i in enumerate(s):
    print(i[0],i[1])

d={'a':1,'b':2,'c':3}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])



#break,continue

for i in range(1,11):
    if i==7:
        break
    print(i)

for i in range(1,11):
    if i==7:
       continue
    print(i)

for i in range(1,11):
    if i==17:
        break
    print(i)
else:
    print("loop completed")
   
l=[1,2,3,4,5]
n=10
for i in l:
    if i==n:
        print(n,"found")
        break
else:
    print(n,"not found")

pin=1234
for i in range(5):
    epin=int(input("enter pin:"))
    if epin==pin:
        print("phone unlocked")
        break
    else:
        print("invalid pin")
else:
    print("try after 24 hours")




n=115
for i in range(2,n//2+1):
    if n%i==0:
        print(n,"not prime")
        break 
else:
    print(n,"is prime")
