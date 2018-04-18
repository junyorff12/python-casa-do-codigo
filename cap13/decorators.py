
class Column():
    def __index__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def other_name(self):
        return self._name


col = Column('Name')
col.other_name


