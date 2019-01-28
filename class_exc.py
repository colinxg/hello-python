import random


class RandomNumber:
    def __init__(self, count=1, start=0, stop=100):
        self._count = count
        self._mix = start
        self._max = stop

    def getnumber(self):
        return [random.randint(self._mix, self._max) for _ in range(self._count)]

    def setvalue(self, count, start=0, stop=100):
        self._count, self._mix, self._max = count, start, stop

    def getvalue(self):
        print('zhe count is {} \nzhe value be "{}" to "{}"'.format(self._count, self._mix, self._max))

    a = property(getvalue, setvalue)


# a = RandomNumber(10)
# print(a.getnumber())
# a.getvalue()
# a.a = 10
# a.a
#
# b = tuple(zip(a.getnumber(), a.getnumber()))
# print(b)


# class CarInfo:
#     def __init__(self, mark, color, price, speed):
#         self.mark = mark
#         self.color = color
#         self.price = price
#         self.speed = speed
#
#
# a = CarInfo('aodi', 'red', '20W', '180km/h')


class CarInfo:
    CARPORT = []

    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


    @classmethod
    def savecarinfo(cls, instance):
        cls.CARPORT.append(instance)

    @classmethod
    def getcarinfor(cls):
        return cls.CARPORT



# a = CarInfo('aodi', 'red', '20W', '180km/h')
#
#
# CarInfo.savecarinfo(a)
# print(CarInfo.getcarinfor())


class ConvertT:
    def __init__(self, T, type='C'):
        if type == 'C':
            self._TC = T
            self._TF = 9*T/5 + 32
            self._TK = T + 273.15
        if type == 'F':
            self._TC = (T - 32)*5/9
            self._TF = T
            self._TK = (T - 32)*5/9 + 273.15
        if type == 'K':
            self._TC = T - 273.15
            self._TF = (T - 273.15)*9/5 +32
            self._TK = T
        else:
            print('zhe Type must be C、F、K')


    def getC(self): return self._TC
    def getF(self): return self._TF
    def getK(self): return self._TK

    
