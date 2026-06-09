from feuh.sample.oop.abstractclass.catalogo.TvLcd import TvLcd
from feuh.sample.oop.abstractclass.catalogo.comics import Comic
from feuh.sample.oop.abstractclass.catalogo.iphone import Iphone
from feuh.sample.oop.abstractclass.catalogo.libro import Libro
from datetime import datetime

productos = [
    Libro(399,datetime(2015,6,23),"Haruki Murakami",'Kafka en la orilla','Tusquets'),
    Libro(289.54,datetime(2019,3,10,14),"Yuval Noah Harari","Sapiens: De animales a dioses","Debate"),
    Comic(150.75,datetime(2021,8,15),"Stan Lee","The Amazing Spider-Man #1","Marvel Comics","Spider-Man"),
    TvLcd('Sony',20000,32),
    Iphone('Apple', 21999,'Negro espacial','Iphone 14'),
    Iphone('Apple', 25999,'Azul','Iphone 15 pro')
]

for p in productos:
    print(f'Tipo de: {type(p).__name__}')
    print(p)
    print(f'Precio de Venta: ${p.get_precio_venta():.2f}\n')




