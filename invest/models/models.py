# -*- coding: utf-8 -*-

from odoo import models, fields, api

class invest(models.Model):
    _name = 'invest.invest'

    code = fields.Char()
    rubriques = fields.Char()
    report_et_anterieurs = fields.Char()
    nouveaux_credits = fields.Char()
    total_credits = fields.Char()
    credits_dengagement = fields.Char()
