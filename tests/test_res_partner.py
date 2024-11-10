from odoo import models, tests

class TestResPartner(tests.TransactionCase):

    def test_create__without_linkedin_handle(self):
        """Test contact without the LinkedIN handle"""

        name = "Steve Jobs"
        email = "steve@apple.com"

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

    def test_create__with_linkedin_handle(self):
        """Test contact with the LinkedIN handle"""

        name = "Satya Nadella"
        email = "satya.nadella@microsoft.com"
        linkedin_url = "https://www.linkedin.com/in/satyanadella/"

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
            res_partner.name
        )
        self.assertEqual(
            email,
            res_partner.email
        )
        self.assertEqual(
            linkedin_url,
            res_partner.linkedin_handle
        )