import sys
import json

##Alinea a
alunos = {}
with open("semana3/alunos.txt") as fp:
    for linha in fp:
        if ";F;" in linha:
            linha = linha.strip().split(";")
            dados = [linha[1], linha[2], linha[3], linha[4]]
            alunos[linha[0]] = dados
fp.close()
print (json.dumps(alunos, ensure_ascii=False))

##Alinea b
sys.stdout.write("Insira numero: ")
sys.stdout.flush()
aluno = sys.stdin.readline()
aluno = aluno.strip()
if aluno in alunos:
    print(alunos[aluno])
else:
    print("Aluno nao encontrado.")

##Alinea c
def media(lista):
    return float(sum(lista)/len(lista))

lista = []
for k,v in alunos.items():
    lista.append(float(alunos[k][1]))

print("A media de idades e %.2f" % (media(lista)))