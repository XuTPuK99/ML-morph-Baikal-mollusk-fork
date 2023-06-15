# -*- coding: utf-8 -*-
"""Xml_to_TPS._from_Modicos.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xoos06_O94TUqpR2XF2llI2Bchjbw97J
"""

import xml.etree.ElementTree as ET

tree = ET.parse('output.xml')
root = tree.getroot()

file_MODICOS = open('output_from_MODICOS.txt', 'w')
file_MODICOS.write("[MODICOS - POINTS]" + "\n")

images = root[2]

number_smooth = 0
number_ribbed = 0

for image in images:

  file = image.attrib['file']
  _, file = file.split('/')
  file , _ = file.split('.')
  file , _ = file.split('_')
  print(file)

  if file == "smooth":

    number_smooth += 1
    file_MODICOS.write("01.01." + str(number_smooth) + "\n")

    for i in range(15):
      x = image[0][i].attrib['x']
      y = image[0][i].attrib['y']

      file_MODICOS.write(x + " ")
      file_MODICOS.write(y + "\n")

  else:

    number_ribbed += 1
    file_MODICOS.write("01.02." + str(number_ribbed) + "\n")

    for i in range(15):
      x = image[0][i].attrib['x']
      y = image[0][i].attrib['y']

      file_MODICOS.write(x + " ")
      file_MODICOS.write(y + "\n")