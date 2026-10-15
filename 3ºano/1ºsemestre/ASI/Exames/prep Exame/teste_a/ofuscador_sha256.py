import re
import hashlib

def ofuscar_estudantes(ficheiro_entrada="estudantes.txt", ficheiro_saida="estudantes_sha256.txt"):
    """
    Pergunta 1 do Teste A (5,0 valores):
    Lê um ficheiro e ofusca todas as ocorrências de um número de estudante com
    o formato 8NNNNNN (onde N é um dígito 0-9) pelo correspondente valor SHA256,
    guardando o output num ficheiro de saída.
    """
    re_estudante = re.compile(r'\b8\d{6}\b')

    def substituir_por_sha256(match):
        num_aluno = match.group(0)
        return hashlib.sha256(num_aluno.encode('utf-8')).hexdigest()

    linhas_processadas = []
    with open(ficheiro_entrada, 'r', encoding='utf-8') as f:
        for linha in f:
            linha_ofuscada = re_estudante.sub(substituir_por_sha256, linha)
            linhas_processadas.append(linha_ofuscada)

    with open(ficheiro_saida, 'w', encoding='utf-8') as f:
        f.writelines(linhas_processadas)

    print(f"[OK] Ficheiro com SHA256 gravado: {ficheiro_saida}")
    return ficheiro_saida

if __name__ == '__main__':
    exemplo = "Aluno: 8210123 realizou o exame com sucesso.\nAluno: 8200456 ausente.\n"
    with open("estudantes.txt", "w", encoding="utf-8") as f:
        f.write(exemplo)
    ofuscar_estudantes()
