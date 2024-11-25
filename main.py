from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# Path to the PDF certificate template
template_path = '/workspaces/certificate-workbook/files/BKC_Completion Certificate.pdf'

# List of student names
student_names = [
"Amirah Yakubu"
]



def create_certificate(template_path, student_name, output_path):
    # Create a canvas to draw text on
    c = canvas.Canvas(output_path)
    
    # Set the font and size
    c.setFont("Helvetica-Bold", 30)
    
    # Add the student name at the desired position
    # Adjust the position (x, y) based on your template

    # short names 
    c.drawString(300, 280, student_name)

    # #long names
    # c.drawString(180, 280, student_name)

    # Save the canvas as a temporary PDF
    c.save()
    
    # Read the original template
    template_pdf = PdfReader(template_path)
    template_page = template_pdf.pages[0]
    
    # Read the temporary PDF with the student name
    temp_pdf = PdfReader(output_path)
    temp_page = temp_pdf.pages[0]
    
    # Merge the temporary PDF onto the template
    template_page.merge_page(temp_page)
    
    # Write the output PDF
    writer = PdfWriter()
    writer.add_page(template_page)
    with open(output_path, 'wb') as f:
        writer.write(f)

# Generate certificates for each student
for student_name in student_names:
    output_path = f'/workspaces/certificate-workbook/output/{student_name.replace(" ", "_")}.pdf'
    create_certificate(template_path, student_name, output_path)
    print(f"Created certificate for {student_name}")
