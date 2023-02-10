class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, numero1: int, numero2: int) -> int or None or str:
        try:
            result = 0
            if numero1 > numero2:
                result = numero1
            elif numero2 > numero1:
                result = numero2
            else:
                result = None
            return result
        except TypeError as e:
            result = "Introduce solo caracteres"
            return result
        except Exception as e:
            print("An exception occurred:", str(e))


"""mayor_objeto = Mayor()
resultado = mayor_objeto.mayor(100, 2.2)
print(resultado)

    def mayor(self, numero1: Union[int, float], numero2: int) -> Union[int, float, None, str]:
    
git branch -M main
git remote add origin 
git push -u origin main

"""


