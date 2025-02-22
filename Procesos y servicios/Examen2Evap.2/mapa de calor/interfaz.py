import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

class HeatmapReport:
    def __init__(self, data: pd.DataFrame, output_dir="reports"):
        self.data = data
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_heatmap(self, filename="mapacalor.png"):
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.data, annot=True, cmap="coolwarm", fmt=".1f")
        heatmap_path = os.path.join(self.output_dir, filename)
        plt.savefig(heatmap_path)
        plt.close()
        return heatmap_path

    def generate_report(self, title="Mapa de Calor", filename="report.pdf"):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, title, ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, "Resumen estadístico", ln=True)
        pdf.ln(5)
        
        for col in self.data.columns:
            if pd.api.types.is_numeric_dtype(self.data[col]):
                stats = self.data[col].describe()
                pdf.cell(0, 10, f"{col}: Media={stats['mean']:.2f}, Desviación={stats['std']:.2f}", ln=True)
        pdf.ln(10)

        heatmap_path = self.generate_heatmap()
        pdf.image(heatmap_path, x=10, w=180)

        report_path = os.path.join(self.output_dir, filename)
        pdf.output(report_path)
        return report_path


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        entry_var.set(file_path)

def generate_report():
    file_path = entry_var.get()
    if not file_path:
        messagebox.showerror("Error", "Porfavor introduce un archivo CSV")
        return
    
    try:
        data = pd.read_csv(file_path)
        if "Timestamp" in data.columns:
            data = data.drop(columns=["Timestamp"])
        
        report = HeatmapReport(data)
        report_path = report.generate_report()
        messagebox.showinfo("Success", f"Reporte generado: {report_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error a la hora de generar el reporte: {e}")


root = tk.Tk()
root.title("Generador de mapas de calor")
root.geometry("400x200")

entry_var = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Selecciona el archivo CSV:").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(frame, textvariable=entry_var, width=40)
entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Buscar", command=select_file).grid(row=0, column=2, padx=5, pady=5)

tk.Button(root, text="Generar reporte", command=generate_report, width=20).pack(pady=20)

root.mainloop()
