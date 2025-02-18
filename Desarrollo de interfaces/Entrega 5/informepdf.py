from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Crear un nuevo PDF
c = canvas.Canvas("InformeVentas.pdf", pagesize=letter)

# Agregar título y datos
c.drawString(100, 750, "Reporte de Ventas - Marzo 2024")
c.drawString(100, 730, "Ventas Totales: $25,000")

# Agregar imagen del gráfico
c.drawImage("Grafico_Ventas.png", 100, 500, width=400, height=300)

# Guardar el PDF
c.save()
