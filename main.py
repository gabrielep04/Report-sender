from data_reader import read_sales_data
from analysis import financial_analysis, sales_by_segment
from report_generator import generate_sales_plot, write_report
from whatsapp_sender import send_whatsapp_message

def main():
    # Leer datos y análisis
    df = read_sales_data('Ventas - Fundamentos.xlsx')
    analysis = financial_analysis(df)
    segment_sales = sales_by_segment(df)

    # Generar gráfica y reporte
    plot_path = generate_sales_plot(segment_sales)
    report_path = write_report(analysis, segment_sales, plot_path)

    # Enviar solo texto para evitar error por URL local
    with open(report_path) as f:
        report_text = f.read()
    sid = send_whatsapp_message(report_text)
    print(f'Reporte enviado con SID: {sid}')

if __name__ == '__main__':
    main()