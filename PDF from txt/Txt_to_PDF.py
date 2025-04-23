from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob('txt/*.txt')

pdf = FPDF(orientation='P', unit='mm', format="A4")


for filepath in filepaths:
    filename = Path(filepath).stem

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=20, txt=filename.title(), ln=1)

    pdf.set_font(family='Times', size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("Output.pdf")
