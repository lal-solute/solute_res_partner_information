solute_res_partner_information
==========

Add-on for showing additional information about contacts

Task
----------
Fork this repo and:

* Transfer the LinkedIN-Handle field from the "Additional Information"-tab with the tab into crm.lead, but show the tab and the field still in res_partner
* Migrate the data that might already exist in res.partner to crm.lead
* Create a One-to-one relation between res.partner and crm.lead, so that a contact can be connected to a specific opportunity and an opportunity can be connected to a specific contact
* The tests for crm.lead are failing, make them run and maybe adjust them accordingly to the changes you made.
* Make Screenshots of how your changes are reflected in the frontend