#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import urllib.request
import re
import os
import subprocess

# Inputs
#operating_system = input('Operating System Linux or Windows (Linux/W): ')
operating_system = subprocess.run(['uname'], stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]
print('operating_system: ', operating_system)
get_files        = input('Get files (Y/N): ')
if get_files == 'Y':
   get_files = True
elif get_files == 'N':
   get_files = False
else:
   get_files = False

# Constants
BASEURL = 'https://www.cia.gov/library/publications/the-world-factbook/'
if operating_system == 'Linux':
   WORKDIR = os.getcwdb().decode('ascii') + '/'
elif operating_system == 'W':
   WORKDIR = 'C:\\Users\\lfo\\Documents\\p\\'
else:
   WORKDIR = '/home/lombardo/Documents/cia/'

CTRYURL = BASEURL + 'geos/'
FLDURL  = BASEURL + 'fields/'
REGEX   = ['(?<=geos/)[a-z]+',
         '(?<=<option value="geos/)*[^.]+</option>',
         '(?<=fields/)\\d+.html#',
         '(?<=.html#US"><img alt=")[a-zA-Z0-9-+\'/(), ]+',
         '(?<=tooltip-content">)[^. ]+[a-zA-Z0-9(),;.&#-:%+/ ]+',
         ''] # last one is for the field's values
# '(?<=<div class=category_data>)[^<]+'
# '/notesanddefs.html?fieldkey=[0-9]+'
# '&amp;term=[a-zA-Z0-2%]+'
# '(?<=">)[a-zA-Z ]+'
# '/notesanddefs.html?fieldkey=2011&amp;term=Geographic%20coordinates">'
# '[a-zA-Z ]+:</a><a href="' + BASEURL +'fields/'

# Auxiliary variables
regular_expression = ''
html               = ''
c                  = 'us' #default value but can change


# Auxiliary lists
field        = []
country      = []
pais         = ['mx', 'us', 'ca'] # instead of country_code list, just to show functionality
field_code   = []
field_name   = []
field_desc   = []
field_data   = [] # the specific field values for each country
country_code = []
country_name = []


# Dictionaries
#'0000': 'country'
fields    = []
countries = {}

# Condensed Information Tables
Factbook = []

# The File with current data
file_data = ''

"""
# fields in boolean
fld_bool = ["Citizenship"]

def isStr(fieldCode):
   for i in range(len(fld_nbr)):
      if fields[fieldCode] == fld_nbr[i]:
         return true
   return false
"""

#Getting document to find country's code and name
with urllib.request.urlopen(BASEURL) as response:
   html = response.read()

# Getting the country's code
regular_expression = re.compile(REGEX[0])
country_code       = re.findall(REGEX[0], str(html))
#print(len(country_code), country_code)

# Getting the country's name
regular_expression = re.compile(REGEX[1])
country_name       = re.findall(REGEX[1], str(html))
for i in range(len(country_name)):
   country_name[i] = country_name[i].split('\\n')[1].strip()
country_name = country_name[1:]
#print(len(country_name), country_name)


#Getting document to find field's code and name
with urllib.request.urlopen(CTRYURL + c + '.html') as response:
   html = response.read()

# Getting the field's code
regular_expression = re.compile(REGEX[2])
field_code         = re.findall(REGEX[2], str(html))
for i in range(len(field_code)):
   field_code[i] = field_code[i].replace('.html#', '')
#print(len(field_code), field_code)

# Getting the field's name
regular_expression = re.compile(REGEX[3])
field_name         = re.findall(REGEX[3], str(html))
for i in range(len(field_name)):
   field_name[i] = field_name[i].replace(' field listing', '')
#print(len(field_name), field_name)

def getFiles(get_files):
   # Create WORKDIR's subdirectories if do not exist
   if get_files:
      if operating_system == 'Linux':
         dir_countries = 'countries/'
         dir_fields    = 'fields/'
      elif operating_system == 'W':
         dir_countries = 'countries\\'
         dir_fields    = 'fields\\'

      if not os.path.exists(WORKDIR + dir_countries):
         os.makedirs(WORKDIR + dir_countries)

      if not os.path.exists(WORKDIR + dir_fields):
         os.makedirs(WORKDIR + dir_fields)

      #"""
      # Getting countries' files for Linux
      for country in country_code:
         urllib.request.urlretrieve(CTRYURL + country + '.html',
         WORKDIR + dir_countries + country + '.html')
      #"""

      #"""
      # Getting fields' files for Linux
      for field in field_code:
         urllib.request.urlretrieve(FLDURL + field + '.html',
         WORKDIR + dir_fields + field + '.html')
      #"""

      print ('Files successfully downloaded.')

   return True
