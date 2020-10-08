class Polygon:
    __width=None
    __height=None
    def set_value(self,width,height):
        self.__width=width
        self.__height=height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()
class Triangle(Polygon):
    def area(self):
        return self.get_width()*self.get_height()/2
rect=Rectangle()
tri=Triangle()
rect.set_value(30,10)
tri.set_value(20,20)
print(rect.area())
print(tri.area())