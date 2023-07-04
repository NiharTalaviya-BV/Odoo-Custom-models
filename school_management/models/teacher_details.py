from odoo import models, fields

class SchoolManagementTeachers(models.Model):
    _name = 'school.management.teachers'
    _description = 'Class Teachers'

    _sql_constraints = [
        ('unique_standard_division', 'unique(standard_division)', 'A class teacher already exists for this standard and division.'),
    ]

    name = fields.Char(string='Name')
    standard_division = fields.Char(string='Standard and Division')
    students_ids = fields.One2many('school.management', 'class_teacher_id', string='Students')


    def assign_students(self, standard_division):
        students = self.env['school.management'].search([('standard_division', '=', standard_division)])
        self.students = students
