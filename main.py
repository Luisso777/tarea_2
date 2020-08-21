print("__________Json____________________________________________")
import json

def leerJson():

  file = open('ejemplo.json')
  data = json.load(file)
  file.close()
  print(data)
  return (data)
  dict = leerJson()
  for element in dict:
      print(element)
leerJson()


print("______________XML_______________________________________________________")
import xml.etree.ElementTree as ET

archivo = ET.parse('ejemplo2.xml')
raiz = archivo.getroot()

for atributo in raiz:
    print(atributo.tag,atributo.attrib)
    for registro in atributo:
        print(registro.tag,registro.attrib)






print("______________csv________________")
import csv

with open('ejemplo3.csv') as archvocsv:
    leer = csv.reader(archvocsv, delimiter=',')
    print(leer)
    for col in leer:
        print(col)