from odoo import models, fields

class SchoolManagementTeachers(models.Model):
    _name = 'school.management.teachers'
    _description = 'Class Teachers'
    _rec_name = 'name'

    _sql_constraints = [
        ('unique_standard_division', 'unique(standard_division)', 'A class teacher already exists for this standard and division.'),
    ]

    name = fields.Char(string='Name')
    standard_division = fields.Char(string='Standard and Division')
    students_ids = fields.One2many('school.management', 'class_teacher_id', string='Students')
    country_id = fields.Many2one('res.country', string='Country')



    def assign_students(self, standard_division):
        students = self.env['school.management'].search([('standard_division', '=', standard_division)])
        self.students = students.id

    
    def name_get(self):
        print(self._context)
        result = []
        for record in self:
            if self._context.get('is_division'):
                name= record.standard_division 
                result.append((record.id, name))
            else:
                name = f"{record.name}"
                result.append((record.id, name))
        return result

    

        