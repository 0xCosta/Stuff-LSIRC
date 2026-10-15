import re

pattern1 = re.compile(r';M;')
pattern2 = re.compile(r';F;')
with open("pyton Aula/semana5/dados.txt") as fp:
	for linha in fp:
		linha = linha.strip()
		linha = pattern1.sub(";M;00351",linha)
		linha = pattern2.sub(";F;00351",linha)
		print (linha)
	
