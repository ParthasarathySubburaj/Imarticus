class calculator():
    
    company = "CASIO"
    
    def __init__(self,color,price):
        self.color = color
        self.price = price
        
    def addition(self,a,b):
        c = a+b
        return c
    
    def subtraction (self,a,b):
        c = a-b
        return c
    
    def multiplication (self,a,b):
        c = a*b
        return c
    
    def division (self,a,b):
        c = a/b
        return c
    
    @classmethod
    def set_company (cls, name):
        cls.comapny = name
		
class scientific_calcultor(calculator):
    
    def __init__(self,color, price, level):
        self.color = color
        self.price = price
        self.level = level
        
    def fact (self, n):
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result
    
    def fibo (self, n):
        a = 1
        b = 1
        i = 3
        series = [1,1]
        while i <= n:
            c = a+b
            a = b
            b = c
            i = i+1
            series.append(c)
        return series