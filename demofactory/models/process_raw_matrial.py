# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class ProcessRawMaterial(models.Model):
    _name = 'demofactory.processrawmaterial'
    _description = 'demofactory.processrawmaterial'

    name = fields.Many2one('demofactory.parts', string='name')
    quantity = fields.Integer(string='quantity')
    relation = fields.Many2one('demofactory.processes', visible=False)

    @api.constrains('quantity')
    def check_quantity(self):
        if self.quantity == 0:
            raise exceptions.ValidationError(" process parts quantity can't be zero")