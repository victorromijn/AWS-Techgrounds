import random #de module random geeft verschillende functie die willekeur oplevert

flag = True #flag is een boolean in een situatie
while flag:
  nummer=input('Geef me een getal tussen de 1 en 100 om het spel mee te spelen: ')

  if nummer.isdigit():
    print('Laten we het spel spelen!')
    nummer= int(nummer)
    flag=False
  else:
    print('onjuiste invoer, probeer het nog een keer!')

secret = random.randint(1,nummer)

raden = None
tellen = 1

while raden !=secret:
  raden=input('raad het getal tussen de 1 en '+str(nummer)+ ": ")
  if raden.isdigit():
    raden= int(raden)

  if raden ==secret:
    print('Goed geraden!')
  else:
    print('probeer het nog een keer')
    tellen +=1

print('je hebt er', tellen, 'keer over gedaan! ')