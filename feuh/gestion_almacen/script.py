from feuh.gestion_almacen.models.fruta import Fruta
from feuh.gestion_almacen.models.lacteo import Lacteo
from feuh.gestion_almacen.models.limpieza import Limpieza
from feuh.gestion_almacen.models.no_perecible import NoPerecible
from feuh.gestion_almacen.models.producto import Producto

fruta1 = Fruta('Manzana Roja', 35, 1.2, 'Manzana', 'Roja')
fruta2 = Fruta('Plátano Tabasco',28,1.5,'Plátano', 'Amarillo')
lacteo1 = Lacteo('Leche entera Alpura',30, 1,3.5, 3.2)
lacteo2 = Lacteo('Yogur Natural Lala',18, 250,2.8, 4.0)
no_perecible1 = NoPerecible('Atún en lata Dolores', 20, 140,'Lata', 120)
no_perecible2 = NoPerecible('Frijoles Negros La Sierra', 25, 560,'Bolsa', 210)
limpieza1 = Limpieza('Limpiador Multiusos X', 45, ['Alcohol etílico','amonio cuaternario'],'Hogar',1)
limpieza2 = Limpieza('Desengrasante Industrial Pro', 120, ['Hidróxido de sodio','solventes'],'Industrial',2)

lista_products: Producto = [fruta1,fruta2,lacteo1,lacteo2,no_perecible1,no_perecible2,limpieza1,limpieza2]
for product in lista_products:
    print(product)

