#  definicao sem __eq__

class DataTable:

    def __init__(self, name):

        self._name = name

class Datatable():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return self.name == other.name



t1 = Datatable("ExecucaoFinanceira")
t2 = Datatable("ExecucaoFinanceira")
print(t1 == t2)



print(t1.__dict__)
print(t2.__dict__)

DataTable.__dict__.keys