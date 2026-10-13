import sys
import json

nifs = {}
with open("semana3/dados.txt") as fp:
    for linha in fp:
        if linha.startswith("#"):
            continue
        linha = linha.strip().split(";")
        if linha[0] in nifs.keys():
            veiculos2 = nifs[linha[0]]
            veiculos2[linha[1]] = linha[2]
            nifs[linha[0]] = veiculos2    
        else:
            veiculos = {}
            veiculos[linha[1]] = linha[2]
            nifs[linha[0]] = veiculos
fp.close()

print (json.dumps(nifs, ensure_ascii=False))

sys.stdout.write("Insira nif: ")
sys.stdout.flush()

nif = sys.stdin.readline()
nif = nif.strip()

if nif in nifs:
    veiculos = nifs[nif]
    for mat,iuc in veiculos.items():
        print("A matricula %s tem a pagar de IUC %s" % (mat, iuc))
else:
    print("NIF nao encontrado.")