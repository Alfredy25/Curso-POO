from feuh.sample.oop.generic.bolsaSupermercado.bolsa import BolsaSupermercado
from feuh.sample.oop.generic.bolsaSupermercado.clases_hijas import Fruta, Lacteo, Limpieza, NoPerecible

bolsa_fruta = BolsaSupermercado[Fruta]()
bolsa_lacteos = BolsaSupermercado[Lacteo]()
bolsa_limpieza = BolsaSupermercado[Limpieza]()
bolsa_no_perecible = BolsaSupermercado[NoPerecible]()

bolsa_fruta.add_producto(Fruta("Manzana Roja", 30.0, 1.2, "Roja"))
bolsa_fruta.add_producto(Fruta("Plátano", 18.5, 1.5, "Amarillo"))
bolsa_fruta.add_producto(Fruta("Naranja", 22.0, 2.0, "Naranja"))
bolsa_fruta.add_producto(Fruta("Uvas", 40.0, 0.8, "Morado"))
bolsa_fruta.add_producto(Fruta("Pera", 28.0, 1.3, "Verde"))

print('Bolsa de frutas')
for f in bolsa_fruta:
    print(f)
print()


bolsa_lacteos.add_producto(Lacteo("Leche Entera", 25.5, 10, 8))
bolsa_lacteos.add_producto(Lacteo("Queso Manchego", 80.0, 5, 25))
bolsa_lacteos.add_producto(Lacteo("Yogur Natural", 15.0, 20, 5))
bolsa_lacteos.add_producto(Lacteo("Mantequilla", 45.0, 8, 1))
bolsa_lacteos.add_producto(Lacteo("Crema", 35.5, 6, 2))

print('Bolsa de Lacteos')
for l in bolsa_lacteos:
    print(l)
print()

bolsa_limpieza.add_producto(Limpieza("Cloro", 20.0, "hipoclorito", 1.0))
bolsa_limpieza.add_producto(Limpieza("Detergente Líquido", 45.0, "tensioactivos", 2.0))
bolsa_limpieza.add_producto(Limpieza("Desinfectante", 35.0, "amonio cuaternario", 1.5))
bolsa_limpieza.add_producto(Limpieza("Limpiador Multiusos", 30.0, "alcohol", 1.2))
bolsa_limpieza.add_producto(Limpieza("Jabón Líquido", 25.0, "glicerina", 0.9))

print('Bolsa de Limpieza')
for limp in bolsa_limpieza:
    print(limp)
print()

bolsa_no_perecible.add_producto(NoPerecible("Arroz", 20.0, 1000, 1300))
bolsa_no_perecible.add_producto(NoPerecible("Fideos", 18.0, 900, 1200))
bolsa_no_perecible.add_producto(NoPerecible("Lentejas", 22.0, 800, 1100))
bolsa_no_perecible.add_producto(NoPerecible("Atún en lata", 35.0, 300, 400))
bolsa_no_perecible.add_producto(NoPerecible("Frijoles", 25.0, 850, 1150))

print('Bolsa de No perecibles')
for no_perecible in bolsa_no_perecible:
    print(no_perecible)
print()
