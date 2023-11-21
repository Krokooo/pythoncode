# print("zadanie 1")
i=1
while i<101:
    print("To jest efekt petli while")
    i+=1
# print("zadanie 2")
i=254
while 320>i:
    if i%2==1 and i%5==0:
     print(i)
    i+=1
# print("zadanie 3")
while True:
    firstnumber = int(input("podaj liczbe"))
    if firstnumber%12==0:
     print("podales liczbe podzielna przez 12,wiec koncze dzialanie petli ")
     break
# print("zadanie 4")
count=0
sum=0
while True:
    secondnumber = int(input("podaj liczbe"))
    count=count+1
    total=secondnumber+sum
    sum+=secondnumber
    print(total/count)
    if secondnumber==0:
        break
# print("zadanie 5")
count=0
sum=0
while True:
    nextnumber = int(input("podaj liczbe"))
    count = count + 1
    total = nextnumber + sum
    sum += nextnumber
    average = total/count
    print(nextnumber)
    if total==100 or average==66:
        break
# print("zadanie 6")
count=0
perfectnumber= int(input("Podaj number"))
for i in range(1,perfectnumber):
 if perfectnumber%i==0:
     count+=i
if perfectnumber == count:
 print("liczba jest doskonala")
else:
 print("liczba nie jest doskonala")
# print("zadanie 7")
number=int(input("podaj numer"))
for i in range(2,number):
    if number % i == 0:
     print("liczba nie jest liczba pierwsza")
     break
    elif number%number==0 and number%1==0:
     print("liczba jest liczba pierwsza")
     break
# print("zadanie 8")
totalrent =0
for i in range(1,13):
    totalrent+=333
    totalrent*=1.08
    print(totalrent)
# print("zadanie 9")
sum=0
storednumber=None
while True:
    try:
     anothernumber=int(input("Podaj liczbe"))
     sum += anothernumber
    except ValueError:
     break
    if storednumber is not None and abs(anothernumber-storednumber )<= 5 :
        print(sum)
        break
    storednumber=anothernumber
# print("zadanie 10")
sum=0
previousnumber=None
while True:
    try:
        secondanothernumber=int(input("podaj liczbe"))
        sum+= secondanothernumber
        print(sum)
    except ValueError:
        break
    if previousnumber is not None and previousnumber==secondanothernumber:
        break
    previousnumber =secondanothernumber

