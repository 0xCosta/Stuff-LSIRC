import re

str="Diogo Fernando Aguia Costa"


pattern = re.compile(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$')
if pattern.match(str):
	print ("Nome valido")
else:
	print ("Nome invalido")
