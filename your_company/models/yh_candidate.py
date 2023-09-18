from odoo import models, fields


class YourCandidate(models.Model):
    _name = 'yh.candidate'
    _description = 'Your Candidates'

    candidate_name = fields.Char()
    email = fields.Char()
    phone_number = fields.Char()
    experience = fields.Char()
    image = fields.Binary()
