from fpdf import FPDF

shirt = "shirtificate.png"

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")


pdf.add_page()
pdf.image(shirt, 10, 70, 190)

pdf.set_font("Helvetica", "B", 40)
pdf.cell(w=0, h=20, txt="CS50 Shirtificate", align="C")

pdf.set_font("Helvetica", "B", 36)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(w=-190, h=250, txt=f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
