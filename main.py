from fpdf import FPDF
import pandas as pd

TOPIC_FILE = "topics.csv"
TOPIC = "Topic"
PAGES = "Pages"
OUTPUT_FILE = "output.pdf"

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv(TOPIC_FILE)


def add_footer():
    pdf.ln(260)
    pdf.set_font(family="Arial", style="I", size=9)
    pdf.set_text_color(60, 70, 100)
    pdf.cell(w=0, h=10, txt=row[TOPIC], align='R')


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Arial", style='B', size=24)
    pdf.set_text_color(100, 100, 180)
    pdf.cell(w=0, h=12, txt=row[TOPIC], align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

    add_footer()

    for i in range(row[PAGES] - 1):
        pdf.add_page()
        add_footer()

pdf.output(OUTPUT_FILE)
