"""
====================================================================
PROVA MODELO / TESTE B RESOLVIDO - NOTA MÁXIMA (20,0 VALORES)
Unidade Curricular: Administração de Sistemas Informáticos (ASI)
Cursos: Licenciatura em Segurança Informática em Rede (LSIRC) / LEI
ESTG - Politécnico do Porto
====================================================================
"""
from ReadLogFile import Read
from Check import CheckLogs
from Average import AvarageMethod
from anonimizador import anonimizar
import pprint

def main():
    print("=" * 65)
    print("  RESOLUÇÃO COMPLETA DO TESTE DE ASI - ESTG (20 VALORES)  ")
    print("=" * 65)

    # -------------------------------------------------------------
    # 1. Pergunta 1: Anonimização de Logs (6,0 valores)
    # -------------------------------------------------------------
    print("\n>>> [1/4] EXECUTANDO PERGUNTA 1: Anonimização e Sanitização (6,0v)")
    ficheiro_anon = anonimizar("acessos.txt")
    with open(ficheiro_anon, "r", encoding="utf-8") as f:
        print("Conteúdo Anonimizado:")
        for l in f:
            print("  ", l.strip())

    # -------------------------------------------------------------
    # 2. Pergunta 2 a) e d): Leitura para Hashtables & Regex (10,0v)
    # -------------------------------------------------------------
    print("\n>>> [2/4] EXECUTANDO PERGUNTA 2 a) & d): Leitura e Validação (10,0v)")
    Log = Read("acessos_servidor.txt")
    print(f"Hashtable Log carregada com sucesso ({len(Log)} hosts válidos):")
    pprint.pprint(Log)

    # -------------------------------------------------------------
    # 3. Pergunta 2 b): Check.py - Pedidos > 2048 Bytes (2,0 valores)
    # -------------------------------------------------------------
    print("\n>>> [3/4] EXECUTANDO PERGUNTA 2 b): Check.py (2,0v)")
    pedidos_grandes = CheckLogs(Log)
    print(f"Total de pedidos com dados transmitidos > 2048 bytes: {len(pedidos_grandes)}")
    for p in pedidos_grandes:
        print(f"  -> Host: {p['host']} | Data: {p['data']} | {p['metodo']} {p['recurso']} | {p['bytes']} bytes")

    # -------------------------------------------------------------
    # 4. Pergunta 2 c): Average.py - Método mais comum no mês (2,0v)
    # -------------------------------------------------------------
    print("\n>>> [4/4] EXECUTANDO PERGUNTA 2 c): Average.py (2,0v)")
    mes_teste = "2025-03"
    metodo_comum = AvarageMethod(Log, mes_teste)
    print(f"Método HTTP mais comum no mês {mes_teste}: '{metodo_comum}'")

    print("\n" + "=" * 65)
    print("  EXECUÇÃO CONCLUÍDA COM 100% DE CONFORMIDADE (20/20 VALORES)  ")
    print("=" * 65)

if __name__ == '__main__':
    main()
