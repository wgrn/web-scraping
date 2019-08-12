#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# C:\Users\lfo\AppData\Local\Programs\Python\Python36-32\python.exe C:\Users\lfo\Documents\p\data.py

from data import *

# Creating fields Dictionary
for i in range(len(field_code)):
   fields[field_code[i]] = field_name[i]
# Printing fields Dictionary
#print (fields)

# Creating countries Dictionary
for i in range(len(country_code)):
   countries[country_code[i]] = country_name[i]
# Printing countries Dictionary
#print (len(countries), countries)

#Factbook = [sorted(fields) for c in sorted(countries)]
#print(Factbook)

# Writing file_data.py file with countries and fields Dictionaries
file_data = open('file_data.py', 'w')
file_data.write('countries = ' + str((countries)) + '\n')
file_data.write('fields = ' + str((fields)) + '\n')

#print(sorted(fields))
#country_fields = list(fields)
#print(country_fields)
#Factbook.append(country_fields)
#print(Factbook)

#Getting document to find the country's fields
with urllib.request.urlopen(CTRYURL + 'us.html') as response:
   html = response.read()

# Getting the country's fields (description)
regular_expression = re.compile(REGEX[4])
country_fields     = re.findall(REGEX[4], str(html))
for i in range(len(country_fields)):
   country_fields[i] = country_fields[i].split('\\n')[1].strip().replace('&#39;', '\'').replace('&quot;', '"')

# Getting the country's fields (values) ????

#Factbook.append(country_fields)
#country_fields = sorted(fields)

#file_data.write('Factbook = ' + str(Factbook))

'''
for c in sorted(countries):
	with urllib.request.urlopen(CTRYURL + c + '.html') as response:
		html = response.read()
	regular_expression = re.compile(REGEX[4])
	country_fields     = re.findall(REGEX[4], str(html))
	country_fields = list(c) + country_fields

	Factbook.append(country_fields)
	#country_fields = sorted(fields)

file_data.write('Factbook = ' + str(Factbook))
'''
file_data.close()
