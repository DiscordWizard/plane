from odoo import models, fields
class vol(models.Model):
    _name = 'vol'
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Integer('Passatgers')
    dataSortida = fields.Date('DataSortida')
    dataArrivada = fields.Date('DataArrivada')
    desti = fields.Many2one('aeroport',string='Desti')
    origen = fields.Many2one('aeroport',string='Origen')
    pilot = fields.Many2one('pilot',string='Pilot')
    avio = fields.Many2one('avio',string='Avio')