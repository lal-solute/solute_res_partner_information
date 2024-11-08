from odoo import models, tests

class TestCrmLead(tests.TransactionCase):

    def test_create__without_linkedin_handle(self):
        """Test the connecetion between contact and lead without the LinkedIN handle"""
        self.env["res.partner"].create(
            [
                {
                    "name": "Steve Jobs",
                    "email": "steve@apple.com",
                }
            ]
        )
        res_partner = self.env["res.partner"].search([("name", "=", "Steve Jobs")])[0]
        self.env["crm.lead"].create(
            [
                {
                    "name": "Steve Jobs",
                    "type": "opportunity",
                    "contact": res_partner,
                }
            ]
        )


        crm_lead = self.env["res.partner"].search([("name", "=", "Steve Jobs")])[0]
        self.assertEqual(
            "Steve Jobs",
            res_partner.name
        )
        self.assertEqual(
            "steve@apple.com",
            res_partner.email
        )
        self.assertEqual(
            False,
            res_partner.linkedin_handle
        )

        self.assertEqual(
            False,
            crm_lead.linkedin_handle
        )

    def test_create__with_linkedin_handle(self):
        """Test the connecetion between contact and lead with the LinkedIN handle"""
        self.env["res.partner"].create(
            [
                {
                    "name": "Satya Nadella",
                    "email": "satya.nadella@microsoft.com",
                    "linkedin_handle": "https://www.linkedin.com/in/satyanadella/",
                }
            ]
        )
        res_partner = self.env["res.partner"].search([("name", "=", "Satya Nadella")])[0]
        self.env["crm.lead"].create(
            [
                {
                    "name": "Satya Nadella",
                    "type": "opportunity",
                    "contact": res_partner,
                }
            ]
        )
        crm_lead = self.env["res.partner"].search([("name", "=", "Satya Nadella")])[0]
        self.assertEqual(
            "Satya Nadella",
            res_partner.name
        )
        self.assertEqual(
            "satya.nadella@microsoft.com",
            res_partner.email
        )
        self.assertEqual(
            "Satya Nadella",
            crm_lead.name
        )
        self.assertEqual(
            self.assertEqual(
                "https://www.linkedin.com/in/satyanadella/",
                crm_lead.linkedin_handle
            )
        )
        self.assertEqual(
            "https://www.linkedin.com/in/satyanadella/",
            res_partner.linkedin_handle
        )
