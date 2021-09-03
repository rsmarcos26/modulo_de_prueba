from odoo import models, fields


class productoModelo(models.Model):
    _name = 'producto.modelo'

    cod = fields.Integer('Código')
    descripcion = fields.Text('Descripcion')
    marca = fields.Char("Marca")
    categoria = fields.Selection(
        string="Categoría",
        selection=[
            ('limpieza', "Limpieza"),
            ('deco', "Decoración"),
            ('cocina', "Cocina"),
            ('alimentos', "Alimentos"),
            ('electro', "Electrónica")
        ]
    )
    precio = fields.Float('Precio')