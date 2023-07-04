from odoo import models, fields


class CountryName(models.Model):
    _name = 'country.name'
    _description = 'Country Name'
    _rec_name = 'country'
    
    country = fields.Char(string='Country Name')    
   
