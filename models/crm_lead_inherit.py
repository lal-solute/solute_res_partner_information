from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    @api.constrains('partner_id')
    def _check_unique_partner(self):
        """ to ensure it is a one-to-one relationship, we might need to add a constraint to
         prevent multiple `crm.lead` records from referencing the same `res.partner`."""
        for lead in self:
            if lead.partner_id and self.search([('partner_id', '=', lead.partner_id.id), ('id', '!=', lead.id)]):
                raise ValidationError("A customer can only be linked to one opportunity.")
