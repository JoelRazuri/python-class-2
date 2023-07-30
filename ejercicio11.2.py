"""
    a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
    asignan en el constructor, y se imprimen como X/Y en el método __str__.
    b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
    con la suma de ambas.
    c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
    con el producto de ambas.
    d) Crear un método __simp__ que modifica la fracción actual de forma que los valores
    del dividendo y divisor sean los menores posibles.
"""


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


class Fraccion:
    def __init__(self,dividendo,divisor):
        self.dividendo = dividendo
        self.divisor = divisor

    def __str__(self):
        
        return (f"{self.dividendo}/{self.divisor}")
    
    def __add__(self,fraccion1,fraccion2):
        
        if (fraccion2.divisor == fraccion1.divisor):
            dividendo = fraccion2.dividendo + fraccion1.dividendo
            divisor = fraccion2.divisor
            fraccion_suma= Fraccion(dividendo,divisor)
        else:
            mcm = minimo_comun_multiplo(fraccion2.divisor,fraccion1.divisor)
            dividendo = (mcm/fraccion2.divisor*fraccion2.dividendo) + (mcm/fraccion1.divisor*fraccion1.dividendo)
            fraccion_suma = Fraccion(int(dividendo),int(mcm))
        
        return fraccion_suma

    # def __mul__(self,fraccion1,fraccion2):
    
    
    def __simp__(self,fraccion):

        mcd = maximo_comun_divisor(fraccion.dividendo,fraccion.divisor)
        
        if ((mcd) > 1):
            fraccion.dividendo = int(fraccion.dividendo / mcd)
            fraccion.divisor = int(fraccion.divisor / mcd)

        return fraccion




fraccion_1 = Fraccion(3,9)
fraccion_2 = Fraccion(4,9)
fraccion_4 = Fraccion(1,4)

fraccion_3 = fraccion_1.__add__(fraccion_1,fraccion_2)
fraccion_5 = fraccion_4.__add__(fraccion_4,fraccion_1)

print(f"{fraccion_1} + {fraccion_2} = {fraccion_3}")
print("--------------------")
print(f"{fraccion_4} + {fraccion_1} = {fraccion_5}")
print("--------------------")
print(f"Simplificado: {fraccion_5 .__simp__(fraccion_5)}")
print(f"Simplificado: {fraccion_2 .__simp__(fraccion_2)}")

