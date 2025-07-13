import pandas as pd

def financial_analysis(df: pd.DataFrame) -> dict:
    """
    Realiza un análisis financiero sobre la columna 'Precio Venta Real'.
    Devuelve un diccionario con:
      - total_sales: Ventas totales
      - avg_sales:   Venta promedio
      - stats:       Estadísticas descriptivas
    """
    sales_col = 'Precio Venta Real'
    return {
        'total_sales': df[sales_col].sum(),
        'avg_sales':   df[sales_col].mean(),
        'stats':       df[sales_col].describe()
    }

def sales_by_segment(df: pd.DataFrame) -> pd.Series:
    """
    Agrupa y suma las ventas por cada segmento.
    """
    return df.groupby('Segmento')['Precio Venta Real'].sum()