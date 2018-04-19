class Proxy:
    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, name):
        print("Acesso ao atributo {}".format(name))
        if hasattr(self.obj, name):
            return getattr(self.obj, name)
        else:
            raise Exception("Atributo desconhcido")


class DataTable:
    def __init__(self, name):
        self.name = name


class Query:
    def __init__(self, atributes):
        self.atributes = atributes


table_proxy = Proxy(DataTable("ExecucaoFinanceira"))

query_proxy = Proxy(Query(['id', 'valor']))

print(table_proxy.__dict__)

print(query_proxy.__dict__)

print(table_proxy.name)

print(query_proxy.atributes)




