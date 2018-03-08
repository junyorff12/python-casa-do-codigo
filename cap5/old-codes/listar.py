import os

#for meta_file in os.listdir('/home/jrff12/Downloads'):
#   print(meta_file)

def extrair_entidade(filename):
    return filename.split('.')[0]

#a = extrair_entidade('Licitação.txt')
#print(a)

def meta_dados(caminho):
    dados = open(caminho, "rt")
    meta_dados = []
    for linha in dados:
        linha_data = linha.split('\t')
        meta_dados.append((linha_data[0],linha_data[1],linha_data[2]))

    dados.close()
    return meta_dados

print(meta_dados('data/meta-data/Instituicao.txt'))




