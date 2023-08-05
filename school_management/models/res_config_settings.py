from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    global_setting = fields.Char(string='Global Setting', config_parameter='school_management.global_setting')


