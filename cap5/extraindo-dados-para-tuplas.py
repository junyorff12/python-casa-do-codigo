def lendo_meta_dados(caminho):
    dados = open(caminho, "rt")  # abrindo arquivo
    meta_dados = []  # definindo a lista
    for linha in dados:  # percorrendo o arquivo linha alinha
        linha_dados = linha.split('\t') # separando os atributos sepsrados por TAB ('\t')
        meta_dados.append((linha_dados[0], linha_dados[1], linha_dados[2]))  # adicionando os atributos separados na lista, dentro de tuplas.

    dados.close()  # fechando arquivo
    return meta_dados


print(lendo_meta_dados("data/meta-data/Instituicao.txt"))


