import math
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class rectangle (polygon):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def sides(self):
        print(f'rectangle has 4 sides:lenth={self.length},width={self.width},lenth={self.length},width={self.width}')
    def area(self):
        print(f'area of the rectangle:{self.length * self.width}')
    def perimeter(self):
        return 2 * (self.length + self.width)
class square(polygon):
    def __init__(self,a):
        self.a=a
    def sides(self):
        print(f'square has 4 equal sides:{ self.a},{self.a},{self.a},{self.a}')
    def area(self):
        print(f'area of the square:{self.a * self.a}')
    def perimeter(self):
        print(f'perimeter of the square:{4 * self.a}')
import math
class triangle(polygon):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def sides(self):
        print(f'a traingle has 3 sides:{self.a},{self.b},{self.c}')
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def perimeter(self):
        print(f'perimeter of the triangle:{self.a + self.b + self.c}')

class rhombus(polygon):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def sides(self):
        print(f'rhombus s 4 equal sides:{self.base},{self.base},{self.base},{self.base}')
    def area(self):
        print(f'area of the rhombus:{self.base * self.height}')
    def perimeter(self):
        print(f'perimeter of the rhombus:{4 * self.base}')

rect:rectangle=rectangle(10,8)
rect.sides()
print("perimeter of the rectangle:",rect.perimeter())
rect.area()
print('******************************')

sqrt:square=square(8)
sqrt.sides()
sqrt.area()
sqrt.perimeter()
print("******************************")

tri:triangle=triangle(6,7,8)
print('area of the triangle:',tri.area())
tri.sides()
tri.perimeter()
print('*******************************')

rho:rhombus=rhombus(5,3)
rho.area()
rho.sides()
rho.perimeter()


