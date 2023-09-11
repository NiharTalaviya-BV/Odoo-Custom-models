from odoo import models, fields

class Custom_Pos(models.Model):
    _name =  'store.location'
    _description = 'Custom Pos Model'
    _rec_name = 'location_name'

    location_name = fields.Char(string='Location Name')