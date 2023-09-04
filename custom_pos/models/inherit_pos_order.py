from functools import partial
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InheritPos(models.Model):
    _inherit = 'pos.order'
    

    order_note = fields.Char(string='Phone Number')
 

    @api.model
    def _order_fields(self, ui_order):
        process_line = partial(self.env['pos.order.line']._order_line_fields, session_id=ui_order['pos_session_id'])
        order_vals = super(InheritPos, self)._order_fields(ui_order)
        order_vals.update({
            'order_note': ui_order.get('customer_order_note', ''),
        })
        return order_vals
    
    # @api.constrains('phone_number')
    # def _check_unique_phone_number(self):
    #     for customer in self:
    #         # Check if there are other customers with the same phone number
    #         existing_customers = self.search([('phone_number', '=', customer.phone_number)])
    #         if len(existing_customers) > 1:
    #             raise ValidationError("Phone number must be unique for each customer!")
            