# -*- coding: utf-8 -*-
#
# Copyright 2010-18, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Community Association <https://odoo-community.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import fields, models


class ResCity(models.Model):
    _name = 'res.city'
    _description = 'City'

    country_id = fields.Many2one('res.country',
                                 'Country',
                                help='Country encoded by ISO-3166.')
    name = fields.Char('City',
                       size=64,
                       help='Use "." (dot) to search with abbreviation',
                       required=True)
    zip = fields.Char('CAP',
                      size=16,
                      help='City\'s ZIP code. (Country dependent).',
                      required=True,
                      index=1)
    phone_prefix = fields.Char('Telephone Prefix', size=16)
    istat_code = fields.Char('ISTAT code', size=16)
    cadaster_code = fields.Char('Cadaster Code', size=16)
    web_site = fields.Char('Web Site')
    state_id = fields.Many2one(
        'res.country.state',
        'District',
        help='Upper administration (Province, District or Federal State).',
        domain="[('country_id', '=', country_id)]")
    nuts = fields.Integer('NUTS', size=1)
