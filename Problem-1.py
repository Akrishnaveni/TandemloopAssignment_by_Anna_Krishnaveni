#Problem-1 
class Calculator:
    def add(self,a:float,b:float)->float:
        return a+b
    def substract(self,a:float,b:float)->float:
        return a-b
    def multiply(self,a:float,b:float)->float:
        return a*b
    def divide(self,a:float,b:float)->float:
        if b==0:
            return "Error: Division by zero"
        else:
            return a/b


if __name__=="__main__":
calc=Calculator()
print(calc.add(5.3,3.6))
print(calc.substract(5.3,3.6))
print(calc.multiply(5.3,3.6))
print(calc.divide(5.3,3.6))
print(calc.divide(5.3,0))

