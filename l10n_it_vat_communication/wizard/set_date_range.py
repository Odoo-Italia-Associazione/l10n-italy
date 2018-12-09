# -*- coding: utf-8 -*-
#    Copyright 2018 Associazione Odoo Italia
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SetDateRange(models.TransientModel):
    _name = 'set.date.range.commitment'

    @api.model
    def _set_date_start(self):
        if 'active_id' in self.env.context:
            return self.env['account.vat.communication'].browse(
                self.env.context['active_id']).date_start
        return False

    @api.model
    def _set_date_stop(self):
        if 'active_id' in self.env.context:
            return self.env['account.vat.communication'].browse(
                self.env.context['active_id']).date_stop
        return False

    date_range_id = fields.Many2one('date.range', string="Date range")
    date_start = fields.Date('From date', required=True,
                            default=_set_date_start)
    date_stop = fields.Date('To date', required=True,
                          default=_set_date_stop)
    state = fields.Selection([('init', 'init'), ('done', 'done')],
                             string='Status', readonly=True, default='init')

    @api.multi
    def set_date_range(self):
        if 'active_id' not in self.env.context:
            raise UserError(_('Current commitment not found'))

        self.ensure_one()
        wizard = self
        if not wizard.date_start or not wizard.date_start:
            raise UserError(_('No date range found!\n'
                              'Please insert date values!'))
        self.env['account.vat.communication'].compute_amounts()
        self.state = 'done'
        return {
            'name': _('Set Date Range'),
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'set.date.range.commitment',
            'domain': [],
            'context': dict(self._context, active_ids=self.ids),
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': self.id,
        }
