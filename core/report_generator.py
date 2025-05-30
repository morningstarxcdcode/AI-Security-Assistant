"""
Report generator module for creating PDF reports with vulnerability charts.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import io

class ReportGenerator:
    def __init__(self):
        pass

    def generate_pdf_report(self, scan_results, output_path):
        """
        Generate a PDF report from scan results.
        Args:
            scan_results (dict): Aggregated scan results.
            output_path (str): File path to save the PDF report.
        """
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(1 * inch, height - 1 * inch, "AI Security Assistant Scan Report")

        c.setFont("Helvetica", 12)
        y = height - 1.5 * inch

        # Summary
        c.drawString(1 * inch, y, "Scan Summary:")
        y -= 0.3 * inch

        total_vulns = 0
        for target, results in scan_results.items():
            vulns = sum(len(r.get('vulnerabilities_found', [])) if isinstance(r, dict) else 0 for r in results.values())
            total_vulns += vulns
            c.drawString(1.2 * inch, y, f"Target: {target} - Vulnerabilities Found: {vulns}")
            y -= 0.2 * inch

        c.drawString(1 * inch, y, f"Total Vulnerabilities Found: {total_vulns}")
        y -= 0.5 * inch

        # Generate vulnerability chart
        targets = list(scan_results.keys())
        vuln_counts = []
        for target in targets:
            results = scan_results[target]
            count = sum(len(r.get('vulnerabilities_found', [])) if isinstance(r, dict) else 0 for r in results.values())
            vuln_counts.append(count)

        plt.figure(figsize=(6, 3))
        plt.bar(targets, vuln_counts, color='red')
        plt.title('Vulnerabilities per Target')
        plt.xlabel('Target')
        plt.ylabel('Number of Vulnerabilities')
        plt.tight_layout()

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='PNG')
        plt.close()
        img_buffer.seek(0)

        from PIL import Image
        img = Image.open(img_buffer)

        c.drawInlineImage(img, 1 * inch, y - 3 * inch, width=6 * inch, height=3 * inch)

        c.showPage()
        c.save()
