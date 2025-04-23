from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob('txt/*.txt')

pdf = FPDF(orientation='P', unit='mm', format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=20, txt=filename.title())

pdf.output("Output.pdf")
