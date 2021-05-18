frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista

if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_pares(nueva)
  eliminar=elimina_elemento_lista(nueva_dos,'10')
  print(eliminar)
