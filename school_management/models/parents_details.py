from odoo import models, fields

class Parents(models.Model):
    _name = 'school.management.parents'
    _description = 'Parents'

    name = fields.Char(string='Name', required=True)
    relation = fields.Char(string='Relation with Student')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    student_id = fields.Many2one('school.management', string='Student')