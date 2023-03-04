# -*- coding: utf-8 -*-
#     info@fakturacion.com
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CabysCategoria7(models.Model):
    _name = 'cabys.categoria8'
    _description = 'Categoría 8 de Cabys'

    name   = fields.Char('Categoria 8', readonly=True)
    codigo = fields.Char('Código', readonly=True)

    cabys_categoria6_id = fields.Many2one(comodel_name='cabys.categoria7', readonly=True)
    cabys_categoria9_ids = fields.One2many('cabys.categoria9', 'cabys_categoria8_id', string='Categorías 9', readonly=True)

