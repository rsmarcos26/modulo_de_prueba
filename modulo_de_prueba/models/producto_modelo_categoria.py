from odoo import models, fields, api


class ProductoModeloCategoria(models.Model):
    _name = 'producto.modelo.categoria'
    name = fields.Char('Categoría')
    parent_id = fields.Many2one(
        'producto.modelo.categoria',
        string='Categoría padre',
        ondelete='restrict',
        index=True,
        relation='producto_modelo_categoria_rel'
    )
    child_ids = fields.One2many(
        'producto.modelo.categoria', 'parent_id',
        string='Categoría hijas'
    )

    @api.constraints('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! no puedes crear categorías recursivas.'
            )