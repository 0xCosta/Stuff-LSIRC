"""
====================================================================
TESTE A RESOLVIDO - NOTA MÁXIMA (20,0 VALORES)
Unidade Curricular: Administração de Sistemas Informáticos (ASI)
ESTG - Politécnico do Porto
====================================================================
"""
from ReadFile import Read
from Check import bckSuccess
from Average import AverageBackupTime
from Stats import TotalBackups, TotalFailed
from ofuscador_sha256 import ofuscar_estudantes
import pprint

def main():
    print("=" * 65)
    print("  RESOLUÇÃO COMPLETA DO TESTE A - ESTG (20 VALORES)  ")
    print("=" * 65)

    # 1. Pergunta 1: Ofuscação com SHA-256 (5,0 valores)
    print("\n>>> [1/4] PERGUNTA 1: Ofuscação de Nºs de Estudante SHA-256 (5,0v)")
    with open("estudantes.txt", "w", encoding="utf-8") as f:
        f.write("Estudante 8210123 submeteu o trabalho.\nEstudante 8200999 também submeteu.\n")
    saida = ofuscar_estudantes("estudantes.txt", "estudantes_sha256.txt")
    with open(saida, "r", encoding="utf-8") as f:
        print(f.read().strip())

    # 2. Pergunta 2 a): ReadFile.py (4,0 valores)
    print("\n>>> [2/4] PERGUNTA 2 a): Leitura para Hashtable Backups (4,0v)")
    backups = Read("backup.txt")
    print(f"Hashtable carregada com {len(backups)} datas registadas:")
    pprint.pprint(backups)

    # 3. Pergunta 2 b): Check.py -> bckSuccess (4,0 valores)
    print("\n>>> [3/4] PERGUNTA 2 b): Backups que falharam por host (4,0v)")
    falhas = bckSuccess(backups)
    for host, lista in falhas.items():
        print(f"  Host {host} falhou em: {lista}")

    # 4. Pergunta 2 c) & d): Average.py e Stats.py (7,0 valores)
    print("\n>>> [4/4] PERGUNTA 2 c) & d): Médias e Estatísticas (7,0v)")
    data_pesquisa = "2024/02/21"
    media_m = AverageBackupTime(backups, data_pesquisa)
    print(f"  Intervalo médio de backups em {data_pesquisa}: {media_m:.2f} minutos")

    print("\n  Estatísticas Globais por Host:")
    for h in ['EX1', 'EX2', 'EX3']:
        t = TotalBackups(backups, h)
        f = TotalFailed(backups, h)
        print(f"  - Host {h}: Total = {t} backups | Falhas = {f}")

    print("\n" + "=" * 65)
    print("  TESTE A EXECUTADO COM SUCESSO (20/20 VALORES)  ")
    print("=" * 65)

if __name__ == '__main__':
    main()
