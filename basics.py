# zadania są zrobione na wersji pythona 3.10
print("zadanie 1")
firstnumber = int(input("first number"))
secondnumber = int(input("second number"))
print(firstnumber+secondnumber)
print(firstnumber-secondnumber)
print(firstnumber*secondnumber)
if secondnumber != 0:
    print(firstnumber/secondnumber)
else:
    print("no result")
print("zadanie 2")
print(1 % 2, 69 % 2, 666 % 2, 1000 % 2, 4 % 2)
print("zadanie 3")
lightyear = 300000
lighttime = 1*60*60*24*365.25
lightinkilo = lightyear*lighttime
print("rok swietlny podany w kilometrach:", lightinkilo)
print("rok swietlny podany jako czas:", lighttime)
print("zadanie 4")
minute = 60
hour = minute*minute
day = hour*24
year = day*365
life = (20*year)+day*54
print(hour, day, year, life)
print("zadanie 5")
cm = 2.54
inch = int(input("liczba cali"))
converter = cm*inch
print("cale na cm", converter)
print("zadanie 6")
displacementinkm = 30
displacement = displacementinkm*1000
time = 15.0
velocity = ((displacement/time)/60)
convert = (velocity*(0.001*3600))
displacementinkm2 = 30
displacement2 = displacementinkm2*1000
time2 = 12.0
velocity2 = ((displacement2/time2)/60)
convert2 = (velocity2*(0.001*3600))
print("pierwsza predkosc")
print(convert)
print("druga predkosc")
print(convert2)
print("srednia predkosc")
print((convert*displacementinkm+convert2*displacementinkm2)/(displacementinkm+displacementinkm2))
