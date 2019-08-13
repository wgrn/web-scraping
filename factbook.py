#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# C:\Users\lfo\AppData\Local\Programs\Python\Python36-32\python.exe C:\Users\lfo\Documents\p\data.py

from data import *

getFiles(get_files)

# Creating countries Dictionary
for i in range(len(country_code)):
   countries[country_code[i]] = country_name[i].replace('&#39;', '\'')
# Printing countries Dictionary
#print (len(countries), countries)


# Getting document to find the country field's description
with urllib.request.urlopen(CTRYURL + c + '.html') as response:
   html = response.read()

# Getting the country field's description
regular_expression = re.compile(REGEX[4])
field_desc         = re.findall(REGEX[4], str(html))

# Creating fields Dictionary (list)
for i in range(len(field_desc)):
   field_desc[i] = field_desc[i].split('\\n')[1].strip().replace('&#39;', '\'').replace('&quot;', '"')
   field.append(field_code[i])
   field.append(field_name[i])
   field.append(field_desc[i])
   fields.append(field)
   field = []


#'''
# Getting each country field's data ????
for c in sorted(pais): # Here is where c finally gets to change
   with urllib.request.urlopen(CTRYURL + c + '.html') as response:
      html = response.read()
   regular_expression = re.compile(REGEX[5])
   field_value        = re.findall(REGEX[5], str(html))

   country.append(c) # country's code
   country.append(countries[c]) # country's name

   for i in range(len(field_code)):
       field.append(field_code[i])
       field.append("data") # field.append(field_data[i])
       country.append(field) # country field's data
       field = []

   Factbook.append(country)
   country = []
#'''

# Writing file_data.py file with countries and fields Dictionaries
file_data = open('file_data.py', 'w')
file_data.write('countries = ' + str((countries)) + '\n\n')
file_data.write('fields = ' + str((fields)) + '\n\n')
file_data.write('Factbook = ' + str((Factbook)) + '\n\n')

file_data.close()
