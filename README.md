# Funciones_3w_1182
Edgar Gael Garcia Camacho 3-W

# 1

def mi_funcion(fname):
    print(fname + " Refsnes")


mi_funcion("Pollos")

mi_funcion("Polleria")

mi_funcion("Pollitos")


![image](https://github.com/user-attachments/assets/338136c0-e780-46dd-8a6d-9fa92307aab1)

![image](https://github.com/user-attachments/assets/723e23a7-049b-4576-9215-3ad1de043c1f)

# 2

#Se crea una funcion para agregar dos valores.

def mi_funcion(fname,iname):

print(fname + iname)

#Loos dos valores que se agregan.

mi_funcion("Pollos"," Locos")

![image](https://github.com/user-attachments/assets/200df5ff-2d7c-480e-8f64-ad9d8680feb1)

![image](https://github.com/user-attachments/assets/577eb6f3-4a0e-4d47-9b80-ae3915f0af7b)

# 3


#SE crea una funcion para agregar dos valores pero solo se agrega uno.

def mi_funcion(fname,iname):

print(fname + "" + iname)

#Solo un valor agregado.

mi_funcion("Pollos","")

![image](https://github.com/user-attachments/assets/319fdf81-dfed-435f-a73d-b306301ced85)

![image](https://github.com/user-attachments/assets/70393379-714c-441e-aea4-8bae4c9f63c8)

# 4

#Se agraga una funcion para saber cual de los polleros es el menor.

def mi_funcion(*kid):

print("El menor de los polleros es :" + kid[2])

#Los nombvres de los polleros.

mi_funcion("Juan","Nicolas","Pedro")    

![image](https://github.com/user-attachments/assets/684c8f75-8d5d-4b98-ae8b-9c69e4a007ba)

![image](https://github.com/user-attachments/assets/6946e70f-b6eb-4726-85e2-03c9334e8376)

# 6

#Se agrega una funcion para saber el apellido para saber el apellido de un pollero.

def mi_funcion(**kid):

print("Mi apellido es :",kid["iname"])

#Se escribe el apellido del pollero.

mi_funcion(fname="Juan",iname="Pollero")

![image](https://github.com/user-attachments/assets/0b6b246a-e9b5-4fb5-9e70-50f2ad24a97f)

![image](https://github.com/user-attachments/assets/af9f1358-c835-4a2b-8627-4470fef92052)

# 7

def mi_funcion(pais = "México"):

print("La polleria se encuentra en :" + pais)


mi_funcion("Perú")

mi_funcion("Venezuela")

mi_funcion()

![image](https://github.com/user-attachments/assets/e08328f5-4a01-4925-ae0f-46a3a3a9eb30)

![image](https://github.com/user-attachments/assets/216347eb-848c-421d-b2a0-b1db6c2b600e)

# 8

def mi_funcion(Pollos):

for x in Pollos:

print(x)

Combos =["Combo 1: pollo Grande y Tortillas de harina.","Combo 2: pollo mediano y dos sodas.","Combo 3: pollo pequeño y un paquete de papas fritas."]

mi_funcion(Combos)

![image](https://github.com/user-attachments/assets/8bd817a0-4877-429f-a7d6-fed64d2816cb)

![image](https://github.com/user-attachments/assets/c876bbde-e702-4543-9fa1-5fb2463d8d6f)

# 9

def mi_funcion(x):

return 23 * x

print(mi_funcion(2))

print(mi_funcion(7))

print(mi_funcion(3))

![image](https://github.com/user-attachments/assets/4737b9a4-470b-4c51-86ec-516d4db693c4)

![image](https://github.com/user-attachments/assets/4b9548b2-6a6d-4a26-86b1-c1f78d528be6)

# 10

def mi_funcion(x,/):

print(x)

mi_funcion(3)

![image](https://github.com/user-attachments/assets/bbefc7b1-0e9d-4323-a3b2-01920720b4bd)

![image](https://github.com/user-attachments/assets/d6e124c7-a0fb-451e-99de-4f17486b541b)

# 11

#Se agrega una funcion para imprimir un numero.

def mi_funcion(x,/):

print(x)

#El numero que se va a imprimir.

mi_funcion(x=23)

#Da error
![image](https://github.com/user-attachments/assets/339af9a1-5f75-402b-b83f-53bb2383830b)

![image](https://github.com/user-attachments/assets/02ff973c-63e0-4ef1-ab47-45791892af05)

# 12

#Se crea la funcion para dar resultado a una variable.

def mi_funcion(x,/):

print(x)

#Da error.

mi_funcion(x=3)


![image](https://github.com/user-attachments/assets/6c5deac9-44e8-486c-8abd-0cb2d6a2f7a7)


![image](https://github.com/user-attachments/assets/bcc9a049-5b29-4fd6-92cc-0c666825ac8a)

# 14

#La funcion corregida

def my_function(*, x):

  print(x)

#Ahora si muestra el valor de la variable.

my_function(x = 3)


![image](https://github.com/user-attachments/assets/51ff7461-a1fc-40a9-8fbc-5dc768c72cb5)

![image](https://github.com/user-attachments/assets/4b90e671-4246-4062-b79b-3595a1b078ab)

# 17

#Se crea una funcion para convertir una variable en numero.

def mi_funcion(x):

print(x)

#El numero en el que vamos acombertir la variable.

mi_funcion(3)


![image](https://github.com/user-attachments/assets/6add2172-636b-44b7-a44f-2ed6cf6c8b8d)

![image](https://github.com/user-attachments/assets/0c1b8a68-b9ee-4c85-a970-2de0c4487539)

# 18

#Se crea una funcion pero se agrega un "*" pero da error

def mi_funcion(*, x):

  print(x)

#Al agregar " * " nos dara error

mi_funcion(3)

![image](https://github.com/user-attachments/assets/0dd4cb29-11eb-44a2-928b-6a5cbde71205)


![image](https://github.com/user-attachments/assets/1be151dc-30f5-401e-b28e-3c0d854afdcc)

# 19


#Se crea ujna funcion para sacar la suma de varias variables.

def mi_funcion(a,b,/,*,c,d):

print(a + b + c + d)

#Se agregan los valores.

mi_funcion(5,6,c=7,d=8)


![image](https://github.com/user-attachments/assets/ef0daf78-9cfe-4a21-9bbd-1cb641fd460a)

![image](https://github.com/user-attachments/assets/1db1311e-dc1e-41cc-b3c8-dbe97a4a938f)

# 20


#Define la funcion

def tri_recursion(pollos):

if pollos > 0:

resultado = pollos + tri_recursion(pollos-1)
 
print(resultado)
    
else:

resultado = 0

return resultado


![image](https://github.com/user-attachments/assets/61ebe698-7900-4f2c-814c-3b652401001c)


![image](https://github.com/user-attachments/assets/8f67fa3e-da73-463f-913f-6748b60c6c61)


















