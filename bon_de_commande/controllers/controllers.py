# -*- coding: utf-8 -*-
from odoo import http

# class BonDeCommande(http.Controller):
#     @http.route('/bon_de_commande/bon_de_commande/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bon_de_commande/bon_de_commande/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bon_de_commande.listing', {
#             'root': '/bon_de_commande/bon_de_commande',
#             'objects': http.request.env['bon_de_commande.bon_de_commande'].search([]),
#         })

#     @http.route('/bon_de_commande/bon_de_commande/objects/<model("bon_de_commande.bon_de_commande"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bon_de_commande.object', {
#             'object': obj
#         })