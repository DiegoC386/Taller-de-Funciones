frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamano
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def tamano_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux
 
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=tamano_lista(nueva)
  
  print(nueva_dos)
  
 