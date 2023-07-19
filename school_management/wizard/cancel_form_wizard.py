from odoo import models, fields

class CancelButtonWizard(models.TransientModel):
    _name = 'cancel.button.wizard'
    _description = 'Cancel Button Wizard'


    name_id = fields.Many2one('school.management', string='Name')


    def action_cancel_application(self):
        if self.name_id:
            self.name_id.status = 'left-school'
            self.name_id.save_all_data()
            
      
               



