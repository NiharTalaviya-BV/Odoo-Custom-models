from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InheritPosSession(models.Model):
    _inherit =  'pos.session'
    

    @api.model
    def _loader_params_res_partner(self):
        params = super(InheritPosSession, self)._loader_params_res_partner()
        params['search_params']['fields'].append('alternate_phone_num')
        return params
    
    def _loader_params_store_location(self):
        return {
            'search_params': {
                'fields': ['location_name'],
            },
        }
      
    @api.model
    def _pos_ui_models_to_load(self):
        models_to_load = super()._pos_ui_models_to_load()  
        models_to_load.append('store.location')
        return models_to_load

    def _loader_params_product_product(self):
        product = super()._loader_params_product_product()
        product.get('search_params').get('fields').append('qty_available')
        return product
    
    def _get_pos_ui_store_location(self, params):
        locations = list(self.env['store.location'].search_read(
            **params['search_params']))
        return locations
    