from reportlab.pdfgen import canvas

# Crear un PDF
c = canvas.Canvas("InformeVentas.pdf")
c.drawString(100, 750, "Reporte de Ventas - Marzo 2024")
c.save()
