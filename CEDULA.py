nc1 = int(input(" leer el primer digito de la cedula: "))
nc2 = int(input(" leer el primer digito de la cedula: "))
nc3 = int(input(" leer el primer digito de la cedula: "))
nc4 = int(input(" leer el primer digito de la cedula: "))
nc5 = int(input(" leer el primer digito de la cedula: "))
nc6 = int(input(" leer el primer digito de la cedula: "))
nc7 = int(input(" leer el primer digito de la cedula: "))
nc8 = int(input(" leer el primer digito de la cedula: "))
nc9 = int(input(" leer el primer digito de la cedula: "))
nc10 = int(input(" leer el primer digito de la cedula: "))
a = nc1 * 2
if a > 9:
   a = a - 9


b = nc3 * 2
if b > 9:
   b = b - 9


c = nc5 * 2
if c > 9:
   c = c - 9


d = nc7 * 2
if d > 9:
   d = d - 9


e = nc9 * 2
if e > 9:
   e = e - 9
#suma de numeros impares:
impares = (a + b + c + d + e)

#suma de pares
pares = (nc2 + nc4 + nc6 + nc8)

#suma de pares e impares
total = (pares + impares)
print(" total: ", total)

if total <= 10:
 total = total - 10
 print(" ultimo digito de ceudula: ", total)

elif total < 20 and total > 10:
 total = total - 20
 print(" ultimo digito de ceudula: ", total)

elif total < 30 and total > 20:
 total = total - 30
 print(" ultimo digito de ceudula: ", total)

elif total < 40 and total > 30:
 total = total - 40
 print(" ultimo digito de ceudula: ", total)

elif total < 50 and total > 40:
 total = total - 50
 print(" ultimo digito de ceudula: ", total)

elif total < 60 and total > 50:
 total = total - 60
 print(" ultimo digito de ceudula: ", total)

elif total < 70 and total > 60:
 total = total - 70
 print(" ultimo digito de ceudula: ", total)

elif total < 80 and total > 70:
 total = total - 80
 print(" ultimo digito de ceudula: ", total)

elif total < 90 and total > 80:
 total = total - 90
 print(" ultimo digito de ceudula: ", total)





