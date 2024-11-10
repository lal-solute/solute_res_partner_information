from odoo import models, fields


class Contact(models.Model):
    """Extend res.partner for additional information"""

    _inherit = "res.partner"
    linkedin_handle = fields.Char(string="LinkedIN Handle")

    # `crm.lead` has a linked a `partner_id` field to `res.partner`, and since there is a restriction for only
    # a one-to-one relation, `lead_ids` will always return a single record
    lead_ids = fields.One2many('crm.lead', 'partner_id', string='Leads', copy=False)
