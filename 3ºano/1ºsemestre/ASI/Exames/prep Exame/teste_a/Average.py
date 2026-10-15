from datetime import datetime

def AverageBackupTime(backups, data_pesquisa):
    """
    Pergunta 2 c) do Teste A (4,0 valores):
    Retorna a duração média ou intervalo médio entre os registos
    numa determinada data (e.g. 2024/02/21 ou 2024-02-21).
    """
    data_formatada = data_pesquisa.replace('/', '-')

    if data_formatada not in backups:
        return 0.0

    # Coletar todos os horários registados nessa data
    horas_dt = []
    for host, horas in backups[data_formatada].items():
        for hora in horas.keys():
            dt = datetime.strptime(hora, "%H:%M:%S")
            horas_dt.append(dt)

    if len(horas_dt) < 2:
        return 0.0

    horas_dt.sort()
    intervalos_segundos = []
    for i in range(len(horas_dt) - 1):
        delta = (horas_dt[i+1] - horas_dt[i]).total_seconds()
        intervalos_segundos.append(delta)

    media_segundos = sum(intervalos_segundos) / len(intervalos_segundos)
    return media_segundos / 60.0  # Retorna em minutos

if __name__ == '__main__':
    from ReadFile import Read
    b = Read()
    media_min = AverageBackupTime(b, "2024/02/21")
    print(f"Intervalo médio entre backups em 2024/02/21: {media_min:.2f} minutos")
