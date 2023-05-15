from odoo import models, fields
class vol(models.Model):
    _name = 'vol'
    codi = fields.Integer('Codi', required=True)
    passatgers = fields.Char('Passatgers')
    dataSortida = fields.Date('DataSortida')
    dataArrivada = fields.Date('DataArrivada')
    desti = fields.Many2one('aeroport.codi',string='Desti')
    origen = fields.Many2one('aeroport.codi',string='Origen')
    pilot = fields.Many2one('pilot.codi',string='Pilot')
    avio = fields.Many2one('avio.codi',string='Avio')