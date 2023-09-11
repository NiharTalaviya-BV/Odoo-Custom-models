from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartnerLoader(models.Model):
    _inherit =  'res.partner'
    
    alternate_phone_num = fields.Char(string='Alternet Phone Number')





   
