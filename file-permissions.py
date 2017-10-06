import os
from os import stat
from pwd import getpwuid

def find_owner(filename):
	
    return getpwuid(stat(filename).st_uid).pw_name


while True:
	if (find_owner('ej01.py') != 'msosa'):
		print("WARNGING!!!!!")

