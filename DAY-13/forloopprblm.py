#program to find factors of a number
n=int(input("Enter the input:"))
res = []
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(f'Factors of {n}={res}')


#frequency count in dictionary
s= "python programming"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


# a6b6c4d9b5s6
s='aaaaaabbbbbbccccdddddddddbbbbbssssss'
c = 1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))