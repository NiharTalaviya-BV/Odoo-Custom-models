from odoo import models, fields

class Custom_Pos(models.Model):
    _name =  'custom.pos'
    _description = 'Custom Pos Model'

    name = fields.Char(string='Name')
    phone_number = fields.Char(string='Phone Number')

    




       
    