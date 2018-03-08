def extract_etity_name(name):  # extraindo a extensão .txt do arquivo, para usar o nome.
    return name.split('.')[0]

print(extract_etity_name('Licitação.txt'))

