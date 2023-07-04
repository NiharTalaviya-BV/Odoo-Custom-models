from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class School(models.Model):
    _name = 'school.management'
    _description = 'School'
    _inherit = 'mail.thread'                   

    name = fields.Char(string='Name', required=True)
    standard_division = fields.Char(string='Standard & Division')
    roll_number = fields.Integer(string='Roll Number')
    enrollment_number = fields.Char(string='Enrollment Number', readonly=True)
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    zipcode = fields.Char(string='Zipcode')
    country_id =fields.Many2one('res.country', default=lambda self: self.env.ref('base.in'), string='country')
    state_id = fields.Many2one('res.country.state', string='State', domain = "[('country_id', '=', country_id)]")
    phone_number = fields.Char(string='Phone Number', tracking = True, required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True, readonly=True)
    parents_ids = fields.One2many('school.management.parents', 'student_id', string='Parents')
    previous_school_ids = fields.One2many('school.management.previous.school', 'student_id', string='Previous Schools')
    class_teacher_id = fields.Many2one('school.management.teachers', string='Class Teacher')
    stream = fields.Selection(
        [('science', 'Science'), ('commerce', 'Commerce'), ('arts', 'Arts')],
        string='Stream', store=True, readonly=False
    )
    birth_month = fields.Selection([ 
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
        ], string='Birth Month', compute='_compute_birth_month', store=True)      
    
    @api.depends('date_of_birth') 
    def _compute_birth_month(self): 
        for student in self: 
            if student.date_of_birth: 
                student.birth_month = student.date_of_birth.strftime('%m') 
            else: 
                student.birth_month = False

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                dob = fields.Date.from_string(record.date_of_birth)
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                record.age = age
                if age < 4:
                    raise ValidationError("Age cannot be less than 4 years.")
            else:
                record.age = 0
           

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'enrollment_number' not in vals:
                vals['enrollment_number'] = self.env['ir.sequence'].next_by_code('school.enrollment.sequence')
                return super(School, self).create(vals)
            
    @api.onchange('standard_division')
    def _onchange_standard_division(self):
        if self.standard_division:
            teacher = self.env['school.management.teachers'].search([
                ('standard_division', '=', self.standard_division)
            ], limit=1)
            if teacher:
                self.class_teacher_id = teacher.id
            else:
                self.class_teacher_id = False

    def open_teacher_form(self):
        self.ensure_one()
        if self.class_teacher_id:
            return {
                'name': 'Class Teacher',
                'view_mode': 'form',
                'res_model': 'school.management.teachers',
                'res_id': self.class_teacher_id.id,
                'type': 'ir.actions.act_window',
            }
            
    
    def write(self, vals):
        res = super(School, self).write(vals)

        if 'name' in vals or 'phone_number' in vals:
            message = ''
            if 'name' in vals:
                message += 'Name updated. '
            if 'phone_number' in vals:
                message += 'Phone number updated. '

            self.env['mail.message'].create({
                'model': self._name,
                'res_id': self.id,
                'message_type': 'notification',
                'partner_ids': [(4, self.env.user.partner_id.id)],
                'subject': 'Student Information Updated',
                'body': message,
            })

        return res
    
    @api.constrains('phone_number')
    def _check_duplicate_phone_number(self):
        for record in self:
            if record.phone_number:
                duplicate_students = self.search([('id', '!=', record.id), ('phone_number', '=', record.phone_number)])
                if duplicate_students:
                    raise ValidationError("A student with the same phone number already exists.")
    
        
    @api.constrains('phone_number')
    def _check_phone_number_length(self):
        for record in self:
            if record.phone_number and len(record.phone_number) != 10:
                raise ValidationError('Phone number must be exactly 10 digits!')

    def save_all_data(self):

        current_name = self.name
        current_phone_number = self.phone_number

        self.write({})

        if self.name != current_name or self.phone_number != current_phone_number:
            message = ''
            if self.name != current_name:
                message += 'Name updated. '
            if self.phone_number != current_phone_number:
                message += 'Phone number updated. '

            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Action Completed',
                    'message': message,
                    'sticky': False,
                },
            }

        self.parents_ids.write({})
        self.previous_school_ids.write({})

        return True
    
    @api.constrains('standard_division')
    def _check_standard_division(self):
        valid_values = [
        '1A', '1B', '1C', '1D',
        '2A', '2B', '2C', '2D',
        '3A', '3B', '3C', '3D',
        '4A', '4B', '4C', '4D',
        '5A', '5B', '5C', '5D',
        '6A', '6B', '6C', '6D',
        '7A', '7B', '7C', '7D',
        '8A', '8B', '8C', '8D',
        '9A', '9B', '9C', '9D',
        '10A', '10B', '10C', '10D'
    ]

        for record in self:
            if record.standard_division and record.standard_division not in valid_values:
                raise ValidationError("Invalid standard division! Valid values are: {}".format(valid_values))
            
    