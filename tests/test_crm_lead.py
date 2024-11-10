from odoo import models, tests

class TestCrmLead(tests.TransactionCase):

    def test_create__without_linkedin_handle(self):
        """Test the connection between contact and lead without the LinkedIN handle"""

        name = "Steve Jobs"
        email = "steve@apple.com"

        # `res.partner` tests
        res_partner = self.env["res.partner"].create(
            [
                {
                    "name": name,
                    "email": email,
                }
            ]
        )

        self.assertEqual(
            name,
            res_partner.name
        )
        self.assertEqual(
            email,
            res_partner.email
        )
        self.assertEqual(
            False,
            res_partner.linkedin_handle
        )

        # `crm.lead` tests
        crm_lead = self.env["crm.lead"].create(
            [
                {
                    "name": name,
                    "type": "opportunity",
                    "partner_id": res_partner.id,
                }
            ]
        )

        self.assertEqual(
            False,
            crm_lead.linkedin_handle
        )

        self.assertEqual(
            res_partner.linkedin_handle,
            crm_lead.linkedin_handle,
            'linkedin_handle for crm_lead and res_partner must be empty/False'
        )

    def test_create__with_linkedin_handle(self):
        """Test the connection between contact and lead with the LinkedIN handle"""

        name = "Satya Nadella"
        email = "satya.nadella@microsoft.com"
        linkedin_url = "https://www.linkedin.com/in/satyanadella/"

        # `res.partner` tests
        res_partner = self.env["res.partner"].create(
            [
                {
                    "name": name,
                    "email": email,
                    "linkedin_handle": linkedin_url,
                }
            ]
        )

        self.assertEqual(
            name,
            res_partner.name,
        )
        self.assertEqual(
            email,
            res_partner.email,
        )
        self.assertEqual(
            linkedin_url,
            res_partner.linkedin_handle,
        )

        # `crm.lead` tests
        crm_lead = self.env["crm.lead"].create(
            [
                {
                    "name": name,
                    "type": "opportunity",
                    "partner_id": res_partner.id,
                }
            ]
        )

        self.assertEqual(
            name,
            crm_lead.name,
        )

        self.assertEqual(
            linkedin_url,
            crm_lead.linkedin_handle,
        )

        self.assertEqual(
            res_partner.linkedin_handle,
            crm_lead.linkedin_handle,
            'linkedin_handle for crm_lead and res_partner must be equal'
        )
