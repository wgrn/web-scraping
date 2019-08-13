# web-scraping
Web scraping program using regular expressions, developed in Python 3.
The purpose is to pull and structure The World Factbook's data into lists and dictionaries to build a Knowledgebase.

Usage: 
$ python3 factbook.py
operating_system:  Linux
Get files (Y/N): N

Output:
File named "file_data.py" in the same directory containing the dictionaries and lists created out of the data pulled from The World Factbook of the CIA.

Note:
In order for the web scraping program to work you must have an internet connection.
If you're on Windows you'll have to change the WORKDIR constant in the line 26 of the data.py file.

In case you enter Get files (Y/N): Y
Only enter Y if you're willing to wait about 8 minutes and spend about 148.8 MB in order to download all the html files used, which is not required.
