from odoo import models, fields, api


class CrmLead(models.Model):
    """Extend `crm.lead` for additional information"""

    _inherit = "crm.lead"
    linkedin_handle = fields.Char(string="LinkedIN Handle",
                                  compute="_compute_linkedin_handle",
                                  store=True, )

    @api.depends('partner_id.linkedin_handle')
    def _compute_linkedin_handle(self):
        """ used to migrate data from `res.partner.linkedin_handle`"""
        for rec in self:
            rec.linkedin_handle = rec.partner_id.linkedin_handle

