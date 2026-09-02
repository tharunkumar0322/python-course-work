data = {
    'milk':30,
    'curd':60,
    'bread':45,
    'salt':21,
    'sugar':70,
    'oil':150,
    'chilli powder':60}
for i in data:
    print(i.ljust(20),data[i])
p = input("Enter the products:").split()
print("----------Bill----------")
bill = 0
for i in p:
    print(i.ljust(20),data[i])
    bill += data[i]
print("Total bill:".ljust(20), bill)


