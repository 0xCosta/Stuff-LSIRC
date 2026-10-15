def TotalBackups(backups, host_alvo):
    """
    Pergunta 2 d) do Teste A (3,0 valores):
    Retorna o número de registos realizados por host.
    """
    total = 0
    for data, hosts in backups.items():
        if host_alvo in hosts:
            total += len(hosts[host_alvo])
    return total

def TotalFailed(backups, host_alvo):
    """
    Pergunta 2 d) do Teste A (3,0 valores):
    Retorna o número de Failed registados por host.
    """
    falhas = 0
    for data, hosts in backups.items():
        if host_alvo in hosts:
            for hora, status in hosts[host_alvo].items():
                if status == 'Failed':
                    falhas += 1
    return falhas

if __name__ == '__main__':
    from ReadFile import Read
    b = Read()
    for h in ['EX1', 'EX2', 'EX3']:
        print(f"Host {h}: Total = {TotalBackups(b, h)} | Falhas = {TotalFailed(b, h)}")
