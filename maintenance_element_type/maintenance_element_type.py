# -*- coding: utf-8 -*-
##############################################################################
#
#    Elneo
#    Copyright (C) 2011-2015 Elneo (Technofluid SA) (<http://www.elneo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields
    
class MaintenanceElementType(models.Model):
    _name = 'maintenance.element.type'
    
    name = fields.Char(string='Name',size=255, translate=True)
    description = fields.Text(string='Description')

class MaintenanceElement(models.Model):
    _inherit='maintenance.element'
    
    element_type_id = fields.Many2one('maintenance.element.type', 'Element type')
    

class product_product(models.Model):
    _inherit='product.product'
    
    maintenance_element_type_id = fields.Many2one('maintenance.element.type', 'Maintenance element type')