#ejercicio1
nota1 = 4
nota2 = 8
nota3 = 6
nota4 = 7
nota5 = 5
media = (nota1+nota2+nota3+nota4+nota5)/5
print('La nota media es',media,)
#ejercicio2
operación = (365 / 12) * 14.7
print('El resultado de la operación es',"{:.2f}".format(operación),)
#ejercicio3
username = input("escriba su nombre de usuario:")
password = input("escriba su contraseña:")

if username:
 A = 3 <= len(username) < 10
else:
  A = False
if password:
 B = password == "Tokio" or password =="Python"
else:
 B = False

print(f"{A}")
print(f"{B}")
#ejercicio4
num1= 1
num2= 2
print(num1+1)
print(num2-2)
print(num1*3)
nuevonum1= 3
print(num2*2)
nuevonum2= 4