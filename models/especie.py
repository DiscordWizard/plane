from odoo import models, fields
class especie(models.Model):
    _name = 'especie'
    id = fields.Char('Id', required=True)
    perill = fields.Char('Perill')
    nomVulgar = fields.Char('NomVulgar')
    nomCientific = fields.Char('NomCientific')
    familia = fields.Char('Familia')
    