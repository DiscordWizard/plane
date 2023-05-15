from odoo import models, fields
class animal(models.Model):
    _name = 'animal'
    id = fields.Char('Id', required=True)
    continentOrigen = fields.Char('ContinentOrigen')
    paisOrigen = fields.Char('PaisOrigen')
    dataNaix = fields.Date('DataNaix')
    sexe = fields.Char('Sex')
    idZoo = fields.Many2one('id', string="Zoo")
    idEspecie = fields.Many2one('id', string="Especie")

    