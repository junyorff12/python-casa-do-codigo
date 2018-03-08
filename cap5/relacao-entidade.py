import os

def extract_name(name):
    return name.split('.')[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for coluna in read_lines(filename):
        if coluna:
            valor = coluna.split('\t')
            nome = valor[0]
            tipo = valor[1]
            desc = valor[2]
            metadata.append((nome, tipo, desc))

    return metadata


def main():
    #  dicionario de atributos
    meta = {}

    # dicionario identidficador -> nome entidade

    keys = {}

    for meta_data_file in os.listdir("data/meta-data"):
        tabela_nome = extract_name(meta_data_file)
        atributos = read_metadata(meta_data_file)
        identificador = atributos[0][0]

        meta[tabela_nome] = atributos
        keys[identificador] = tabela_nome
    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    i = col[0]
                    print('Entidade {} -> {}'.format(key, col[0]))


if __name__ == "__main__":
    main()

