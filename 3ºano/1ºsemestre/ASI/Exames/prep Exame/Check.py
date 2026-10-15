def CheckLogs(Log):
    """
    Pergunta 2 b) do Teste B (2,0 valores):
    Retorna uma lista com os pedidos em que o valor dos dados transmitidos
    ultrapassou os 2048 bytes utilizando as estruturas de dados criadas.
    """
    pedidos_maiores = []

    for host, datas in Log.items():
        for data, lista_pedidos in datas.items():
            for metodo, recurso, status, nbytes in lista_pedidos:
                if nbytes > 2048:
                    pedidos_maiores.append({
                        'host': host,
                        'data': data,
                        'metodo': metodo,
                        'recurso': recurso,
                        'status': status,
                        'bytes': nbytes
                    })

    return pedidos_maiores

if __name__ == '__main__':
    from ReadLogFile import Read
    Log = Read()
    resultado = CheckLogs(Log)
    print(f"Pedidos com bytes > 2048: {len(resultado)}")
    for r in resultado:
        print(r)
