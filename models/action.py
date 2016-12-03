# -*- coding: utf-8 -*-

from odoo import models, fields


class ActWindow(models.Model):
    _name = "ir.actions.act_window"
    _inherit = "ir.actions.act_window"

    auto_refresh = fields.Integer()
