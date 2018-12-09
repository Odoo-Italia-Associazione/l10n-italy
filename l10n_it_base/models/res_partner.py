# -*- coding: utf-8 -*-
#
# Copyright 2010-18, Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2018-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
# Copyright 2018-19 - Odoo Community Association <https://odoo-community.org>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
#
from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _build_where_city(self, level=None, ign_city=None):
        level = level or 0
        ign_city = ign_city or False
        where = []
        if self.zip:
            if self.country_id:
                where.append(('country_id', '=', self.country_id.id))
            zip = '%s%s' % (self.zip[0: len(self.zip) - level],
                            '%' * level)
            where.append(('zip', '=ilike', zip))
        if self.city and not ign_city:
            tofind = self.city.replace('.', '%')
            tofind = tofind.replace(' ', '%') + '%'
            tofind = tofind.replace('%%', '%')
            where.append(('name', '=ilike', tofind))
        return where

    def _build_where_stateid(self, state_id):
        where = []
        if self.country_id:
            where.append(('country_id', '=', self.country_id.id))
        where.append(('id', '=', state_id))
        return where

    def _onchange_addrflds(self, force_city=None):
        force_city = force_city or False
        where = self._build_where_city()
        if where:
            city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=1)
                city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=2)
                city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=1, ign_city=True)
                city_ids = self.env['res.city'].search(where)
            if not city_ids:
                where = self._build_where_city(level=2, ign_city=True)
                city_ids = self.env['res.city'].search(where)
            if city_ids:
                found = False
                for id in city_ids:
                    city = self.env['res.city'].browse(id.id)
                    if city.zip and city.zip.find('%') >= 0:
                        found = True
                        break
                if not found:
                    city = self.env['res.city'].browse(city_ids[0].id)
                if not self.city or force_city:
                    self.city = city.name
                if not self.zip:
                    self.zip = city.zip.replace('%', '0')
                where = self._build_where_stateid(city.state_id.id)
                stateid_ids = self.env['res.country.state'].search(where)
                if stateid_ids:
                    self.state_id = stateid_ids[0]

    @api.onchange('country_id')
    def onchange_country(self):
        return self._onchange_addrflds()

    @api.onchange('zip')
    def onchange_zip(self):
        return self._onchange_addrflds(force_city=True)

    @api.onchange('state_id')
    def onchange_state_id(self):
        return self._onchange_addrflds()

    @api.onchange('city')
    def onchange_city(self):
        return self._onchange_addrflds()

    @api.onchange('vat')
    def onchange_vat(self):
        res = {}
        if self.vat:
            ids = self.search([('vat', '=', self.vat),
                               ('parent_id', '!=', False)])
            if ids:
                name = self.browse(ids[0].id).name
                res['warning'] = {
                    'title': _('Warning'),
                    'message': _('Found another partner with same vat: '
                                 '%s' % name)}
        return res
