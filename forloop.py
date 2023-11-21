import random
print("zadanie 1")
for i in range(1,100):
    if i%8==0:
        print(i)
print("zadanie 2")
number=int(input("Podaj liczbe"))
for i in range(number,0,-1):
    if i%6==0 and i%9==0:
        print(i)
print("zadanie 3")
for i in range (100,200):
    if i%2==1 and  i%3!=0:
        print(i)
print("zadanie 4")
for i in range (100,200):
    if i%2==0 and  i%5!=0 and i%6!=0 and i%11!=0:
        print(i)
print("zadanie 5")
number1=int(input("podaj silnie"))
factorial=1
if(number1>=0):
 for i in range(1,number1+1):
    factorial=factorial*i
 print(factorial)
else:
 print("nie istnieje")
print("zadanie 6")
for i in range(1,6):
    print("*"*i)
print("zadanie 7")
number2=int(input("liczba"))
for i in range(number2+1):
    print(2**i)
print()
print("zadanie 8")
for i in range(999,0,-1):
  if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
        print(i)
        break
print("zadanie 9")
for i in range (6):
 lotto = random.randint(1, 49)
 print(lotto)
print("zadanie 10")
for i in range (20):
 multimulti = random.randint(1, 80)
 print(multimulti)
print("zadanie 11")
for i in range (5):
 minilotto = random.randint(1, 42)
 print(minilotto)
print("zadanie 12")
orzel=0
reszka=0
rzuty = {0: "orzeł", 1: "reszka"}
for i in range(50):
     wynik=random.randint(0,1)
     print(rzuty[wynik])
     if wynik==0:
         orzel+=1
     elif wynik==1:
         reszka+=1
print("liczba orlow",orzel)
print("liczba reszek",reszka)