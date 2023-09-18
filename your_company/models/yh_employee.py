from odoo import models, fields


class YourHomeEmployees(models.Model):
    _name = 'yh.employees'
    _description = 'Your Employees'

    employee_name = fields.Char()
    email = fields.Char()
    phone_number = fields.Char()
    experience = fields.Char()
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=?', country_id)]", string='City/State')
    description = fields.Text()
    image = fields.Binary()

