class  Hello:
    def __init__(self,name):
        self.a=10
        self._b=20
        self.__c=30    #private method
    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()
    def private_method(self):
        print('private')
hello=Hello('name')
print(hello.a)
print(hello._b)
#print(hello.__c)   #private methods are not accessible outside the class
