#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    training_value = fields.Integer("Training Value", compute="_compute_training_value")

    def _compute_training_value(self):
        for partner in self:
            partner.training_value = sum(self.env["training.training"].search([("partner_id", "=", partner.id)]).mapped('value'))
