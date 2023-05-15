from odoo import models, fields
class zoo(models.Model):
    _name = 'zoo'
    id = fields.Char('Id', required=True)
    grandaria = fields.Char('Grandaria')
    nom = fields.Char('Nom')
    ciutat = fields.Char('Ciutat')
    pais = fields.Char('Pais')
    