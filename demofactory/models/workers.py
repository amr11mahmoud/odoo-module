# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Workers(models.Model):
    _name = 'demofactory.workers'
    _description = 'demofactory.workers'
    name = fields.Char(string='name', required=True, help='required')
    hours_number = fields.Float(string='hours number', required=True, help='required')
    hour_price = fields.Float(string='hour price', required=True, help='required')
    total_salary = fields.Float(string='total salary',compute="_compute_total_salary", store=True)
    image = fields.Binary(string='image', help='Select image here',store=True)

    @api.depends('hours_number', 'hour_price')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = float(record.hours_number * record.hour_price)

    @api.constrains('hour_price')
    def check_values(self):
        if self.hour_price == 0 :
            raise exceptions.ValidationError(" worker hour price can't be zero")
