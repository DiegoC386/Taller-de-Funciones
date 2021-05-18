frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Salidas
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def informacion_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux
 
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=informacion_lista(nueva)

  print(type(nueva_dos))