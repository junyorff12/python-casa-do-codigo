import os

def extract_name(name):
    return name.split('.')[0]  # separa o nome da extensao, (.) e pega so o primeiro indice

def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data

def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split('\t')[:3]))
    return metadata

def prompt():
    print("\nOque deseja ver?")
    print("(l) Listar entidades")
    print("(d) Exibir atrinbutos de entidade")
    print("(r) Exibir referência de entidade")
    print("(s) Sair do programa")
    return input('')

def main():
    #  dicionario de entidades -> atributos
    meta ={}

    #  dicionario identificador  -> nome atributos
    keys = {}

    #  dicionario de relacionamentos
    relationships = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name

    for key, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] in meta[key][0][0]:
                    relationships[key] = keys[col[0]]

    opcao = prompt()
    while opcao != 's':
        if opcao == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif opcao == 'd':
            entity_name = input("Nome da entidade: ")
            for col in meta[entity_name]:
                print(col)

        elif opcao == 'r':
            entity_name = input("nome da entidade: ")
            other_entity = relationships[entity_name]
            print(other_entity)
        else:
            print("inexistente\n")

        opcao = prompt()


if __name__ == '__main__':
    main()






