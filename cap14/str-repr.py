class Datatable:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return "Tabela {}".format(self._name)


class DataT:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return "Tabela {}".format(self._name)


table = Datatable("Execucaofinanceira")

table2 = DataT("ExecucaoFinanceira2")

str(table)
str(table2)
