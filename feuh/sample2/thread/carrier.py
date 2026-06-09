import pandas as pd
from dataclasses import dataclass

@dataclass
class Carrier:
    file_path: str
    colums_fedex = ["Rastreo", "Estado", "Fecha de envío", "Detalles", "FechaUltimoEvento"]
    filtro = "Estado == 'De regreso al establecimiento de FedEx' or Estado == 'Excepción de entrega' or Estado == 'Hemos intentado entregarlo' or Estado == 'Intentamos hacer la entrega'"
    formato_fecha = ''
    df_fedex = pd.DataFrame()
    name: str = 'FedEx'

    def process(self) -> pd.DataFrame:
        self.df_fedex = self.read()
        self.df_fedex = self.filter(self.df_fedex)
        self.df_fedex = self.clean(self.df_fedex)
        return self.df_fedex

    def read(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        self.formato_fecha = "%m/%d/%y" if "Número de rastreo" in df.columns else "%d/%m/%Y"
        return df

    def filter(self, df: pd.DataFrame) -> pd.DataFrame:
        df.rename(columns={
            df.columns[0]: "Rastreo",
            "Estado ": "Estado",
            "Estado con detalles ": "Detalles",
            "Fecha de tránsito estándar ": "FechaUltimoEvento",
            "Fecha de envío ": "Fecha de envío"
        },
            inplace=True)

        return df.query(self.filtro)[self.colums_fedex]

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df_fedex = df
        df_fedex['Fecha de envío'] = pd.to_datetime(
            df_fedex['Fecha de envío'],
            format="%m/%d/%y",
            errors="coerce"
        )
        df_fedex.dropna(subset=["Fecha de envío"], inplace=True)
        df_fedex.sort_values(by=["Fecha de envío"], ascending=False, inplace=True)
        df_fedex['FechaUltimoEvento'] = pd.to_datetime(
            df_fedex['FechaUltimoEvento'],
            format=self.formato_fecha,
            errors="coerce"
        )
        df_fedex["Rastreo"] = df_fedex["Rastreo"].astype(str)
        df_fedex["Guia"] = (
            df_fedex["Rastreo"].astype(str).str.replace(r"(\d{4})(\d{4})(\d{4})", r"\1 \2 \3", regex=True)
        )
        df_fedex = df_fedex[["Guia", "Estado", "Detalles", "FechaUltimoEvento", "Fecha de envío"]]
        df_fedex.rename(columns={"Fecha de envío": "FechaEnvio"}, inplace=True)
        return df_fedex