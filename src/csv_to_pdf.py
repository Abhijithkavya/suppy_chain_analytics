import csv
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "reports"

OUTPUT_DIR.mkdir(exist_ok=True)

# Read all CSV files
for csv_file in DATA_DIR.glob("*.csv"):

    pdf_file = OUTPUT_DIR / (csv_file.stem + ".pdf")

    with open(csv_file, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows:
        print("Empty file:", csv_file.name)
        continue

    # Create PDF
    pdf = SimpleDocTemplate(
        str(pdf_file),
        pagesize=landscape(A4),
        rightMargin=25,
        leftMargin=25,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    elements.append(
        Paragraph(csv_file.stem.title(), styles["Title"])
    )
    elements.append(Spacer(1, 0.2 * inch))

    table = Table(rows, repeatRows=1)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.lightgrey])
    ]))

    elements.append(table)
    pdf.build(elements)

    print("PDF Created:", pdf_file.name)

print("\nAll CSV files converted successfully!")