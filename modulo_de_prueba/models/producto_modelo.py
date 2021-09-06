from odoo import models, fields, api


class ProductoModelo(models.Model):
    _name = 'producto.modelo'

    cod = fields.Integer('Código')
    descripcion = fields.Text('Descripcion')
    marca = fields.Char("Marca")
    categoria_id = fields.Many2one('producto.modelo.categoria')
    valor_venta = fields.Float('VV')
    igv = fields.Float(
        string='IGV',
        compute='_igv'
    )
    precio_venta = fields.Float(
        string='PV',
        compute='_precio_venta'
    )

    @api.depends('valor_venta')
    def _igv(self):
        self.igv = self.valor_venta * 0.18

    @api.depends('valor_venta')
    def _precio_venta(self):
        self.precio_venta = self.valor_venta * 1.18

    @api.onchange('precio_venta')
    def _mensaje(self):
        if self.precio_venta != 0:
            return {
                'warning': {
                    'title': 'Precio de Venta actualizado',
                    'message': 'El IGV y el precio de venta han sido actualizados'
                }
            }