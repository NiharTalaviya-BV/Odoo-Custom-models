import io
import xlsxwriter

from odoo import models, fields, api


class StudentXLSXReport(models.AbstractModel):
    _name = 'report.school_management.report_student_detail_xls'
    _description = 'Student XLSX Report'
    _inherit= 'report.report_xlsx.abstract'

    @api.model
    def _get_report_data(self):
        students = self.env['school.management'].search([]) 
        return students

    def generate_xlsx_report(self, workbook, data, objs):
        print('vvvvvvvvvvvvvvvvv', data['students'])
        worksheet = workbook.add_worksheet('students')
        header_format = workbook.add_format({'bold': True, 'bg_color': 'yellow'})

        headers = ['Name', 'Enrollment Number', 'Phone Number']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_format)

        for row, student in enumerate(objs, start=1):
            worksheet.write(row, 0, student.name)
            worksheet.write(row, 1, student.enrollment_number)
            worksheet.write(row, 2, student.phone_number)
       
       
  