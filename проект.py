# создать базовый класс, сделать 3 подкласса, внутри классов было не менее 3 атрибутов, не менее 2 свойства, не менее 3 методов и был полиформизм
import datetime 
import random



class Mixin:
    def time(self):
        return datetime.datetime.now()


class Human(Mixin):
    def __init__(self):
        self.legs = 2
        self.arms = 2
        self.eyes = 2
        self.intellegent = True
        self.hair = True 

    @property
    def get_hair(self):
        return self.hair 
    
    @get_hair.setter 
    def get_hair(self, hair):
        if isinstance(hair, str) == True:
            self.hair = hair 
        else:
            raise ValueError('Ошибка в типе данных')
        
    @property 
    def get_intellegent(self):
        return self.intellegent
    
    @get_intellegent.setter
    def get_intellegent(self, intellegent):
        if isinstance(intellegent, int) or isinstance(intellegent, str) == True:
            self.intellegent = intellegent 
        else:
            raise ValueError('Ошибка в типе данных')
    
    def breath(self):
        return 'Дышим'
    
    def look(self):
        return 'Видим'
    
    def walk(self):
        return 'Хожу'
    
    def __del__(self):
        print('Объект был удален')
    

class Baby(Human):
    def __init__(self, old=0, height=50, weight=3):
        self.old = old 
        self.weight = weight 
        self.height = height 
    
    def breath(self):
        return 'Первый вздох'
    
    def look(self):
        return 'Первые картины мира'
    
    @property 
    def _old(self):
        return self.old 
    
    @_old.setter
    def _old(self, old):
        if isinstance(old, int) == True and 0 <= old <= 3:
            self.old = old 
        else:
            raise ValueError('Возраст должен быть в периоде 0 и 3 лет')
    
    @property
    def _height(self):
        return self.height 
    
    @_height.setter 
    def _height(self, height):
        if isinstance(height, int) == True:
            self.height = height 
        else:
            raise ValueError('Рост должен быть в цифрах')
        
    def walk(self):
        return 'Осваиваю первые шаги'
    
class Children(Baby):
    def __init__(self, old, height, weight, energy):
        super().__init__(old, height, weight)
        self.energy = energy
        self.happy = True 
        self.IQ = 50 

    def walk(self):
        return 'Хожу с энергией'
    
    def breath(self):
        return 'Дышу глубоко'
    
    def look(self):
        return 'Смотрю с любопытством'
    
    @property
    def _energy(self):
        return self.energy 
    
    @_energy.setter
    def _energy(self, energy):
        if isinstance(energy, str) == True:
            self.energy = energy
        else:
            raise ValueError('Тип данных должен быть str')
        
    @property 
    def _happy(self):
        return self.happy
    
    @_happy.setter 
    def _happy(self, happy):
        if isinstance(happy, str) == True:
            self.happy = happy 
        else:
            raise ValueError('Тип данных должен быть str')
        

# children = Children(12, 32, True, 45)
# print(children.time())

from dataclasses import dataclass
from typing import Any

@dataclass
class Human2():
    legs: int
    arms: int
    eyes: int
    intellegent: bool
    hair: int
    field: Any


h = Human2(2,2,2,True,False,"sfg")
q = Human2(1,2,2,True,False,"sfg")
print(h,q)




    # def __init__(self):
    #     self.legs = 2
    #     self.arms = 2
    #     self.eyes = 2
    #     self.intellegent = True
    #     self.hair = True 