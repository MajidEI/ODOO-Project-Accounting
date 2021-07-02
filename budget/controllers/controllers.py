# -*- coding: utf-8 -*-
from odoo import http

# class Budget(http.Controller):
#     @http.route('/budget/budget/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/budget/budget/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('budget.listing', {
#             'root': '/budget/budget',
#             'objects': http.request.env['budget.budget'].search([]),
#         })

#     @http.route('/budget/budget/objects/<model("budget.budget"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('budget.object', {
#             'object': obj
#         })