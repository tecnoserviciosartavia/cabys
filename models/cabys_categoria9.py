# -*- coding: utf-8 -*-
#     info@fakturacion.com
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CabysCategoria8(models.Model):
    _name = 'cabys.categoria9'
    _description = 'Categoría 9 de Cabys'

    name   = fields.Char('Categoria 9', readonly=True)
    codigo = fields.Char('Código', readonly=True)

    cabys_categoria8_id = fields.Many2one(comodel_name='cabys.categoria8', readonly=True)
    cabys_producto_ids = fields.One2many('cabys.producto', 'cabys_categoria9_id', string='Productos', readonly=True)


