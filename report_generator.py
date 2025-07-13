import matplotlib.pyplot as plt
from pathlib import Path

def generate_sales_plot(series, output_path: str = 'segment_sales.png') -> str:
    """
    Dibuja un gráfico de barras de ventas por segmento.
    """
    fig, ax = plt.subplots()
    series.plot(kind='bar', ax=ax)
    ax.set_title('Ventas por Segmento')
    ax.set_ylabel('Ventas ($)')
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)
    return output_path

def write_report(analysis_results: dict, segment_sales, plot_path: str,
                 output_path: str = 'report.txt') -> str:
    """
    Crea un documento de texto con:
      - Ventas totales y promedio formateados en $.
      - Estadísticas descriptivas.
      - Ventas por segmento con símbolo $.
      - Ruta del gráfico.
    """
    total = analysis_results['total_sales']
    avg = analysis_results['avg_sales']
    stats = analysis_results['stats']

    segment_fmt = segment_sales.map(lambda x: f"${x:,.0f}")

    with open(output_path, 'w') as f:
        f.write('=== Reporte de Ventas ===\n')
        f.write(f"Ventas totales: ${total:,.0f}\n")
        f.write(f"Venta promedio: ${avg:,.2f}\n\n")
        f.write('--- Estadísticas Descriptivas ---\n')
        f.write(stats.to_string(float_format='{:,.2f}'.format))
        f.write('\n\n--- Ventas por Segmento ---\n')
        f.write(segment_fmt.to_string())
    return output_path