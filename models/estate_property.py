from odoo import fields, api, models

class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_do_sold(self):
        # omar
        import logging
        _logger = logging.getLogger(__name__)
        output = "\n\n\n\n"+str("Yaay, the inherited thing is working on sold")+"\n\n\n\n"
        _logger.exception('In the Log file to view the  %s', output)
        # omar
        return super().action_do_sold()