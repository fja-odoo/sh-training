#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import populate


class training(models.Model):
    _name = 'training.training'
    _description = 'training.training'
    _populate_sizes = {
        'small': 1000,
        'medium': 100000,
        'large': 1000000,
    }

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    average = fields.Float(compute="_training_average")
    description = fields.Text()
    partner_id = fields.Many2one("res.partner", "Partner")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def _populate_factories(self):
        return [
            ("name", populate.constant('Training_{counter}')),
            ("value", populate.randfloat(0, 100)),
            ("partner_id", populate.randomize(self.env['res.partner'].search([]).ids + [False])),
        ]

    def _training_average(self):
        for record in self:
            records = self.search([])
            record.average = sum(records.mapped('value')) / len(records)
