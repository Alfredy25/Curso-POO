from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass(order=True, frozen=True)
class Vuelo:
    nombre: str
    origen: str
    destino: str
    fecha_llegada: datetime
    cantidad_pasajeros: int

    def __str__(self):
        return (f'Vuelo(nombre={self.nombre}, origen={self.origen}, '
                f'destino={self.destino}, fecha_llegada={self.fecha_llegada.strftime('%d %b %Y %H:%M')}hrs, '
                f'cantidad_pasajeros={self.cantidad_pasajeros})')

vuelos: List[Vuelo] = [
    Vuelo('AAL 933','New York','Santiago',datetime(2021,8,29,5,39),62),
    Vuelo('LAT 755','Sao Paulo','Santiago',datetime(2021,8,31,4,45),47),
    Vuelo('SKU 621','Rio De Janeiro','Santiago',datetime(2021,8,30,16,0),52),
    Vuelo('DAL 147','Atlanta','Santiago',datetime(2021,8,29,13,22),59),
    Vuelo('AVA 241','Bogota','Santiago',datetime(2021,8,31,14,5),25),
    Vuelo('AMX 10','Mexico City','Santiago',datetime(2021,8,31,5,20),29),
    Vuelo('IBE 6833','Londres','Santiago',datetime(2021,8,30,8,45),55),
    Vuelo('LAT 2479','Frankfurt','Santiago',datetime(2021,8,29,7,41),51),
    Vuelo('SKU 803','Lima','Santiago',datetime(2021,8,30,10,35),48),
    Vuelo('LAT 533','Los Ángeles','Santiago',datetime(2021,8,29,9,14),59),
    Vuelo('LAT 1447','Guayaquil','Santiago',datetime(2021,8,31,8,33),31),
    Vuelo('CMP 111','Panama City','Santiago',datetime(2021,8,31,15,15),29),
    Vuelo('LAT 705','Madrid','Santiago',datetime(2021,8,30,8,14),47),
    Vuelo('AAL 957','Miami','Santiago',datetime(2021,8,29,22,53),60),
    Vuelo('ARG 5091','Buenos Aires','Santiago',datetime(2021,8,31,9,57),32),
    Vuelo('LAT 1283','Cancún','Santiago',datetime(2021,8,31,4,0),35),
    Vuelo('LAT 579','Barcelona','Santiago',datetime(2021,8,29,7,45),61),
    Vuelo('AAL 945','Dallas-Fort Worth','Santiago',datetime(2021,8,30,7,12),58),
    Vuelo('LAT 501','París','Santiago',datetime(2021,8,29,18,29),49),
    Vuelo('LAT 405','Montevideo','Santiago',datetime(2021,8,30,15,45),39),
]

vuelos = sorted(vuelos, key=lambda x: x.fecha_llegada, reverse=False)
print('... listado ordenado por fecha llegada ascendente ...')
for vuelo in vuelos:
    print(vuelo)
ultimo_vuelo = vuelos[-1]
print(f'El último vuelo en llegar {ultimo_vuelo}')
vuelo_menor_pasajeros = min(vuelos, key=lambda p: p.cantidad_pasajeros)
print(f'El vuelo con menor número de pasajeros es {vuelo_menor_pasajeros}')



