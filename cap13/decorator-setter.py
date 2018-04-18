class Column():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valor):
        raise Exception("Não pode mudar")

    @name.deleter
    def name(self):
        pass



col = Column('Name')
col.name = 'New name'
