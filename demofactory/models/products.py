# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Products(models.Model):
    _name = 'demofactory.products'
    _description = 'demofactory.products'
    name = fields.Char(string='', required=True, help='required', placeholder='Name')
    price = fields.Float(string="price", required=True)
    actual_cost = fields.Float(string="actual cost")
    processes = fields.Many2many('demofactory.processes', string='')

    state = fields.Many2one('demofactory.processes', tracking = True , domain = "[( 'id' , 'in', processes)]")

    process_state = fields.Selection([
        ('running', 'Running'),
        ('paused', 'Paused'),
        ('completed', 'Completed')
    ], string="process state", default="paused")

    @api.onchange('processes')
    def change_status(self):
        print('onchange')
        return {'domain':{'state':[('name','in',[i.name for i in self.processes])]}}
    
    @api.constrains('price')
    def check_price(self):
        if self.price == 0:
            raise exceptions.ValidationError("price can't be zero")

    @api.model
    def create(self, vals):
        if not vals['processes'][0][2]:
            raise exceptions.ValidationError("Processes can't be empty")

        res_id = super(Products, self).create(vals)
        
        # remove from storage area
        # test = self.env['demofactory.parts'].search(cr, uid, [('')])

        return res_id

    def start_process(self):
        return self.write({'process_state':'running'})
    
    def pause_process(self):
        return self.write({'process_state':'paused'})

    def complete_process(self):
        return self.write({'process_state':'completed'})