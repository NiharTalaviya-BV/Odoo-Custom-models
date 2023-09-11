from odoo import models, fields

class SaleLocation(models.TransientModel):
    _inherit =  'res.config.settings'

    available_location_id = fields.Many2many(
        related='pos_config_id.store_location_id',  
        string='Store Location',  
        readonly = False 
    )

class PosLocation(models.Model):
    _inherit = 'pos.config'

    store_location_id = fields.Many2many('store.location', string="Store Locations")
    




       
    