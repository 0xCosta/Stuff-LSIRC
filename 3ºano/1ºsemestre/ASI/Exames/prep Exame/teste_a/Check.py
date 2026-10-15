def bckSuccess(backups):
    """
    Pergunta 2 b) do Teste A (4,0 valores):
    Retorna uma hashtable tendo como chave o host e o valor será uma
    lista contendo a data e hora em que os backups falharam (status != 'Success').
    """
    falhas_por_host = {}

    for data, hosts in backups.items():
        for host, horas in hosts.items():
            for hora, status in horas.items():
                if status != 'Success':
                    if host not in falhas_por_host:
                        falhas_por_host[host] = []
                    falhas_por_host[host].append(f"{data} {hora}")

    return falhas_por_host

if __name__ == '__main__':
    from ReadFile import Read
    b = Read()
    falhas = bckSuccess(b)
    print("Falhas registradas por host:")
    print(falhas)
