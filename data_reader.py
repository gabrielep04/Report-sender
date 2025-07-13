import pandas as pd

def read_sales_data(path: str) -> pd.DataFrame:
    """
    Lee los datos de ventas desde un archivo Excel.
    Retorna un DataFrame con las ventas.
    """
    df = pd.read_excel(path, engine='openpyxl')
    return df