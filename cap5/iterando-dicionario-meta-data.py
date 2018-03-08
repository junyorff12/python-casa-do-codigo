import os


def extract_name(name):
    return name.split('.')[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split('\n')
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for coluna in read_lines(filename):
        if coluna:
            valores = coluna.split('\t')
            nome = valores[0]
            tipo = valores[1]
            desc = valores[2]
            metadata.append((nome, tipo, desc))
    return metadata


def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
            nome_tabela = extract_name(meta_data_file)
            meta[nome_tabela] = read_metadata(meta_data_file)

    for key, val in meta.items():
        print("Entidades {}:".format(key))
        print("Atributos :")
        for col in val:
            print(" {}: {}".format(col[1], col[0]))


if __name__ == "__main__":
    main()