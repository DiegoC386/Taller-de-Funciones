frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#realizar una funcion que agregue al final de archivo frutas una fruta
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
def frutas(lista,elemento):
  lista.append(elemento)
  return lista

if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
print("Ingrese la nueva fruta: ")
elemento=input()
nueva_fruta = frutas(nueva, elemento)
print(nueva_fruta)