#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = "res.partner"

    training_value = fields.Integer("Training Value", compute="_compute_training_value")

    def _compute_training_value(self):
        trainings = self.env['training.training'].read_group([("partner_id", "in", self.ids)], ['value:sum'], ['partner_id'])
        counts = {
            training['partner_id'][0]: training['value']
            for training in trainings
        }
        for partner in self:
            partner.training_value = counts.get(partner.id, 0)
