import file_data as fd


def add_header(pdf, row):
    pdf.set_font(family="Arial", style='B', size=24)
    pdf.set_text_color(100, 100, 180)
    pdf.cell(w=0, h=12, txt=row[fd.TOPIC], align='L', ln=1)


def add_footer(pdf, row):
    pdf.ln(fd.PAGE_END)
    pdf.set_font(family="Arial", style="I", size=9)
    pdf.set_text_color(60, 70, 100)
    pdf.cell(w=0, h=12, txt=row[fd.TOPIC], align='R')


def add_lines(pdf):
    for y in range(fd.LINE_Y, fd.PAGE_END, 10):
        pdf.line(fd.LINE_X1, y, fd.LINE_X2, y)
