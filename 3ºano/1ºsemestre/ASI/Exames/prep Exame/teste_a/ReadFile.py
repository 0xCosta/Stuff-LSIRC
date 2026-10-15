def Read(caminho_ficheiro="backup.txt"):
    """
    Pergunta 2 a) do Teste A (4,0 valores):
    Lê o ficheiro 'backup.txt' para uma estrutura hashtable backups:
    backups = {
        'AAAA-MM-DD': {
            'host': {
                'HH:MM:SS': 'Status'
            }
        }
    }
    """
    backups = {}
    with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue

            partes = linha.split(';')
            if len(partes) != 3:
                continue

            data_hora, host, status = partes
            data_str, hora_str = data_hora.split(' ')

            # Formato da data pedido no enunciado: AAAA-MM-DD
            data_formatada = data_str.replace('/', '-')

            if data_formatada not in backups:
                backups[data_formatada] = {}
            if host not in backups[data_formatada]:
                backups[data_formatada][host] = {}

            backups[data_formatada][host][hora_str] = status

    return backups

if __name__ == '__main__':
    import pprint
    b = Read()
    pprint.pprint(b)
