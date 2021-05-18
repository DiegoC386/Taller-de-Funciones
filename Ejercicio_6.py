frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas
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
def letra(lista,elemento):
  auxiliar=[]
  for x in lista:
    if(x[0]=="M"):
      print(x)
      auxiliar.append(x)
    return auxiliar

if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=letra(nueva,"M")
  print(nueva_dos)
 
 