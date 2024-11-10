from odoo import models, fields


class CrmLead(models.Model):
    """Extend `crm.lead` for additional information"""

    _inherit = "crm.lead"
    linkedin_handle = fields.Char(string="LinkedIN Handle")
