# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bon_de_commande(models.Model):
    _name = 'bon_de_commande.bon_de_commande'

    quantite = fields.Char('Quantite')
    designation = fields.Char('Designation des prestations')
    price = fields.Float('Prix unitaires Mensuels (Hors TVA)')
    montant = fields.Float('Montant')