from odoo import models, fields
class pilot(models.Model):
    _name = 'pilot'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    cognoms = fields.Char('Cognoms')
    nif = fields.Char('Nif')
    telf = fields.Char('Telefon')
    email = fields.Char('Email')
    