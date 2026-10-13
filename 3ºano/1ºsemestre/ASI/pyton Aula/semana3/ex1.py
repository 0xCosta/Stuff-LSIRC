import sys

hashtable = {}

with open('semana3/input.txt') as fp:
    for linha in fp:
        linha = linha.strip()
        if linha:
            campos = linha.split(';')
            numero = campos[0]
            nome = campos[1]
            hashtable[numero] = nome

print(hashtable)

sys.stdout.write("Insira numero: ")
sys.stdout.flush()
numero = sys.stdin.readline().strip()

print(hashtable[numero])