# -*- coding: utf-8 -*-

from odoo import models, fields, api

class budget(models.Model):
    _name = 'budget.budget'

    idLinkExplo = fields.Many2one('explo.explo',string='Code Explo')
    code = fields.Char('Code')
    rubriques = fields.Char('Rubriques')
    budgetprevu = fields.Char('Budget Prevu')
    budgetreel  = fields.Char('Budget Réel')
    

    