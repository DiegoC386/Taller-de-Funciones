frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que retorne la copia de una lista que pasa por parametro
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def copia_lista(lista):
  aux=[]
  for i in lista:
    aux.append(i)
  return aux
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
nueva_dos=eliminar_un_caracter(lista_numeros,"\n")
print(copia_lista(nueva))
print(copia_lista(nueva_dos))