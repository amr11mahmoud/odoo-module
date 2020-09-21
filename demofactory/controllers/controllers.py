# -*- coding: utf-8 -*-
# from odoo import http


# class Demofactory(http.Controller):
#     @http.route('/demofactory/demofactory/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demofactory/demofactory/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demofactory.listing', {
#             'root': '/demofactory/demofactory',
#             'objects': http.request.env['demofactory.demofactory'].search([]),
#         })

#     @http.route('/demofactory/demofactory/objects/<model("demofactory.demofactory"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demofactory.object', {
#             'object': obj
#         })
