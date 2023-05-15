from odoo import models, fields
class avio(models.Model):
    _name = 'avio'
    codi = fields.Integer('Codi', required=True)
    imatge = fields.Binary('Imatge')
    marca = fields.Integer('Marca')
    model = fields.Char('Model')
    maxVel = fields.Float('MaxVel')
    