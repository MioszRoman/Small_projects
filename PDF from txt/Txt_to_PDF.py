from fpdf import FPDF
import glob
from pathlib import Path

#Take every filepaths to .txt files
filepaths = glob.glob('txt/*.txt')

#Create a pdf file
pdf = FPDF(orientation='P', unit='mm', format="A4")

#Go through every text file
for filepath in filepaths:
    filename = Path(filepath).stem

    #Get the content from every text file
    with open(filepath, 'r') as file:
        content = file.read()
    #Create a pages for each text files
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    #Create a titles for each page
    pdf.cell(w=0, h=20, txt=filename.title(), ln=1)

    pdf.set_font(family='Times', size=12)
    #Give a content for each page
    pdf.multi_cell(w=0, h=6, txt=content)

#Create an output file
pdf.output("Output.pdf")
