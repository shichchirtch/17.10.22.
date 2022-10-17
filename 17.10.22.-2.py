class CellException(Exception):
    """Класс для формирования общих исключений"""
class CellIntegerException(CellException):
    """Класс исключений для CellInteger"""
class CellFloatException(CellException):
    """Класс исключений для CellFloat"""
class CellStringException(CellException):
    """Класс исключений для CellString"""

class  CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value, self._max_value = min_value, max_value
        self._value = None

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, data):
        if not self._min_value < data <= self._max_value or not isinstance(data, int):
            raise CellIntegerException("значение выходит за допустимый диапазон")
        self._value = data

    def __str__(self):
        return f'{self._value}'

class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value, self._max_value = min_value, max_value
        self._value = None
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, data):
        if not self._min_value < data<= self._max_value or not isinstance(data, float):
            raise CellFloatException("значение выходит за допустимый диапазон")
        self._value = data

    def __str__(self):
        return f'{self._value}'

class CellString:
    def __init__(self, min_lenth, max_lenth):
        self._min_lenth, self.max_lenth = min_lenth, max_lenth
        self._value = None
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, data):
        if not self._min_lenth < len(data)<= self.max_lenth or not isinstance(data, str):
            raise CellStringException("значение выходит за допустимый диапазон")
        self._value = data

    def __str__(self):
        return f'{self.value}'

class TupleData:
    def __init__(self, *args):
        if not all(isinstance(x, (CellInteger, CellFloat, CellString )) for x in args):
            raise ValueError("Only certain objects")
        self.tup = (args)

    def __iter__(self):
        # print("iter works")
        for i in self.tup:
            yield i._value




    def __len__(self):
        if self.tup:
            return len(self.tup)
        return 0

    def __getitem__(self, item):
        return self.tup[item]._value

    def __setitem__(self, key, value):
        # print("setitem")
        self.tup[key]._value = value

d = CellInteger(1,5)
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
for x in ld:
    print(x)
try:
    print("try works")
    ld[0] = 1
    print(ld[0])
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
    print(ld[3])
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
