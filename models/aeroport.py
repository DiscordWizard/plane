from odoo import models, fields
class aeroport(models.Model):
    _name = 'aeroport'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    imatge = fields.Binary('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Float('latitud', string="Latitud")
    longitud = fields.Float('longitud', string="Longitud")

    