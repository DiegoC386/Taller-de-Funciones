frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
""" 
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
#Realizar una funcion que cuente el numero de veces que se repite un elemento  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def repetir(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return len(lista_posiciones)

if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  print("Ingresa el numero que se repite en la lista de numeros: ")
  elemento = input()
  repeticiones = repetir(nueva, elemento)
  print(repeticiones)
