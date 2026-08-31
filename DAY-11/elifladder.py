#elif is used when there are multiple conditions
budget=int(input("Enter your budget:"))

if budget>10000:
    print("Trip")
elif budget>5000:
    print("Resort stay")
elif budget>3000:
    print("Movie and dinner")
elif budget>1000:
    print("Cafe and shopping")
elif budget>500:
    print("Street and park view")
else:
    print("Stay home")


hr = int(input('enter the time:'))

if 5<=hr<=11:
    print('Good morning')
elif 12<=hr<=16:
    print('Good afternoon')
elif 17<=hr<=20:
    print('good evening')
elif 21<=hr<24:
    print('good night')
else:
    print('midnight sleep well')



budget = int(input('enter your budget:'))
if budget>10000:
    print('Cloud hosting')
elif budget>5000:
    print('Business hosting')
elif budget>2000:
    print('premium hosting')
else:
    print()
