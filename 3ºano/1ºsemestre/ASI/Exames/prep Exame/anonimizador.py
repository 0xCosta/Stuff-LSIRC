import re
import os

def anonimizar(caminho_entrada="acessos.txt"):
    """
    Pergunta 1 do Teste B (6,0 valores):
    - Lê um ficheiro de texto contendo registos de acessos.
    - Ofusca os endereços IP substituindo os dois primeiros grupos por ***,
      mantendo os restantes (ex: 192.168.0.15 -> ***.***.0.15).
    - Converte todas as datas para DD/MM/YYYY (ex: 2025-10-24 -> 24/10/2025).
    - Anonimiza utilizadores para utilizador_X com X incremental consistente.
    - Remove linhas em branco e espaços duplicados.
    - Guarda no ficheiro <nome_original>_anon.txt.
    """
    base, ext = os.path.splitext(caminho_entrada)
    caminho_saida = f"{base}_anon{ext}"

    # Regex para capturar os 2 últimos grupos de um IP
    re_ip = re.compile(r'\b\d{1,3}\.\d{1,3}\.(\d{1,3}\.\d{1,3})\b')
    # Regex para capturar formato de data YYYY-MM-DD
    re_data = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')
    # Regex para utilizadores
    re_user = re.compile(r'\b(?:user|admin)_[a-zA-Z0-9_]+\b')

    mapa_users = {}
    contador_user = 1
    linhas_finais = []

    with open(caminho_entrada, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            # 1. Remover linhas em branco
            if not linha:
                continue

            # 2. Remover espaços duplicados
            linha = re.sub(r' +', ' ', linha)

            # 3. Ofuscar IPs
            linha = re_ip.sub(r'***.***.\1', linha)

            # 4. Converter datas YYYY-MM-DD para DD/MM/YYYY
            linha = re_data.sub(r'\3/\2/\1', linha)

            # 5. Anonimizar nomes de utilizadores
            def callback_user(m):
                nonlocal contador_user
                nome = m.group(0)
                if nome not in mapa_users:
                    mapa_users[nome] = f"utilizador_{contador_user}"
                    contador_user += 1
                return mapa_users[nome]

            linha = re_user.sub(callback_user, linha)
            linhas_finais.append(linha)

    # 6. Guardar no novo ficheiro
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        for l in linhas_finais:
            f.write(l + '\n')

    print(f"[OK] Ficheiro anonimizado gerado com sucesso: {caminho_saida}")
    return caminho_saida

if __name__ == '__main__':
    # Teste de demonstração
    exemplo = "192.168.0.15  user_jose   2025-10-24\n\n10.0.1.25    admin_maria   2025-11-05\n"
    with open("acessos.txt", "w", encoding="utf-8") as f:
        f.write(exemplo)
    anonimizar("acessos.txt")
