import os

caminho = r"c:\python"

arquivos = os.listdir(caminho)

data_recente = []

for arquivo in arquivos:
    if 'xlsx' in arquivo:
        # pegar a data de modificação do arquivo
        data = os.path.getmtime(f"{caminho}\\{arquivo}")
        data_recente.append((data, arquivo))


data_recente.sort(reverse=True)
print(data_recente[0][1])
