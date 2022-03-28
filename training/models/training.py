#-*- coding: utf-8 -*-

from odoo import models, fields, api


class training(models.Model):
    _name = 'training.training'
    _description = 'training.training'

    name = fields.Char()
    value = fields.Float()
    max_attendees = fields.Integer(string="Maximum Attendees")
    expected_revenue = fields.Float(compute="_compute_expected_revenue", store=True)
    description = fields.Text()

    @api.depends('value', 'max_attendees')
    def _compute_expected_revenue(self):
        for record in self:
            record.expected_revenue = record.value * record.max_attendees
