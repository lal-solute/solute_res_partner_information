from odoo import models, tests

class TestResPartner(tests.TransactionCase):

    def test_create__without_linkedin_handle(self):
        """Test contact without the LinkedIN handle"""
        self.env["res.partner"].create(
            [
                {
                    "name": "Steve Jobs",
                    "email": "steve@apple.com",
                }
            ]
        )
        res_partner = self.env["res.partner"].search([("name", "=", "Steve Jobs")])[0]
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

    def test_create__with_linkedin_handle(self):
        """Test contact with the LinkedIN handle"""
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
        self.assertEqual(
            "Satya Nadella",
            res_partner.name
        )
        self.assertEqual(
            "satya.nadella@microsoft.com",
            res_partner.email
        )
        self.assertEqual(
            "https://www.linkedin.com/in/satyanadella/",
            res_partner.linkedin_handle
        )