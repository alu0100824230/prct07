
#! encoding: UTF-8
import modulo
def upla(fin):
    for elemento in fin:
      print "El valor aproximado de PI es: %11.10f" % elemento
  
l=[]
t_upla=(10,100,1000,10000,100000,1000000,10000000,100000000)
for elemento in t_upla:
    s=modulo.aproxpi(elemento)
    l=l+[s]
m=upla(l)


#Con 7 elementos va lento pero llega hasta 8 elementos.
#Valores mayores de 100000000.
#Sí se puede por ejemplo 1*10.
#Es el archivo ejecutable, aparece en el módulo.
#Tarda más de un minuto en ejecutarse.
