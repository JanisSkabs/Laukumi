x=0
print('Programa pieprasa figūras elementus un aprēķina to laukumu')
print('Nospied burtu: ')
print('T - Ja figūra ir trīstūris')
print('Tr - Ja figūra ir trapece')
print('P - Ja figūra ir paralelograms')
print('Ta - Ja figūra ir taisnstūris')
print('K - Ja figūra ir kvadrāts')
print('R - Ja figūra ir riņķis')
print('____________________________________________________________________________')

a=input('Ievadi burtu: ')
if a=="T":
  print('Trīstūris')
  a = int(input("ievadi  a malas garumu metros: "))
  h = int(input("ievadi vērtību h metros: "))
  S= a * h / 2
  print(S,'m2')
elif a=="Tr":
  print('Trapece')
  k = int(input("ievadi   1.malas garumu: "))
  j = int(input("ievadi 2. malas garumu: "))
  u = int(input("Ievadi augstuma garumu:"))
  S= (k+j)*u/2
  print(S)
elif a=="P":
  print('paralelograms')
  n = int(input("ievadi  1. malas garumu: "))
  e = int(input("ievadi augstuma vērtību: "))
  S= n*e
  print(S)
elif a=="Ta":
  print('taisnstūris')
  w = int(input("ievadi   1.malas garumu: "))
  e = int(input("ievadi 2. malas garumu: "))
  S= w*e
  print(S)
elif a=="K":
  print('kvadrāts')
  l = int(input("ievadi   malas garumu: "))
  S= l*l
  print(S)

elif a=="R":
  print('riņķis')
  R = float(input("ievadi   rādiusu: "))
  S= R*R*3.14
  print(S)
