import re

cc="10021723 7 ZY2"

pattern = re.compile(r'^\d{8} \d [A-Z]{2}\d$')
if pattern.match(cc):
	print ("CC valido")
else:
	print ("CC invalido")
