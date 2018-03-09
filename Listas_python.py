



"""

Colores = ['rojo', 'Azul', 123, 'Morado', 'Amarillo']




#llamado la lista
print(Colores,"\n")
print(Colores[2],"\n")
print(len(Colores),"\n")

"""





#EJERCICIO DE LISTAS


"""

lista = []

i=1
while i<=100:
    lista.append(i)
    i=i+1

lista = list(range(1,101))

print(lista)
"""

#EJERCICIO LISTAS 2


#LISTA DE IZQUIERDA A DERECHA ES POSITIVO
#LISTA DE DERECHA A IZQUIERDA ES -1

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


"""
salir = False
while(not salir):

    numero = int(input("Dame un numero: "))

    if(numero==0):
        salir= True
    else:
        if(numero>=1 and numero<=len(meses)):
            print(meses[numero-1])
        else:
            print("Inserta un numero entre 1 y ",len(meses))
"""

meses.append('camilo') #insertar en la ultima posicion
meses.insert(3, 'nuevoObjeto')# (posicion de la lista, el nuevo objeto de la posicion)
remover = meses.pop()#eliminar algo de nuestra lista la ultima posision
meses.remove('Mayo')#remover un objeto identificado
meses.sort()#ordenar mi lista
mejorar_lista = sorted(meses)#una lista nueva pero de una forma mejor organizada
mejorar_lista = reversed() # revertir una lista que tengamos ordenados
print(meses)
