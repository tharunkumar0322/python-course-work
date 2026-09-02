i=1
while i<=10:
    print(i)
    i+=1

i =10
while i>0:
    print(i)
    i-=1
    
i=5
while i<=50:
    print(i)
    i+=5
  
s='while loop'
i =0
while i<len(s):
    print(s[i])
    i+=1

s = "pyhton"
i=len(s)-1
while i>=0:
    print(s[i])
    i-=1

    
l=[1,2,3,4,5]
i=0
while i<len(l):
    print(l[i])
    i+=1

#reverse
n = 8765
while n>0:
    print(n%10)
    n//=10

#sumofdigits
n=1234
s=0
while n>0:
    s+= n%10
    n//=10
print(s)

#product
n =1234
p=1
while n>0:
    p*=n%10
    n//=10
print(p)

n=34567
res=0
while n > 0:
    rem=n % 10
    if rem %2 ==0 :
        res += rem
    n//=10
print(res)

n = [7,9,23,0,0,0,12,0,34,0,0,13,31,0,0,]
while 0 in n:
    n.remove(0)
print(n)

l = [12,32,4,3,12,4,23,53,65,52,65]
i=0
j=len(l)-1
while i <= j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j+=1
    