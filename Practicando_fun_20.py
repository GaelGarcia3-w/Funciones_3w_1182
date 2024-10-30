#Quien sabe
def tri_recursion(pollos):
    if pollos > 0:
        resultado = pollos + tri_recursion(pollos-1)
        print(resultado)
    else:
        resultado = 0
    return resultado