from decimal import Decimal


class Relationsip:
    def __init__(self, name, _from, to, on):
        self.name = name
        self._from = _from
        self._to = to
        self._on = on


class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []
        self._references = []
        self._referenced = []

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        relationship = Relationsip(name, self, to, on)
        self._references.append(relationship)

    def add_refereced(self, name, by, on):
        relationship = Relationsip(name, by, self, on)
        self._referenced.append(relationship)

    '''
    Encapsulando com getter
    
    def getData(self):
        return self._data
    '''
    '''
    encapsulando com decorator
    '''
    @property
    def data(self):
        return self._data


class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {} ".format(self._name, self._kind, self._description)
        return _str

    def _validate(cls, kind,  data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

    validate = classmethod(_validate)


class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {} ".format(self._name, self._kind, self._description)
        return "{} - {} ".format('PK', _str)


# table1 = DataTable("TabelaTeste")
# print(table1.getData)

table2 = DataTable("TabelaTeste")
print(table2.data)
