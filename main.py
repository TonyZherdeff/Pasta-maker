from abc import ABC, abstractmethod
import random as r


class Pasta_Type(ABC):
    @abstractmethod
    def set_up(self):
        pass


class Spaghetti(Pasta_Type):
    def set_up(self):
        print('For Pasta used Spaghetti pasta!')


class Maccheroni(Pasta_Type):
    def set_up(self):
        print('For Pasta used Maccheroni pasta!')


class Ditalini(Pasta_Type):
    def set_up(self):
        print('For Pasta used Ditalini pasta!')


class Bolognese(Pasta_Type):
    def set_up(self):
        print('For Pasta used Bolognese sauce!')


class Carbonara(Pasta_Type):
    def set_up(self):
        print('For Pasta used Carbonara sauce!')


class Mushroom(Pasta_Type):
    def set_up(self):
        print('For Pasta used Mushroom sauce!')


class Tabasco(Pasta_Type):
    def set_up(self):
        print('Tabasco is added to Pasta!')


class Garlic(Pasta_Type):
    def set_up(self):
        print('Garlic is added to Pasta!')


class Basilico(Pasta_Type):
    def set_up(self):
        print('Basilico is added to Pasta!')


class No_Additions(Pasta_Type):
    def set_up(self):
        print('No additions were added to Pasta!')


class Main_Factory(ABC):
    @abstractmethod
    def get_type_ing(self: int):
        pass


class Pasta_Factory(Main_Factory):
    def get_type_ing(self: int):
        if self == 0:
            sp = Spaghetti()
            return sp.set_up()
        elif self == 1:
            mc = Maccheroni()
            return mc.set_up()
        elif self == 2:
            dt = Ditalini()
            return dt.set_up()


class Sauce_Factory(Main_Factory):
    def get_type_ing(self: int):
        if self == 0:
            bl = Bolognese()
            return bl.set_up()
        elif self == 1:
            cb = Carbonara()
            return cb.set_up()
        elif self == 2:
            ms = Mushroom()
            return ms.set_up()


class Additions_Factory(Main_Factory):
    def get_type_ing(self: int):
        if self == 0:
            tb = Tabasco()
            return tb.set_up()
        elif self == 1:
            gc = Garlic()
            return gc.set_up()
        elif self == 2:
            bs = Basilico()
            return bs.set_up()
        elif self == 3:
            na = No_Additions()
            return na.set_up()


class Producer_Factory:
    def get_factory(self, type_of_factory):
        if type_of_factory == 'Pasta':
            return Pasta_Factory.get_type_ing(r.randint(0, 2))
        elif type_of_factory == 'Sauce':
            return Sauce_Factory.get_type_ing(r.randint(0, 2))
        elif type_of_factory == 'Additions':
            return Additions_Factory.get_type_ing(r.randint(0, 3))


print("Hello! It's a random Pasta generator!\n"
      "So, let's generate your own random Pasta!\n"
      "That's your Pasta:")
ing1 = Producer_Factory()
ing1.get_factory('Pasta')
ing1.get_factory('Sauce')
ing1.get_factory('Additions')
print('Buon Appetito!')
