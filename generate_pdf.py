import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class ExpensesPDFGenerator:
    def __init__(self):
        self.json_file = "expenses.json"
        self.output_pdf = "expenses_report.pdf"
        self.data = self.read_json_data()

    def read_json_data(self):
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def generate_pdf(self):
        categories = self.group_by_category(self.data)

        doc = SimpleDocTemplate(self.output_pdf, pagesize=letter)
        elements = []

        all_data = []
        grand_total = 0

        for category, items in categories.items():
            category_total = 0
            category_data = []

            category_data.append([category.capitalize()])
            category_data.append(["Date", "Description", "Amount"])
            
            for item in items:
                category_data.append([item["date"], item["description"], f"{item['amount']:,.2f} rs"])
                category_total += item["amount"]

            category_data.append(["", "Category Total", f"{category_total:,.2f}/- rs"])
            all_data.extend(category_data)

            grand_total += category_total

        all_data.append(["", "Grand Total", f"{grand_total:,.2f}/- rs"])

        table = Table(all_data)
        table.setStyle(self.get_table_style())

        elements.append(table)

        doc.build(elements)

    def group_by_category(self, data):
        categories = {}
        for entry in data:
            category = entry["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(entry)
        return categories

    def get_table_style(self):
        return TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 10),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (1, 1), (2, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ])
