import re

masculino = dict()
feminino = dict()

pattern = re.compile(r';M;')
with open("dados.txt") as fp:
	for linha in fp:
		if pattern.search(linha):
			linha = linha.strip().split(";")
			masculino[linha[3]] = linha[0]
		else:
			linha = linha.strip().split(";")
			feminino[linha[3]] = linha[0]
print ("Masculino" , masculino.items())		
print ("Feminino", feminino.items())		
