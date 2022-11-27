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
    value = fields.Float()
    max_attendees = fields.Integer(string="Maximum Attendees")
    expected_revenue = fields.Float(compute="_compute_expected_revenue", store=True)
    profitability = fields.Float(compute="_compute_profitability")
    description = fields.Text()
    partner_id = fields.Many2one("res.partner", "Partner")

    @api.depends('value', 'max_attendees')
    def _compute_expected_revenue(self):
        for record in self:
            record.expected_revenue = record.value * record.max_attendees

    def _compute_profitability(self):
        for record in self:
            trainings = self.search([])
            average = sum(trainings.mapped('expected_revenue')) / len(trainings)
            record.profitability =  average / record.expected_revenue if record.expected_revenue else 0

    def _populate_factories(self):
        return [
            ("name", populate.constant('Training_{counter}')),
            ("value", populate.randfloat(0, 100)),
            ("max_attendees", populate.randfloat(1, 50)),
            ("partner_id", populate.randomize(self.env['res.partner'].search([]).ids + [False])),
        ]
