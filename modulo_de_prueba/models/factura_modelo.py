from odoo import models, fields


class factura_modelo (models.Model):
    _name = 'factura.modelo'

    numero = fields.Integer('N° Factura')
    ruc = fields.Integer('N° RUC')
    cliente = fields.Char('Razón Social')
    fecha_venta = fields.Date(string='Fecha de Venta')
    forma_pago = fields.Selection(
        string="Forma de Pago",
        selection=[
            ('credito', "Crédito"),
            ('efectivo', "Efectivo")
        ]
    )
