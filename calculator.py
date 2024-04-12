class Calculator:
    def addition(self,a,b):
        result= a+b
        return result
        
    def substraction(self,a,b):
        result=a-b
        return result

    def division(self,a,b):
        if b == 0:
            raise ValueError("Division by 0.")
        result=a/b
        return result
calculator=Calculator()