# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class Parts(models.Model):
    _name = 'demofactory.parts'
    _description = 'demofactory.parts'
    
    name = fields.Char(string='part', required=True, help='required')
    item_price = fields.Float(string='item price', help='required')
    quantity = fields.Float(string='quantity', help='required')
    storage_area = fields.Many2one('demofactory.storagearea', string='storage area', required=True)
    total_price = fields.Float(string='total price',  compute="_compute_total_price")
    
    _sql_constraints = [
        ('price_not_zero', 'Check(item_price > 0 )', ' Item Price can\'t be zero please add valid price'),
        ('quantity_is_not_zero', 'Check(quantity > 0 )', ' Quantity can\'t be zero please add valid quantity'),
        ('unique_name', 'unique(name)', 'item already exists!, please add another name or increase quantity in original item'),

    ]

    @api.depends('quantity', 'item_price')
    def _compute_total_price(self):
        for record in self:
            record.total_price = float(record.item_price * record.quantity)
