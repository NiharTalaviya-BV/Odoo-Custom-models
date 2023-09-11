from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class School(models.Model):
    _name = 'school.management'
    _description = 'School'
    _inherit = ['mail.thread']
       
    name = fields.Char(string='Name', required=True)
    standard_division = fields.Selection([
        ('1A', '1-A'), ('1B', '1-B'), ('1C', '1-C'), ('1D', '1-D'),
        ('2A', '2-A'), ('2B', '2-B'), ('2C', '2-C'), ('2D', '2-D'),
        ('3A', '3-A'), ('3B', '3-B'), ('3C', '3-C'), ('3D', '3-D'),
        ('4A', '4-A'), ('4B', '4-B'), ('4C', '4-C'), ('4D', '4-D'),
        ('5A', '5-A'), ('5B', '5-B'), ('5C', '5-C'), ('5D', '5-D'),
        ('6A', '6-A'), ('6B', '6-B'), ('6C', '6-C'), ('6D', '6-D'),
        ('7A', '7-A'), ('7B', '7-B'), ('7C', '7-C'), ('7D', '7-D'),
        ('8A', '8-A'), ('8B', '8-B'), ('8C', '8-C'), ('8D', '8-D'),
        ('9A', '9-A'), ('9B', '9-B'), ('9C', '9-C'), ('9D', '9-D'),
        ('10A', '10-A'), ('10B', '10-B'), ('10C', '10-C'), ('10D', '10-D'),
        ('11', '11'), ('12', '12'),
    ], string='Standard & Division')
    roll_number = fields.Integer(string='Roll Number')
    enrollment_number = fields.Char(string='Enrollment Number', readonly=True)
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    zipcode = fields.Char(string='Zipcode')
    country_id =fields.Many2one('res.country', default=lambda self: self.env.ref('base.in'), string='country')
    state_id = fields.Many2one('res.country.state', string='State', domain = "[('country_id', '=', country_id)]")
    phone_number = fields.Char(string='Phone Number', tracking = True)
    email = fields.Char(string='Email')
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=False, readonly=True)
    parents_ids = fields.One2many('school.management.parents', 'student_id', string='Parents')
    previous_school_ids = fields.One2many('school.management.previous.school', 'student_id', string='Previous Schools')
    class_teacher_id = fields.Many2one('school.management.teachers',  string='Class Teacher')
    stream = fields.Selection(
        [('science', 'Science'), ('commerce', 'Commerce'), ('arts', 'Arts')],
        string='Stream', store=True, readonly=False)
    create_date = fields.Datetime()
    write_date = fields.Datetime()
    fee_detail = fields.Selection([
        ('pending', 'Pending'), 
        ('half-paid', 'Half-Paid'), 
        ('paid', 'Paid')], string='Fee Status')
    active = fields.Boolean(default=True)
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
  
    division_id = fields.Many2one('school.management.teachers', string = 'division')
    student_info=fields.Selection([('active','Active'),('left-school',"Left-School")], string="Student Status")
    progress_bar = fields.Integer(compute='_compute_progress_bar', string='Progress')
    extracurricular_activity_ids = fields.Many2many(
        'extracurricular.activity', 
        'student_activity_rel', 
        'student_id', 
        'activity_id', 
        string='Extra curricular Activities'
    )
    handle=fields.Integer()
    xls_report = fields.Binary('XLSX Report')
    xls_report_name = fields.Char('Report Name')

    
   
    @api.depends('name', 'standard_division', 'roll_number', 'enrollment_number', 'street',
                 'city', 'zipcode', 'country_id', 'state_id', 'phone_number', 'date_of_birth',
                 'parents_ids', 'previous_school_ids', 'class_teacher_id', 'stream', 'fee_detail',
                 'active', 'birth_month', 'division_id', 'student_info')
    
    def _compute_progress_bar(self):
     
        fields_to_include = [
            'name', 'standard_division', 'roll_number', 'enrollment_number', 'street',
            'city', 'zipcode', 'country_id', 'state_id', 'phone_number', 'date_of_birth',
            'parents_ids', 'previous_school_ids', 'class_teacher_id', 'stream', 'fee_detail',
            'active', 'birth_month', 'division_id', 'student_info'
        ]
        total_fields = len(fields_to_include)
        filled_fields = 0

        for record in self:
            for field_name in fields_to_include:
                field_value = record[field_name]
                if field_value:
                    # Check if the field has a value (not empty or False)
                    filled_fields += 1

            # Calculate the percentage and set the value of the progress_bar field
            if total_fields > 0:
                progress_percentage = (filled_fields / total_fields) * 100
                record.progress_bar = min(int(progress_percentage), 100)
            else:
                record.progress_bar = 0

    @api.constrains('email', 'student_info')
    def send_congratulations_email(self):
        template = self.env.ref('school_management.email_template_student_report')
        
        for student in self:
            if student.email and student.student_info == 'active':
                try:
                    template.send_mail(student.id, force_send=True)
                except exceptions.UserError as e:
                    pass

    
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
        

    def action_print_excel_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{self._name}/{self.id}/xls_report',
            'target': 'new',
        }

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if 'enrollment_number' not in vals: 
    #             vals['enrollment_number'] = self.env['ir.sequence'].next_by_code('school.enrollment.sequence')
    #             return super(School, self).create(vals)
                
    @api.model_create_multi
    def create(self, vals_list):
        existing_enrollments = self.search([('enrollment_number', 'like', 'ENR')], order='enrollment_number desc', limit=1)
        last_enrollment = existing_enrollments.enrollment_number if existing_enrollments else 'ENR0000'
        sequence = int(last_enrollment[3:])
        for vals in vals_list:
            if 'enrollment_number' not in vals:
                sequence += 1
                vals['enrollment_number'] = f'ENR{sequence:04d}'
        return super(School, self).create(vals_list)
  

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



    # @api.onchange('street')
    # def _onchange_street(self):
          
    #     new_context_values = {
    #         'key1': 'value1',
    #         'key2': 'value2',
    #     }
    #     updated_record = self.with_context(new_context_values)

    #     self = updated_record
    #     print("vvvvvvvAAAAAAAAAAAAA", updated_record)

    #     print('Updated Context:', self._context)
    #     for record in self:
    #         if self._context.get('key1'):
    #             record.street="LA MIAMI"
    #         else:
    #             return False

            
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

        self.write({})

        self.parents_ids.write({})
        self.previous_school_ids.write({})
        self.class_teacher_id.write({})
        return {
            'effect': {
                'fadeout':'slow',
                'message' : 'saved successfully',
                'type':'rainbow_man'
            }
        }
    
    def redirect_class_teacher(self):
        return{
            'type':'ir.actions.act_url',
            'target':'self',
            'url':'http://localhost:8069/web#action=438&model=school.management.teachers&view_type=list&cids=1&menu_id=259'
        }
            
    def action_change_fee_status_paid(self):
        for rec in self:
            if rec.fee_detail == "pending" or "half-paid":
                rec.fee_detail = "paid"
        
    def action_change_fee_status_pending(self):
        for rec in self:
            if rec.fee_detail == "paid":
                rec.fee_detail = "pending"
            
    def name_get(self):
        student_list = []
        record_ids = self.env['school.management'].search([]).ids
        # print("Record ids:",record_ids)
        for record in self:
            student_name = str(record.name) + " " + str(record.enrollment_number)
            student_list.append((record.id, student_name.upper()))
        return student_list
    
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', '|', ('phone_number', operator, name), ('name', operator, name), ('enrollment_number', operator, name)]
        return super(School, self).search(domain, limit=limit).name_get()
    
    def write(self,values):
        if 'date_of_birth' in values:
            record_id = [12]
            res = self.env['school.management'].browse(record_id)
            # print('AAAAAAAAAAAAAAAAA',res)
            res.name='Niharrrrr'
            res.phone_number=9632587410
        return super(School,self).write(values)
    

    def action_cancel_application(self):
        for record in self:
            record.status = 'left-school'

    def action_active_student(self):
        for record in self:
            record.status='active'

    def action_send_mail(self):
        template_id=self.env.ref('school_management.email_template_student_report').id
        template=self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
    

    @api.model
    def action_send_mail_to_all(self):
        template_id = self.env.ref('school_management.email_template_student_report').id
        template = self.env['mail.template'].browse(template_id)

        students_with_email = self.search([('email', '!=', False)])
        
        for student in students_with_email:
            template.send_mail(student.id, force_send=True)
    # def generate_student_report(self, student_id):
    #     student = self.env['school.management'].browse(student_id)
    #     report = self.env.ref('school_management.action_report_student')
    #     return report.report_action(student)

            
         
    
    
    # @api.onchange('standard_division')
    # def create_related_record(self):
    #     if self.standard_division:
    #        self.env['school.management.teachers'].create({'name':'xyzzzzzz', 'standard_division': self.standard_division})
            

    # @api.constrains('name')
    # def write(self):
    #     student_name = self.env['school.management'].search([('roll_number', '=', 45)], limit=1)
      
    #     if student_name:
    #         record_id = student_name.id
    #         print("Record Id:juuuuuuuuuuuuuuuuuuuuu", record_id)
    #     else:
    #         print('No record found')


    #     def open_teacher_form(self):
    #     self.ensure_one()
    #     if self.class_teacher_id:
    #         return {
    #             'name': 'Class Teacher',
    #             'view_mode': 'form',
    #             'res_model': 'school.management.teachers',
    #             'res_id': self.class_teacher_id.id,
    #             'type': 'ir.actions.act_window',
    #         }
    
    
   
