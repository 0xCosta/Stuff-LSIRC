import re

# Expressões Regulares de Validação de Linha (Pergunta 2d - 6,0 valores)
# Host: 4 grupos de números entre 10 e 255 separados por ponto
re_host = re.compile(r'^(?:(?:[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$')
# Data: AAAA-MM-DD entre 2025-01-01 e 2025-12-31 (inclusive)
re_data = re.compile(r'^2025-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$')
# Hora: HH:MM:SS válida entre 00:00:00 e 23:59:59
re_hora = re.compile(r'^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$')
# Método: GET, POST, PUT, DELETE, PATCH
re_metodo = re.compile(r'^(?:GET|POST|PUT|DELETE|PATCH)$')
# Recurso: Começa com / e pode conter letras, números, hífens, barras e parâmetros (?, =, &)
re_recurso = re.compile(r'^/[a-zA-Z0-9\-_/?=&]+$')
# HTTP Status: 3 dígitos com primeiro dígito 2, 3 ou 4
re_status = re.compile(r'^[234]\d{2}$')
# Bytes: Inteiro positivo inferior a 10.000.000
re_bytes = re.compile(r'^[1-9]\d{0,6}$')

def linha_valida(host, data, hora, metodo, recurso, status, nbytes):
    """Retorna True se todos os campos da linha satisfazem as regras do enunciado."""
    return (bool(re_host.match(host)) and
            bool(re_data.match(data)) and
            bool(re_hora.match(hora)) and
            bool(re_metodo.match(metodo)) and
            bool(re_recurso.match(recurso)) and
            bool(re_status.match(status)) and
            bool(re_bytes.match(nbytes)))

def Read(caminho_ficheiro="acessos_servidor.txt"):
    """
    Pergunta 2 a) (4,0 valores):
    Lê para a hashtable Log o conteúdo válido do ficheiro.
    Log = {
        Host: {
            Data: [(Método, Recurso, HTTP_Status, Bytes), ...]
        }
    }
    """
    Log = {}
    with open(caminho_ficheiro, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            # Ignorar linhas vazias e cabeçalhos iniciados por '#'
            if not linha or linha.startswith('#'):
                continue

            campos = linha.split(';')
            if len(campos) != 7:
                continue

            host, data, hora, metodo, recurso, status, nbytes = campos

            # Validação rigorosa segundo a Pergunta 2d
            if not linha_valida(host, data, hora, metodo, recurso, status, nbytes):
                continue

            status_num = int(status)
            bytes_num = int(nbytes)

            # Construção do dicionário aninhado multinível
            if host not in Log:
                Log[host] = {}
            if data not in Log[host]:
                Log[host][data] = []

            Log[host][data].append((metodo, recurso, status_num, bytes_num))

    return Log

if __name__ == '__main__':
    import pprint
    dados = Read()
    print("Hashtable Log:")
    pprint.pprint(dados)
