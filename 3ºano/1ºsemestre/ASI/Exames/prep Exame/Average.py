def AvarageMethod(Log, mes):
    """
    Pergunta 2 c) do Teste B (2,0 valores):
    Retorna o método (e.g. POST, GET, PUT, etc.) mais comum num determinado
    mês, utilizando as estruturas de dados criadas.
    Exemplo de 'mes': '2025-03' ou '03'.
    """
    contagem = {}

    for host, datas in Log.items():
        for data, lista_pedidos in datas.items():
            # Verifica se o registo corresponde ao mês especificado
            if data.startswith(mes) or f"-{mes.zfill(2)}-" in data:
                for metodo, recurso, status, nbytes in lista_pedidos:
                    contagem[metodo] = contagem.get(metodo, 0) + 1

    if not contagem:
        return None

    # Devolve a chave com maior valor de contagem
    return max(contagem, key=contagem.get)

if __name__ == '__main__':
    from ReadLogFile import Read
    Log = Read()
    metodo = AvarageMethod(Log, "2025-03")
    print(f"Método mais comum no mês 2025-03: {metodo}")
