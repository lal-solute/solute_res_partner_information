from odoo import models, fields


class Contact(models.Model):
    """Extend res.partner for additional information"""

    _inherit = "res.partner"
    linkedin_handle = fields.Char(string="LinkedIN Handle")
