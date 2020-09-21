# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _


class Processes(models.Model):
    _name = 'demofactory.processes'
    _description = 'demofactory.processes'
    name = fields.Char(string='process', help='required', required=True)
    duration = fields.Float(string='duration in minutes', required=True, help='required')
    parts_ids = fields.One2many('demofactory.processrawmaterial', 'relation', string='process parts')
    workers_ids = fields.Many2many('demofactory.workers', string='workers')
    output = fields.Many2one('demofactory.parts', string='Output', required=True)
    output_quantity = fields.Float(string='output quantity', required=True)

    _sql_constraints = [
        ('unique_name', 'unique(name)', 'process already exists!, please add another name '),
    ]

    @api.constrains('duration')
    def check_duration(self):
        if self.duration == 0:
            raise exceptions.ValidationError("duration can't be zero")

    @api.constrains('output_quantity')
    def check_output_quantity(self):
        if self.output_quantity == 0:
            raise exceptions.ValidationError("Output Quantity can't be zero")

    @api.model
    def create(self, vals):
        if 'parts_ids' not in vals:
            raise exceptions.ValidationError("Parts can't be empty")

        res_id = super(Processes, self).create(vals)
        # print(vals['parts_ids'][0][2]['quantity'])
        print(vals)
        # remove from storage area
        # test = self.env['demofactory.parts'].search(cr, uid, [('')])

        return res_id
    #
    # def write(self, vals):
    #     res_id = super(processes, self).write(vals)
    #     print(vals['parts_ids'][0][2]['quantity'])
    #     # remove from storage area
    #     # test = self.env['demofactory.parts'].search(cr, uid, [('')])
    #
    #     return res_id