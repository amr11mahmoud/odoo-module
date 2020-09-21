# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class Log(models.Model):
    _name = 'demofactory.log'
    _description = 'demofactory.log'
    # standard processs
    process = fields.Many2many('demofactory.processes', string='process')
    # real time
    time = fields.Float(string="time")
    # difference time 
    time_difference = fields.Float(string="time difference")
    # actual workers
    worker = fields.Many2many('demofactory.workers', string='worker')
    
    part = fields.Many2many('demofactory.processes', string='part')

    difference_items = fields.FLoat(string='difference_items')
    quantity = fields.Float(string='quantity')
    rating = fields.Float(string='rating')
    notes = fields.Float(string='notes')
    cost = fields.Float(string='cost')

  