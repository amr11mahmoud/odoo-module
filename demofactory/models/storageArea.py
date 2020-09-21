# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StorageArea(models.Model):
    _name = 'demofactory.storagearea'
    _description = 'demofactory.storagearea'
    name = fields.Char(string='name', required=True, help='required')
