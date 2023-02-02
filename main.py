from fpdf import FPDF
import pandas as pd

TOPIC_FILE = "topics.csv"
HEADER = "Topic"
OUTPUT_FILE = "output.pdf"

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv(TOPIC_FILE)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style='B', size=24)
    pdf.set_text_color(100, 100, 180)
    pdf.cell(w=0, h=12, txt=row[HEADER], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

pdf.output(OUTPUT_FILE)
