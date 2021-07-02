# -*- coding: utf-8 -*-
from odoo import http

# class Import(http.Controller):
#     @http.route('/import/import/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/import/import/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('import.listing', {
#             'root': '/import/import',
#             'objects': http.request.env['import.import'].search([]),
#         })

#     @http.route('/import/import/objects/<model("import.import"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('import.object', {
#             'object': obj
#         })