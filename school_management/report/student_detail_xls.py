import xlsxwriter
from odoo import models, fields, api
from io import BytesIO
import base64

class StudentXLSXReport(models.AbstractModel):
    _name = 'report.school_management.report_student_detail_xls'
    _description = 'Student XLSX Report'
    
    @api.model
    def _get_report_data(self):
        students = self.env['school.management'].search([])
        return students

    def generate_xlsx_report(self, data, objs):
        output = BytesIO()  # Create a binary stream to hold the XLSX content
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('students')
        header_format = workbook.add_format({'bold': True, 'bg_color': 'yellow'})

        headers = ['Name', 'Enrollment Number', 'Phone Number']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)

        for row, student in enumerate(objs, start=1):
            worksheet.write(row, 0, student.name)
            worksheet.write(row, 1, student.enrollment_number)
            worksheet.write(row, 2, student.phone_number)

        workbook.close()
        
        # Get the binary content from the BytesIO stream
        xls_content = output.getvalue()

        # Attach the XLSX content to the record
        self.write({
            'xls_report': base64.b64encode(xls_content),
            'xls_report_name': 'student_report.xlsx'  # You can change the name if needed
        })
