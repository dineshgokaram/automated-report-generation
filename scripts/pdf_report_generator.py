from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf_report(summary, output_path):
    """Generates a PDF report from the data summary."""
    if summary:
        c = canvas.Canvas(output_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Automated Data Report")
        c.drawString(100, 730, "-" * 50)

        # Add summary details
        y = 710
        for key, value in summary.items():
            c.drawString(100, y, f"{key}: {value}")
            y -= 20

        c.save()
        print(f"PDF report generated at: {output_path}")
    else:
        print("No summary to include in the report.")
