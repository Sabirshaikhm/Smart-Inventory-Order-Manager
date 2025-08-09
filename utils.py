from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import io

def generate_invoice_pdf(order, order_items, company_info=None):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    styles = getSampleStyleSheet()
    story = []

    title = 'sabir Hacker'
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1,6))
    story.append(Paragraph(f"Invoice ID: {order.id}", styles['Normal']))
    story.append(Paragraph(f"Customer: {order.customer_name}", styles['Normal']))
    story.append(Paragraph(f"Date: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1,12))

    data = [['Product', 'Qty', 'Unit (INR)', 'Total (INR)']]
    total = 0.0
    for it in order_items:
        line_total = it['price'] * it['qty']
        data.append([it['product_name'], str(it['qty']), f"{it['price']:.2f}", f"{line_total:.2f}"])
        total += line_total

    data.append(['', '', 'Grand Total', f"{total:.2f}"])

    table = Table(data, colWidths=[220,50,80,80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('ALIGN', (1,0), (-1,-1), 'CENTER'),
    ]))
    story.append(table)
    story.append(Spacer(1,12))
    story.append(Paragraph("Thank you for your order!", styles['Normal']))
    doc.build(story)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
