frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def posicion_elemento(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return lista_posiciones

if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
print("Ingresa una fruta que se encuentre en la lista de frutas:")
elemento = input() 
posicion = posicion_elemento(nueva, elemento)
print(posicion)



