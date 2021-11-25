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
  a = int(input("ievadi  a malas garumu: "))
h = int(input("ievadi vērtību h: "))
S= a * h / 2
print(S)

elif a=="Tr":
  print('Trapece')
  
elif a=="P":
  print('paralelograms')
elif a=="Ta":
  print('taisnstūris')
elif a=="K":
  print('kvadrāts')
elif a=="R":
  print('riņķis')
