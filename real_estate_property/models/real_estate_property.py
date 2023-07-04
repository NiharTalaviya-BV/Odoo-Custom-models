from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    
   

    name = fields.Char(string='Name')
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    zip = fields.Char(string='Zip')
    country_id = fields.Many2one('country.name', string='Country')
    property_type_id = fields.Many2one('property.type',
        string='Property Type',
        domain="[('name', '=', 'Residential')]")
    listing_date = fields.Date(string='Listing Date')
    listing_price = fields.Float(string='Listing Price')
    status = fields.Selection([ 
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('under_contract', 'Under Contract')],
        string='Status')
    agent_id = fields.Many2one('res.partner', string='Agent')
    property_size = fields.Float(string='Size')
    lot_size = fields.Float(string='Lot Size')
    year_built = fields.Integer(string='Year Built')
    amenities = fields.Text(string='Amenities')
    # image_name = fields.Char(string='Image Detail')
    property_image = fields.One2many('property.image', 'property_image_id', string = 'Proprty_Image')
    property_document = fields.One2many('property.document', 'document_id', string= 'Documents')
    # property_tag_name = fields.Char(string='Property Name')
    # property_tag = fields.Many2many('property.tag', string = 'tag')
    sequence_number = fields.Char(string='Sequence Number', readonly=True, copy=False)
    property_rent_date = fields.Date(string='Rent Date')
   
   

    _sql_constraints = [
        ('zip_check', 'CHECK(zip ~ \'^\\d+$\' AND length(zip) <= 6)', 'Zip should contain only numeric values and have a maximum length of 6!')
    ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'sequence_number' not in vals:
               vals['sequence_number'] = self.env['ir.sequence'].next_by_code('real.estate.property.sequence') or '/'
               return super(RealEstateProperty, self).create(vals)

   
    # def unlink(self):
    #     for record in self:
    #         if record.status != 'sold':
    #             raise ValidationError('You cannot delete this record. Status must be "Sold" to delete the record.')
    #     return super(RealEstateProperty, self).unlink()

     
    def custom_action(self):
        for record in self:
            print(record.name)
            record.status = 'active'

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Action Completed',
                'message': 'Custom action performed successfully.',
                'sticky': False,
            },
        }
    
    @api.depends('country_id')
    def _compute_state(self):
        for record in self:
            if record.country_id:
                record.state_id = record.country_id.default_state_id.id

    
    @api.onchange('property_size')
    def onchange_size(self):
        if self.lot_size and self.property_size:
            self.property_size = self.lot_size - self.property_size

    # @api.model
    # def search(self, domain, offset=0, limit=None, order=None, count=False):
    #     res = self._search(domain=[('country_id', '=', 'India')], offset=offset, limit=limit, order=order, count=count)
    #     return res
    
       
class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name')

class PropertyDocument(models.Model):
    _name = 'property.document'
    _description = 'Property Document'
    _rec_name = 'document_id'

    document = fields.Binary(string = 'Upload Document')
    document_id = fields.Many2one('real.estate.property', string = 'Property')

class PropertyImage(models.Model):
    _name = 'property.image'
    _description = 'Property Images'
    _rec_name = 'property_image_id'
    
    image = fields.Image(string ="Upload Image")
    property_image_id = fields.Many2one('real.estate.property', string = 'Property Image')

# class PropertyTags(models.Model):
#     _name = 'property.tag'
#     _description = 'Property Tags'
#     _rec_name = 'tag_id'

#     tag_name = fields.Char(string = 'Property Tags')
#     tag_id = fields.Many2many('real.estate.property', string = 'Properties')








