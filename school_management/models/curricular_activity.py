from odoo import models, fields

class ExtracurricularActivity(models.Model):
    _name = 'extracurricular.activity'
    _description = 'Extracurricular Activity'

    name = fields.Char(string='Name', required=True)
    color= fields.Integer(string='Color')