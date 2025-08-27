import os

def renomear_arquivos(pasta, prefixo):
    arquivos = os.listdir(pasta)
    for i, nome in enumerate(arquivos):
        extensao = os.path.splitext(nome)[1]
        novo_nome = f"{prefixo}_{i}{extensao}"
        os.rename(os.path.join(pasta, nome), os.path.join(pasta, novo_nome))
        print(f"{nome} → {novo_nome}")

# Exemplo de uso
renomear_arquivos("arquivos", "documento")
