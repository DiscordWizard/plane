from odoo import models, fields
class aeroport(models.Model):
    _name = 'aeroport'
    codi = fields.Integer('Codi', required=True)
    nom = fields.Char('Nom')
    imatge = fields.Binary('Imatge')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    latitud = fields.Double('id', string="Latitud")
    longitud = fields.Double('id', string="Longitud")

    