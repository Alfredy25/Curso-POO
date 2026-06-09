from datetime import date
from pathlib import Path
from queue import Queue
import pandas as pd

from feuh.sample2.thread.carrier import Carrier
from feuh.sample2.thread.worker import CarrierWorker


def flujo_completo():
    queue = Queue()
    fecha_hoy = date.today()
    fecha_hoy = fecha_hoy.strftime("%d-%m-%Y")
    rutas = []
    ruta_home = Path.home()
    ruta_compartida = "OneDrive - FGC\\Archivos de Stefano Mendoza - AutoTracking\\AHH_SIS_DOCUMENT´S\\PAD"
    rutas_paqueterias = [
        f"DHL\\DHL {fecha_hoy}.csv",
        f"FEDEX\\DataExportFEDEX_{fecha_hoy}.csv",
        f"PaqueteExpress\\descarga_PE\\paquetesEnviados {fecha_hoy}.xls",
        f"UPS\\UPS_DescargaWeb\\UPSData {fecha_hoy}.csv"
    ]

    rutas = [Path(ruta_home, ruta_compartida, r) for r in rutas_paqueterias]

    ruta_dhl = rutas[0]
    ruta_fedex = rutas[1]
    ruta_px = rutas[2]
    ruta_ups = rutas[3]

    print("\n".join(map(str, rutas)))

    carriers = [
        Carrier(str(ruta_fedex)),
    ]

    workers = [CarrierWorker(queue, carrier) for carrier in carriers]

    for w in workers:
        w.start()

    # esperar resultados
    results = [queue.get() for _ in workers]
    dfs = [r["data"] for r in results if r["success"]]
    errors = [r for r in results if not r["success"]]

    # esperar a que terminen los hilos
    for w in workers:
        w.join()
    if dfs:
        df_exceptions = pd.concat(dfs, ignore_index=True)
        print(df_exceptions.info())
    if errors:
            for e in errors:
                print(f"Error en Carrier: {e['carrier']}\n"
                      f"El error es el siguiente: {e['error']}")

if __name__ == "__main__":
    flujo_completo()
    input('Finalizado... ')




