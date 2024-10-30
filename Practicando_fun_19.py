#Se crea ujna funcion para sacar la suma de varias variables.
def mi_funcion(a,b,/,*,c,d):
    print(a + b + c + d)
#Se agregan los valores.
mi_funcion(5,6,c=7,d=8)