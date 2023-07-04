from odoo import models, fields

class PreviousSchool(models.Model):
    _name = 'school.management.previous.school'
    _description = 'Previous Schools'

    name = fields.Char(string='Name', required=True)
    enrollment_number = fields.Char(string='Enrollment Number')
    admission_date = fields.Date(string='Admission Date')
    leaving_date = fields.Date(string='Leaving Date')
    student_id = fields.Many2one('school.management', string='Student')                         