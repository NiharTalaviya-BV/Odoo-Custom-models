from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InheritPosSession(models.Model):
    _inherit =  'pos.session'
    
    @api.model
    def _loader_params_res_partner(self):
        params = super(InheritPosSession, self)._loader_params_res_partner()
        params['search_params']['fields'].append('alternate_phone_num')
        return params
