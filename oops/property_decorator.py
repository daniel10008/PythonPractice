class Temperature:
    def __init__(self, celsius):
        self.__celsius=celsius
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self,celsius):
        self.__celsius=celsius
    @property
    def celsius(self):
        return self.__celsius
    @celsius.setter
    def celsius(self,value):
        self.__celsius=value
    @celsius.deleter
    def celsius(self):
        del self.__celsius
temp=Temperature(31.5)
temp.set_celsius(51.3)
temp.celsius=60
del temp.celsius
print(temp.celsius)
