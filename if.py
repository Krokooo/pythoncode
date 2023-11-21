# zadania są zrobione na wersji pythona 3.10
print("zadanie 1")
firstnumber = int(input("Podaj liczbe a"))
secondnumber = int(input("Podaj liczbe b"))
thirdnumber = int(input("Podaj liczba c"))
fourthnumber = int(input("podaj liczbe d"))
if firstnumber % secondnumber != 0:
    print("liczba a nie jest podzielna przez b")
else:
    print("liczba  jest podzielna")
print("zadanie 2")
if firstnumber <= 10:
    print("pierwszy komunikat")
elif 25 >= firstnumber > 10:
    print("inny komunikat")
elif 25 < firstnumber:
    print("kolejny inny komunikat")
print("zadanie 3")
if firstnumber > thirdnumber and firstnumber > secondnumber:
    print("a jest wieksze od b i c")
elif firstnumber < secondnumber and thirdnumber < secondnumber:
    print("b jest wieksze od a i c ")
elif firstnumber < thirdnumber and secondnumber < thirdnumber:
    print("c jest wieksze od a i b")
elif firstnumber == secondnumber == thirdnumber:
    print("a ,b i c sa rowne")
elif firstnumber == secondnumber:
    print("a i b sa rowne")
elif firstnumber == thirdnumber:
    print("a i c sa rowne")
elif secondnumber == thirdnumber:
    print("b i c sa rowne")
print("zadanie 4")
if firstnumber < 0 and firstnumber % 2 != 0:
    print("liczba jest ujemna i jest podzielna z reszta")
elif firstnumber < 0 and firstnumber % 2 == 0:
    print("liczba jest ujemna ale nie jest podzielna z reszta")
elif firstnumber >= 0 and firstnumber % 2 != 0:
    print("liczba jest dodatnia i podzielna z reszta")
elif firstnumber > 0 and firstnumber % 2 == 0:
    print("liczba jest dodatnia i nie jest podzielna z reszta")
print("zadanie 5")
stateofintoxication = 0.1
stateafteralcoholconsumption = 0.05
exhaledair = float(input("Podaj wartosc wydychanego powietrza mg/l"))
if exhaledair >= stateofintoxication:
    print("stan nietrzeźwości")
elif exhaledair >= stateafteralcoholconsumption:
    print("stan po spożyciu alkoholu")
else:
    print("stan trzeźwości")
print("zadanie 6")
if firstnumber > secondnumber and firstnumber > thirdnumber and firstnumber > fourthnumber:
    print("a jest najwieksza", firstnumber)
elif secondnumber > firstnumber and secondnumber > thirdnumber and secondnumber > fourthnumber:
    print("b jest najwieksza", secondnumber)
elif thirdnumber > firstnumber and thirdnumber > secondnumber and thirdnumber > fourthnumber:
    print("c jest najwieksza", thirdnumber)
elif fourthnumber > firstnumber and fourthnumber > secondnumber and fourthnumber > thirdnumber:
    print("d jest najwieksze", fourthnumber)
elif fourthnumber == firstnumber == secondnumber == thirdnumber:
    print("a,b,c i d sa rowne")
elif firstnumber == secondnumber == thirdnumber:
    print("a,b i c sa rowne")
elif firstnumber == thirdnumber == fourthnumber:
    print("a,c i d sa rowne")
elif firstnumber == secondnumber == fourthnumber:
    print("a,b i d sa rowne")
elif secondnumber == thirdnumber == fourthnumber:
    print("b,c i d sa rowne")
elif fourthnumber == firstnumber:
    print("a i d sa rowne i sa najwieksze")
elif fourthnumber == thirdnumber:
    print("c i d sa rowne i sa najwieksze")
elif fourthnumber == secondnumber:
    print("b i d sa rowne i sa najwieksze")
elif thirdnumber == firstnumber:
    print("a i c sa rowne i sa najwieksze")
elif thirdnumber == secondnumber:
    print("b i c sa najwieksze")
elif secondnumber == firstnumber:
    print(" a i b sa rowne")
print("zadanie 7")
arg_a = int(input("Podaj liczbe a"))
arg_b = int(input("Podaj liczbe b"))
arg_c = int(input("Podaj liczbe c"))
delta = (arg_b*arg_b)-4*arg_a*arg_c
deltasquareroot = delta**0.5
firstxarg = (-arg_b-deltasquareroot)/(2*arg_a)
secondxarg = (-arg_b+deltasquareroot)/(2*arg_a)
if delta < 0:
    print("nie ma rozwiazania")
elif delta == 0:
    print(firstxarg)
else:
    print(firstxarg, secondxarg)
print("zadanie 8")
firsttriangleside = int(input("podaj bok trojkata a"))
secondtriangleside = int(input("podaj bok trojkata b"))
thirdtriangleside = int(input("podaj bok trojkata c"))
if firsttriangleside**2+secondtriangleside**2 == thirdtriangleside**2:
    print("trojkat jest prostokatny")
else:
    print("trojkat nie jest prostokatny")
