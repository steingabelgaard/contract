# Copyright 2019-2020 Akretion France (http://www.akretion.com/)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class ContractLine(models.Model):
    _inherit = 'contract.line'

    def _prepare_sale_line(self, order_id=False, sale_values=False):
        vals = super(ContractLine, self)._prepare_sale_line(
            order_id=order_id, sale_values=sale_values)
        if self.product_id.must_have_dates:
            dates = self._get_period_to_invoice(
                self.last_date_invoiced, self.recurring_next_date)
            vals.update({
                'start_date': dates[0],
                'end_date': dates[1],
            })
        return vals