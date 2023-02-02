from fpdf import FPDF
import pandas as pd
import file_data as fd
import functions as f

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv(fd.TOPIC_FILE)

for index, row in df.iterrows():
    pdf.add_page()
    f.add_header(pdf, row)
    f.add_lines(pdf)
    f.add_footer(pdf, row)

    for i in range(row[fd.PAGES] - 1):
        pdf.add_page()
        f.add_lines(pdf)
        f.add_footer(pdf, row)

pdf.output(fd.LINED_OUTPUT_FILE)
