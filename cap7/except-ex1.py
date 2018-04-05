import zipfile

try:
    banco_zip = zipfile.ZipFile("saida.zip")

except FileNotFoundError:
    print("Arquivo inexistente")
except PermissionError as pme:
    print("erro de permissão")

except OSError as ose:
    print("algum problema ao lero arquivo {} ".format(ose.filename))

except (FileNotFoundError, PermissionError):
    print("Algum problema ao ler o arquivo")
else:
    banco_zip.extractall(path="banco")
    banco_zip.close()

