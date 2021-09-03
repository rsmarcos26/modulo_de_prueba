from odoo import models, fields


class FacturaModelo(models.Model):
    _name = 'factura.modelo'

    numero = fields.Integer('N° Factura')
    ruc = fields.Integer('N° RUC')
    cliente = fields.Many2one(
        'res.partner', string="Cliente"
    )
    fecha_venta = fields.Date(string='Fecha de Venta')
    forma_pago = fields.Selection(
        string="Forma de Pago",
        selection=[
            ('credito', "Crédito"),
            ('efectivo', "Efectivo")
        ]
    )


class ResPartner(models.Model):
    _inherit = 'res.partner'
    cliente_ids = fields.One2many(
        'factura.modelo', 'cliente',
        string="Facturas del Cliente"
    )
