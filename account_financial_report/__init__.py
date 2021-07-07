# Author: Damien Crier
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from . import models
from . import report
from . import wizard

from openupgradelib import openupgrade


def module_migration(cr):
    v8_model = "account_financial_report_webkit"
    v9_model = "account_financial_report_qweb"
    v11_model = "account_financial_report"
    account_move_line = "account_move_line"
    last_rec_date = "last_rec_date"
    if openupgrade.is_module_installed(cr, v8_model):
        openupgrade.update_module_names(
            cr,
            [
                (v8_model, v11_model),
            ],
            merge_modules=True,
        )
        openupgrade.drop_columns(cr, [(account_move_line, last_rec_date)])

    if openupgrade.is_module_installed(cr, v9_model):
        openupgrade.update_module_names(
            cr,
            [
                (v9_model, v11_model),
            ],
            merge_modules=True,
        )
