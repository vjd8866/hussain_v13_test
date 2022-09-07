# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    def _get_picking_type_create_values(self, max_sequence):
        create_data, max_sequence = super(
            StockWarehouse, self
        )._get_picking_type_create_values(max_sequence)
        create_data.update(
            {
                "in_type_id": {
                    "name": _("Return"),
                    "code": "internal",
                    "use_create_lots": True,
                    "use_existing_lots": False,
                    "default_location_src_id": self.lot_stock_id.id,
                    "default_location_dest_id": self.lot_stock_id.id,
                    "sequence": max_sequence + 6,
                    "barcode": self.code.replace(" ", "").upper() + "-RETURN",
                    "show_reserved": False,
                    "sequence_code": "RET",
                    "company_id": self.company_id.id,
                },
            }
        )
        max_sequence += 2
        return create_data, max_sequence
