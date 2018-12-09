# -*- coding: utf-8 -*-
#    Copyright (C) 2017-2018 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
#
import logging

import odoo.release as release
from odoo import api, fields, models
from odoo.exceptions import UserError, Warning
from odoo.addons import decimal_precision as dp
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)
try:
    import codicefiscale
except ImportError as err:
    _logger.debug(err)

# TODO: Use module for classification
EU_COUNTRIES = ['AT', 'BE', 'BG', 'CY', 'HR', 'DK', 'EE',
                'FI', 'FR', 'DE', 'GR', 'IE', 'IT', 'LV',
                'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'GB',
                'CZ', 'RO', 'SK', 'SI', 'ES', 'SE', 'HU']


class AccountVatCommunication(models.Model):

    def _get_eu_res_country_group(self):
        eu_group = self.env.ref("base.europe", raise_if_not_found=False)
        if not eu_group:
            raise Warning(_('The Europe country group cannot be found. '
                            'Please update the base module.'))
        return eu_group

    # def _get_default_soggetto_codice_fiscale(self, cr, uid, context=None):

    @api.model
    def _get_default_soggetto_codice_fiscale(self):
        if self.company_id.vat:
            return self.company_id.vat[2:]
        return False

    _name = "account.vat.communication"
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env.user.company_id)
    soggetto_codice_fiscale = fields.Char(
        'Codice fiscale contribuente',
        size=16, required=True,
        default=_get_default_soggetto_codice_fiscale,
        help="CF del soggetto a cui riferiscono i dati "
        "della liquidazione.")
    codice_carica = fields.Many2one(
        'italy.ade.codice.carica', 'Codice carica',
        help="Codice carica responsabile trasmissione")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('confirmed', 'Confirmed'), ],
        'State', readonly=True,
        default='draft')
    date_start = fields.Date('From date')
    date_stop = fields.Date('To date')
    # 'period_ids': fields.one2many(
    #     'account.period', 'vat_commitment_id', 'Periods'),
    account_vat_communication_dte_line_ids = fields.One2many(
        'account.vat.communication.dte.line', 'commitment_id',
        'Sale invoices',
        help='Sale invoices to export in VAT communication',
        states={
            'draft': [('readonly', False)],
            'open': [('readonly', False)],
            'confirmed': [('readonly', True)]
        })
    account_vat_communication_dtr_line_ids = fields.One2many(
        'account.vat.communication.dtr.line', 'commitment_id',
        'Purchase invoices',
        help='Purchase invoices to export in VAT communication',
        states={
            'draft': [('readonly', False)],
            'open': [('readonly', False)],
            'confirmed': [('readonly', True)]
        })
    attachment_ids = fields.One2many(
        'ir.attachment', 'res_id', 'Attachments',)
    dte_amount_total = fields.Float(
        'Total sales',
        help='Total amount of sale invoices in Communication',
        digits=dp.get_precision('Account'))
    dte_amount_taxable = fields.Float(
        'Total taxable sales',
        help='Total taxables of sale invoices in Communication',
        digits=dp.get_precision('Account'))
    dte_amount_tax = fields.Float(
        'Total tax sales',
        help='Total taxes of sale invoices in Communication',
        digits=dp.get_precision('Account'))
    dte_amount_discarded = fields.Float(
        'Total discarded sales',
        help='Total amount discarded from sale invoices',
        digits=dp.get_precision('Account'))
    dtr_amount_total = fields.Float(
        'Total purchases',
        help='Total amount of purchase invoices in Communication',
        digits=dp.get_precision('Account'))
    dtr_amount_taxable = fields.Float(
        'Total taxable purchases',
        help='Total taxables of purchase invoices in Communication',
        digits=dp.get_precision('Account'))
    dtr_amount_tax = fields.Float(
        'Total tax purchases',
        help='Total taxes of purchase invoices in Communication',
        digits=dp.get_precision('Account'))
    dtr_amount_discarded = fields.Float(
        'Total discarded purchases',
        help='Total amount discarded from purchase invoices',
        digits=dp.get_precision('Account'))
    # _defaults = {
    #     'company_id': lambda self, cr, uid, c:
    #         self.pool['res.company']._company_default_get(
    #             cr, uid, 'account.vat.communication', context=c),
    #     'state': 'draft',
    #     'soggetto_codice_fiscale': _get_default_soggetto_codice_fiscale,
    # }

    # def create(self, cr, uid, vals, context=None):
    #     res = super(AccountVatCommunication, self).create(
    #         cr, uid, vals, context)
    #     if 'company_id' in vals:
    #         sequence_ids = self.search_sequence(cr, uid, vals['company_id'],
    #                                             context=None)
    #         if not sequence_ids:
    #             self.create_sequence(cr, uid, vals['company_id'], context)
    #     return res

    # def search_sequence(self, cr, uid, company_id, context=None):
    #     return self.pool['ir.sequence'].search(
    #         cr, uid, [
    #             ('name', '=', 'VAT communication'),
    #             ('company_id', '=', company_id)
    #         ])
    # def create_sequence(self, cr, uid, company_id, context=None):
    #     """ Create new no_gap entry sequence for progressivo_telematico
    #     """
    #     # Company sent own communication, so set next number as the nth quarter
    #     next_number = int((date.today().toordinal() -
    #                        date(2017, 7, 1).toordinal()) / 90) + 1
    #     sequence_model = self.pool['ir.sequence']
    #     vals = {
    #         'name': 'VAT communication',
    #         'implementation': 'no_gap',
    #         'company_id': company_id,
    #         'prefix': '',
    #         'number_increment': 1,
    #         'number_next': next_number,
    #         'number_next_actual': next_number,
    #     }
    #     return [sequence_model.create(cr, uid, vals)]

    # def set_progressivo_telematico(self, cr, uid, communication, context=None):
    #     context = context or {}
    #     sequence_model = self.pool['ir.sequence']
    #     company_id = communication.company_id.id
    #     sequence_ids = self.search_sequence(cr, uid, company_id,
    #                                         context=None)
    #     if not sequence_ids:
    #         sequence_ids = self.create_sequence(cr, uid, company_id,
    #                                             context=context)
    #     if len(sequence_ids) != 1:
    #         raise UserError(
    #             _('Error!'), _('VAT communication sequence not set!'))
    #     number = int(sequence_model.next_by_id(
    #         cr, uid, sequence_ids[0], context=context))
    #     return number

    # def test_open(self, cr, uid, ids, *args):
    #     return True

    # def communication_draft(self, cr, uid, ids, context=None):
    #     self.write(cr, uid, ids, {'state': 'draft'})

    # def communication_open(self, cr, uid, ids, context=None):
    #     self.write(cr, uid, ids, {'state': 'open'})

    # def build_tax_tree(self, cr, uid, company_id, context=None):
    #     """
    #     account.tax.code records cannot be recognized as VAT or base amount and
    #     Italian law requires to couple base and VAT amounts,
    #     thats is stored on account.tax model.
    #     This function rebuilds (base,VAT) couples throught account.tax.
    #     Warning: end-user could have set many-2-many base,VAT relationship;
    #     in this case some couple (base,VAT) may be wrong.
    #     However, all tutorial of Odoo Italian Comunity and standard Italian
    #     Localization have just one-2-one relationshiop on (base,VAT).
    #     return: tax_tree[type][basevat][left], where
    #     - type may be 'sale', 'purchase' or 'all'
    #     - basevat may be 'tax_code_id', 'base_code_id', 'ref_tax_code_id' or
    #           'ref_base_code_id'
    #     - left is id of account.tax.code record
    #     """
    #     context = context or {}
    #     tax_model = self.pool['account.tax']
    #     tax_ids = tax_model.search(
    #         cr, uid, [('company_id', '=', company_id)])
    #     tax_tree = {}
    #     for tax_id in tax_ids:
    #         tax = tax_model.browse(cr, uid, tax_id)
    #         type = tax.type_tax_use
    #         if type not in tax_tree:
    #             tax_tree[type] = {}
    #         for basevat in ('tax_code_id', 'base_code_id',
    #                         'ref_tax_code_id', 'ref_base_code_id'):
    #             if basevat[-11:] == 'tax_code_id':
    #                 vatbase = basevat[0:-11] + 'base_code_id'
    #             elif basevat[-12:] == 'base_code_id':
    #                 vatbase = basevat[0:-12] + 'tax_code_id'
    #             else:
    #                 vatbase = False             # never should run here!
    #             if basevat not in tax_tree[type]:
    #                 tax_tree[type][basevat] = {}
    #             if getattr(tax, basevat):
    #                 left = getattr(tax, basevat).id
    #                 if getattr(tax, vatbase):
    #                     right = getattr(tax, vatbase).id
    #                     tax_tree[type][basevat][left] = right
    #                 elif left not in tax_tree[type][basevat]:
    #                     tax_tree[type][basevat][left] = False
    #     return tax_tree

    # def get_country_code(self, cr, uid, partner):
    #     if release.major_version == '6.1':
    #         address_id = self.pool['res.partner'].address_get(
    #             cr, uid, [partner.id])['default']
    #         address = self.pool['res.partner.address'].browse(
    #             cr, uid, address_id, context=None)
    #     else:
    #         address = partner
    #     code = partner.vat and partner.vat[0:2].upper()
    #     return address.country_id.code or code

    def load_invoices(self, commitment, commitment_line_model,
                      dte_dtr_id, where, comm_lines):
        """Read all in/out invoices and return amount and fiscal parts"""
        invoice_model = self.env['account.invoice']
        # account_tax_model = self.pool['account.tax']
        sum_amounts = {}
        for f in ('total', 'taxable', 'tax', 'discarded'):
            sum_amounts[f] = 0.0
        for invoice in invoice_model.browse(invoice_model.search(where)):
            inv_line = {}
    #         for invoice_tax in invoice.tax_line:
    #             tax_nature = False
    #             tax_payability = 'I'
    #             tax_rate = 0.0
    #             tax_nodet_rate = 0.0
    #             tax_type = ''
    #             if invoice_tax.tax_code_id:
    #                 if invoice_tax.tax_code_id.notprintable:
    #                     continue
    #                 if invoice_tax.tax_code_id.exclude_from_registries:
    #                     continue
    #                 taxcode_base_id = invoice_tax.tax_code_id.id
    #                 taxcode_vat_id = False
    #                 where = [('tax_code_id', '=', taxcode_base_id)]
    #             else:
    #                 if invoice_tax.base_code_id.notprintable:
    #                     continue
    #                 if invoice_tax.base_code_id.exclude_from_registries:
    #                     continue
    #                 taxcode_base_id = invoice_tax.base_code_id.id
    #                 taxcode_vat_id = invoice_tax.tax_code_id.id
    #                 where = [('base_code_id', '=', taxcode_base_id)]
    #             # for tax in invoice_tax.tax_code_id.tax_ids:
    #             for tax_id in account_tax_model.search(
    #                     cr, uid, where):
    #                 tax = account_tax_model.browse(cr, uid, tax_id)
    #                 if tax and not tax.parent_id:
    #                     if tax.amount > tax_rate:
    #                         tax_rate = tax.amount
    #                     if tax.non_taxable_nature:
    #                         tax_nature = tax.non_taxable_nature
    #                     if tax.payability:
    #                         tax_payability = tax.payability
    #                     if tax.type_tax_use:
    #                         tax_type = tax.type_tax_use
    #                 else:
    #                     if release.major_version == '6.1':
    #                         tax_rate = 0
    #                         for child in account_tax_model.browse(
    #                                 cr, uid, tax.parent_id.id).child_ids:
    #                             if child.type == 'percent':
    #                                 tax_rate += child.amount
    #                         tax_nodet_rate = 1 - (tax.amount / tax_rate)
    #                     else:
    #                         if tax.type == 'percent' and \
    #                                 tax.amount > tax_nodet_rate:
    #                             tax_nodet_rate = tax.amount
    #                         tax = account_tax_model.browse(
    #                             cr, uid, tax.parent_id.id)
    #                         taxcode_base_id = invoice_tax.tax_code_id.id
    #                         if tax.amount > tax_rate:
    #                             tax_rate = tax.amount
    #             if tax_type in ('sale', 'purchase'):
    #                 if tax_rate == 0.0 and not tax_nature:
    #                     raise UserError(
    #                         _('Error!'),
    #                         _('00400 - '
    #                           'Invalid tax %s nature for invoice %s') % (
    #                               invoice_tax.name,
    #                               invoice.number))
    #                 elif tax_rate and tax_nature and tax_nature != 'N6':
    #                     raise UserError(
    #                         _('Error!'),
    #                         _('00401 - '
    #                           'Invalid tax %s nature for invoice %s') % (
    #                               invoice_tax.name,
    #                               invoice.number))
    #                 if tax_payability == 'S' and tax_nature == 'N6':
    #                     raise UserError(
    #                         _('Error!'),
    #                         _('00420 - '
    #                           'Wrong tax %s nature/payment for invoice %s') % (
    #                               invoice_tax.name,
    #                               invoice.number))

    #             if tax_nature == 'FC' or (tax_nature == 'N2' and
    #                                       not invoice.partner_id.vat):
    #                 if invoice.type[-7:] == '_refund':
    #                     sum_amounts['discarded'] -= round(
    #                         invoice_tax.base + invoice_tax.amount, 2)
    #                 else:
    #                     sum_amounts['discarded'] += round(
    #                         invoice_tax.base + invoice_tax.amount, 2)
    #                 _logger.info(_('Invoice %s (%d), discarded tax line %s' %
    #                                (invoice.number, invoice.id,
    #                                 invoice_tax.name)))
    #                 continue
    #             if taxcode_base_id not in inv_line:
    #                 inv_line[taxcode_base_id] = {}
    #                 inv_line[taxcode_base_id]['amount_taxable'] = 0.0
    #                 inv_line[taxcode_base_id]['amount_tax'] = 0.0
    #                 inv_line[taxcode_base_id]['amount_total'] = 0.0
    #                 inv_line[taxcode_base_id]['tax_vat_id'] = taxcode_vat_id
    #                 inv_line[taxcode_base_id]['tax_rate'] = tax_rate
    #                 inv_line[taxcode_base_id][
    #                     'tax_nodet_rate'] = tax_nodet_rate
    #                 inv_line[taxcode_base_id]['tax_nature'] = tax_nature
    #                 inv_line[taxcode_base_id][
    #                     'tax_payability'] = tax_payability
    #             if tax_rate and not inv_line[taxcode_base_id]['tax_rate']:
    #                 inv_line[taxcode_base_id]['tax_rate'] = tax_rate
    #             if tax_nodet_rate and not inv_line[taxcode_base_id][
    #                     'tax_nodet_rate']:
    #                 inv_line[taxcode_base_id][
    #                     'tax_nodet_rate'] = tax_nodet_rate
    #             if tax_payability and not inv_line[taxcode_base_id][
    #                     'tax_payability']:
    #                 inv_line[taxcode_base_id][
    #                     'tax_payability'] = tax_payability
    #             inv_line[taxcode_base_id]['amount_taxable'] += invoice_tax.base
    #             inv_line[taxcode_base_id]['amount_tax'] += invoice_tax.amount
    #             inv_line[taxcode_base_id]['amount_total'] += round(
    #                 invoice_tax.base + invoice_tax.amount, 2)
    #             if invoice.type[-7:] == '_refund':
    #                 sum_amounts['taxable'] -= invoice_tax.base
    #                 sum_amounts['tax'] -= invoice_tax.amount
    #                 sum_amounts['total'] -= round(
    #                     invoice_tax.base + invoice_tax.amount, 2)
    #             else:
    #                 sum_amounts['taxable'] += invoice_tax.base
    #                 sum_amounts['tax'] += invoice_tax.amount
    #                 sum_amounts['total'] += round(
    #                     invoice_tax.base + invoice_tax.amount, 2)
            if inv_line:
                comm_lines[invoice_id] = {}
                comm_lines[invoice_id]['partner_id'] = invoice.partner_id.id
                comm_lines[invoice_id]['taxes'] = inv_line
        return comm_lines, sum_amounts

    def load_DTE_DTR(self, commitment, commitment_line_model, dte_dtr_id):
        journal_model = self.env['account.journal']
        exclude_journal_ids = journal_model.search(
            ['|', '|',
             ('rev_charge', '=', True),
             ('proforma', '=', True),
             ('anom_sale_receipts', '=', True),
            ])

    #     period_ids = [x.id for x in commitment.period_ids]
        company_id = commitment.company_id.id
        return 0        #debug
        where = [('company_id', '=', company_id),
                 ('registration_date', '>=', commitment.date_start),
                 ('registration_date', '<=', commitment.date_stop),
                 ('journal_id', 'not in', exclude_journal_ids),
                 ('state', 'in', ('open', 'paid'))]
        if dte_dtr_id == 'DTE':
            where.append(('type', 'in', ['out_invoice', 'out_refund']))
        elif dte_dtr_id == 'DTR':
            where.append(('type', 'in', ['in_invoice', 'in_refund']))
        else:
            return

        comm_lines, sum_amounts = self.load_invoices(
            commitment, commitment_line_model,
            dte_dtr_id, where, {})
    #     if comm_lines:
    #         for line_id in commitment_line_model.search(
    #             cr, uid, [('commitment_id', '=', commitment.id),
    #                       ('invoice_id', 'not in', comm_lines.keys()), ]):
    #             commitment_line_model.unlink(cr, uid, [line_id])
    #     for invoice_id in comm_lines:
    #         for line_id in commitment_line_model.search(
    #             cr, uid, [('commitment_id', '=', commitment.id),
    #                       ('invoice_id', '=', invoice_id),
    #                       ('tax_id', 'not in', comm_lines[
    #                           invoice_id]['taxes'].keys()),
    #                       ]):
    #             commitment_line_model.unlink(cr, uid, [line_id])
    #         for tax_id in comm_lines[invoice_id]['taxes']:
    #             line = {'commitment_id': commitment.id,
    #                     'invoice_id': invoice_id,
    #                     'tax_id': tax_id,
    #                     'partner_id': comm_lines[invoice_id]['partner_id'],
    #                     }
    #             for f in ('amount_total',
    #                       'amount_taxable',
    #                       'amount_tax',
    #                       'tax_vat_id',
    #                       'tax_rate',
    #                       'tax_nodet_rate',
    #                       'tax_nature',
    #                       'tax_payability',
    #                       ):
    #                 line[f] = comm_lines[invoice_id]['taxes'][tax_id][f]

    #             ids = commitment_line_model.search(
    #                 cr, uid, [('commitment_id', '=', commitment.id),
    #                           ('invoice_id', '=', invoice_id),
    #                           ('tax_id', '=', tax_id), ])
    #             if ids:
    #                 commitment_line_model.write(cr, uid, ids, line)
    #             else:
    #                 commitment_line_model.create(cr, uid, line)
        return sum_amounts

    @api.model
    def load_DTE(self, commitment):
        """Read all sale invoices in periods"""
        commitment_DTE_line_model = self.env[
             'account.vat.communication.dte.line']
        sum_amounts = self.load_DTE_DTR(
            commitment, commitment_DTE_line_model, 'DTE')
        return sum_amounts

    @api.model
    def load_DTR(self, commitment):
        """Read all purchase invoices in periods"""
        commitment_DTR_line_model = self.env[
            'account.vat.communication.dtr.line']
        sum_amounts = self.load_DTE_DTR(
            commitment, commitment_DTR_line_model, 'DTR')
        return sum_amounts

    @api.multi
    def compute_amounts(self):
        for commitment in self:
            dte_sum_amounts = self.load_DTE(commitment)
            dtr_sum_amounts = self.load_DTR(commitment)
            vals = {}
            for t in ('total', 'taxable', 'tax', 'discarded'):
                f = 'dte_amount_' + t
                vals[f] = dte_sum_amounts[t]
                f = 'dtr_amount_' + t
                vals[f] = dtr_sum_amounts[t]
            self.write(vals)
        return True


    @api.onchange('soggetto_codice_fiscale')
    def onchange_fiscalcode(self):
        name = 'soggetto_codice_fiscale'
        if self.soggetto_codice_fiscale:
            if len(self.soggetto_codice_fiscale) == 11:
                res_partner_model = self.env['res.partner']
                chk = res_partner_model.simple_vat_check('it', self.soggetto_codice_fiscale)
                if not chk:
                    return {'value': {name: False},
                            'warning': {
                        'title': 'Invalid fiscalcode!',
                        'message': 'Invalid vat number'}
                    }
            elif len(self.soggetto_codice_fiscale) != 16:
                return {'value': {name: False},
                        'warning': {
                    'title': 'Invalid len!',
                    'message': 'Fiscal code len must be 11 or 16'}
                }
            else:
                self.soggetto_codice_fiscale = self.soggetto_codice_fiscale.upper()
                chk = codicefiscale.control_code(self.soggetto_codice_fiscale[0:15])
                if chk != self.soggetto_codice_fiscale[15]:
                    value = self.soggetto_codice_fiscale[0:15] + chk
                    return {'value': {name: value},
                            'warning': {
                                'title': 'Invalid fiscalcode!',
                                'message': 'Fiscal code could be %s' % (value)}
                            }

    # #
    # # INTERNAL INTERFACE TO XML EXPORT CODE
    # #
    # def get_xml_fattura_header(self, cr, uid, commitment, dte_dtr_id,
    #                            context=None):
    #     """Return DatiFatturaHeader: may be empty"""
    #     res = {}
    #     if commitment.codice_carica and commitment.soggetto_codice_fiscale:
    #         res['xml_CodiceFiscale'] = commitment.soggetto_codice_fiscale
    #         res['xml_Carica'] = commitment.codice_carica
    #     return res

    # def get_xml_company(
    #         self, cr, uid, commitment, dte_dtr_id, context=None):
    #     """Return data of CessionarioCommittente or CedentePrestatore
    #     which referers to current company.
    #     This function is pair to get_xml_cessionario_cedente which returns
    #     customer or supplier data"""
    #     line_model = self.pool['account.vat.communication.line']
    #     res = line_model._dati_partner(
    #         cr, uid, commitment.company_id.partner_id, None, context)
    #     if res['xml_IdPaese'] != 'IT':
    #         raise UserError(
    #             _('Error!'),
    #             _('Missed company VAT number'))
    #     return res

    # def get_partner_list(self, cr, uid, commitment, dte_dtr_id,
    #                      context=None):
    #     """Return list of partner_id in communication by commitment_id
    #     This function has to be used for CessionarioCommittente or
    #     CedentePrestatore iteration"""
    #     if dte_dtr_id != 'DTE' and dte_dtr_id != 'DTR':
    #         raise UserError(
    #             _('Error!'),
    #             _('Internal error: no DTE neither DTR selected'))
    #     model_name = 'account.vat.communication.%s.line' % dte_dtr_id.lower()
    #     table_name = model_name.replace('.', '_')
    #     sql = 'SELECT DISTINCT partner_id FROM %s WHERE commitment_id = %d' % \
    #         (table_name, commitment.id)
    #     cr.execute(sql)
    #     ids = []
    #     for rec in cr.fetchall():
    #         ids.append(rec[0])
    #     return ids

    # def get_xml_cessionario_cedente(self, cr, uid, commitment, partner_id,
    #                                 dte_dtr_id, context=None):
    #     """Return data of CessionarioCommittente or CedentePrestatore
    #     This function has to be used as result of every iteration of
    #     get_partner_list"""
    #     commitment_line_model = self.pool['account.vat.communication.line']
    #     res_partner_model = self.pool['res.partner']
    #     partner = res_partner_model.browse(cr, uid, partner_id)
    #     return commitment_line_model._dati_partner(cr, uid, partner,
    #                                                None, context)

    # def get_invoice_list(self, cr, uid, commitment, partner_id, dte_dtr_id,
    #                      context=None):
    #     """Return list of invoices in communication
    #     by partner_id and commitment_id.
    #     This function has to be used for CessionarioCommittente or
    #     CedentePrestatore sub-iteration"""
    #     if dte_dtr_id != 'DTE' and dte_dtr_id != 'DTR':
    #         raise UserError(
    #             _('Error!'),
    #             _('Internal error: no DTE neither DTR selected'))
    #     model_name = 'account.vat.communication.%s.line' % dte_dtr_id.lower()
    #     table_name = model_name.replace('.', '_')
    #     sql = '''SELECT DISTINCT invoice_id FROM %s
    #                     WHERE commitment_id = %d and partner_id = %d''' % \
    #         (table_name, commitment.id, partner_id)
    #     cr.execute(sql)
    #     ids = []
    #     for rec in cr.fetchall():
    #         ids.append(rec[0])
    #     return ids

    # def get_xml_invoice(self, cr, uid, commitment, invoice_id,
    #                     dte_dtr_id, context=None):
    #     """Return data of Invoice.
    #     This function has to be used as result of every iteration of
    #     get_invoice_list"""
    #     account_invoice_model = self.pool['account.invoice']
    #     invoice = account_invoice_model.browse(cr, uid, invoice_id)
    #     res = {}
    #     res['xml_TipoDocumento'] = self.pool[
    #         'account.vat.communication.line']._tipodocumento(cr, uid, invoice,
    #                                                          context)
    #     res['xml_Data'] = invoice.date_invoice
    #     if invoice.type in ('in_invoice', 'in_refund'):
    #         if not invoice.supplier_invoice_number:
    #             raise UserError(
    #                 _('Error!'),
    #                 _('Missed supplier invoice number %s, id=%d') % (
    #                     invoice.number, invoice.id))
    #         res['xml_Numero'] = invoice.supplier_invoice_number[-20:]
    #         res['xml_DataRegistrazione'] = invoice.registration_date
    #     else:
    #         res['xml_Numero'] = invoice.number[:20]
    #     return res

    # def get_riepilogo_list(self, cr, uid, commitment, invoice_id,
    #                        dte_dtr_id, context=None):
    #     """Return list of tax lines of invoice in communication
    #     by invoice_id and commitment.id.
    #     This function has to be used for CessionarioCommittente or
    #     CedentePrestatore sub-sub-iteration"""
    #     if dte_dtr_id != 'DTE' and dte_dtr_id != 'DTR':
    #         raise UserError(
    #             _('Error!'),
    #             _('Internal error: no DTE neither DTR selected'))
    #     model_name = 'account.vat.communication.%s.line' % dte_dtr_id.lower()
    #     line_model = self.pool[model_name]
    #     ids = line_model.search(
    #         cr, uid, [
    #             ('commitment_id', '=', commitment.id),
    #             ('invoice_id', '=', invoice_id)
    #         ])
    #     return ids

    # def get_xml_riepilogo(self, cr, uid, commitment, line_id,
    #                       dte_dtr_id, context=None):
    #     """Return data of tax invoice line.
    #     This function has to be used as result of every iteration of
    #     get_riepilogo_list"""
    #     commitment_line_model = self.pool['account.vat.communication.line']
    #     model_name = 'account.vat.communication.%s.line' % dte_dtr_id.lower()
    #     line_model = self.pool[model_name]
    #     CommitmentLine = line_model.browse(cr, uid, line_id)
    #     return commitment_line_model._dati_line(
    #         cr, uid, CommitmentLine, {'xml': True}, context)


class CommitmentLine(models.AbstractModel):
    _name = 'account.vat.communication.line'

    # def _get_error(self, error, context):
    #     if context.get('no_except', False):
    #         return error
    #     else:
    #         raise UserError(_('Error!'), error)
    #     return False

    # def _dati_partner(self, cr, uid, partner, args, context=None):
    #     if release.major_version == '6.1':
    #         address_id = self.pool['res.partner'].address_get(
    #             cr, uid, [partner.id])['default']
    #         address = self.pool['res.partner.address'].browse(
    #             cr, uid, address_id, context)
    #     else:
    #         address = partner

    #     res = {'xml_Error': ''}
    #     if partner.vat:
    #         vat = partner.vat.replace(' ', '')
    #         res['xml_IdPaese'] = vat and vat[0:2].upper() or ''
    #         res['xml_IdCodice'] = vat and vat[2:] or ''
    #     res['xml_Nazione'] = address.country_id.code or res.get('xml_IdPaese')
    #     if not res.get('xml_Nazione'):
    #         self._get_error(_('Unknow country of %s') % partner.name, context)

    #     if (partner.individual or
    #             not partner.is_company) and partner.fiscalcode:
    #         r = self.pool['account.vat.communication'].onchange_fiscalcode(
    #             cr, uid, partner.id,
    #             partner.fiscalcode, None,
    #             country_id=partner.country_id,
    #             context=context)
    #         if 'warning' in r:
    #             res['xml_Error'] += self._get_error(
    #                 _('Invalid fiscalcode of %s') % partner.name, context)
    #         if res.get('xml_Nazione', '') == 'IT' and \
    #                 partner.fiscalcode != res.get('xml_IdCodice'):
    #             res['xml_CodiceFiscale'] = partner.fiscalcode.replace(' ', '')
    #     elif res.get('xml_IdPaese', '') == 'IT':
    #         pass
    #     elif not partner.vat:
    #         res['xml_CodiceFiscale'] = '99999999999'

    #     if partner.individual or not partner.is_company:
    #         if release.major_version == '6.1':
    #             if partner.fiscalcode_firstname and partner.fiscalcode_surname:
    #                 res['xml_Nome'] = partner.fiscalcode_firstname
    #                 res['xml_Cognome'] = partner.fiscalcode_surname
    #             else:
    #                 res['xml_Denominazione'] = partner.name
    #         else:
    #             res['xml_Nome'] = partner.firstname
    #             res['xml_Cognome'] = partner.lastname
    #         if not res.get('xml_Cognome') or not res.get('xml_Nome'):
    #             res['xml_Error'] += self._get_error(
    #                 _('Invalid First or Last name %s') % (partner.name),
    #                 context)
    #     else:
    #         res['xml_Denominazione'] = partner.name
    #         if not partner.vat and \
    #                 res['xml_Nazione'] == 'IT':
    #                 # or
    #                 # res['xml_Nazione'] in EU_COUNTRIES):
    #             raise UserError(
    #                 _('Error!'),
    #                 _('Partner %s %d without VAT number') % (
    #                     partner.name, partner.id))
    #     if not res.get('xml_CodiceFiscale') and \
    #             not res.get('xml_IdPaese') and \
    #             not res.get('xml_IdCodice'):
    #         raise UserError(
    #             _('Error!'),
    #             _('Partner %s %d without fiscal data') % (
    #                 partner.name, partner.id))
    #     # if res.get('xml_IdPaese') and \
    #     #         res.get('xml_IdPaese') !=res['xml_Nazione']:
    #     #     raise UserError(
    #     #         _('Error!'),
    #     #         _('Partner %s %d vat country differs from country') % (
    #     #             partner.name, partner.id))

    #     if address.street:
    #         res['xml_Indirizzo'] = address.street.replace(
    #             u"'", '').replace(u"’", '')
    #     else:
    #         raise UserError(
    #             _('Error!'),
    #             _('Partner %s without street on address') % (partner.name))

    #     if res.get('xml_IdPaese', '') == 'IT':
    #         if address.zip:
    #             res['xml_CAP'] = address.zip.replace('x', '0').replace('%',
    #                                                                    '0')
    #         if len(res['xml_CAP']) != 5 or not res['xml_CAP'].isdigit():
    #             raise UserError(
    #                 _('Error!'),
    #                 _('Partner %s has wrong zip code') % (partner.name))
    #     res['xml_Comune'] = address.city or ' '
    #     if not address.city:
    #         raise UserError(
    #             _('Error!'),
    #             _('Partner %s without city on address') % (partner.name))
    #     if res['xml_Nazione'] == 'IT':
    #         if release.major_version == '6.1':
    #             res['xml_Provincia'] = address.province.code
    #         else:
    #             res['xml_Provincia'] = partner.state_id.code
    #         if not res['xml_Provincia']:
    #             del res['xml_Provincia']
    #             raise UserError(
    #                 _('Error!'),
    #                 _('Partner %s without province on address') % (
    #                     partner.name))
    #     return res

    # def _dati_line(self, cr, uid, line, args, context=None):
    #     res = {}
    #     res['xml_ImponibileImporto'] = abs(line.amount_taxable)
    #     res['xml_Imposta'] = abs(line.amount_tax)
    #     res['xml_Aliquota'] = line.tax_rate * 100
    #     res['xml_Detraibile'] = 100.0 - line.tax_nodet_rate * 100
    #     if (args and args.get('xml', False)):
    #         # Load data during export xml
    #         if res['xml_Detraibile'] == 0:
    #             res['xml_Deducibile'] = "SI"
    #             del res['xml_Detraibile']
    #         if line.tax_nature:
    #             res['xml_Natura'] = line.tax_nature
    #         if line.tax_payability:
    #             res['xml_EsigibilitaIVA'] = line.tax_payability
    #     else:
    #         # Data to line for displaying
    #         res['xml_Natura'] = line.tax_nature
    #     return res

    # def _tipodocumento(self, cr, uid, invoice, context=None):
    #     doctype = invoice.type
    #     country_code = self.pool['account.vat.communication'].get_country_code(
    #         cr, uid, invoice.partner_id)
    #     if doctype == 'out_invoice' and \
    #             not invoice.partner_id.vat and \
    #             not invoice.partner_id.fiscalcode:
    #         if invoice.amount_total >= 0:
    #             return 'TD07'
    #         else:
    #             return 'TD08'
    #     elif doctype == 'out_refund' and \
    #             not invoice.partner_id.vat and \
    #             not invoice.partner_id.fiscalcode:
    #         return 'TD08'
    #     elif country_code != 'IT' and country_code in EU_COUNTRIES and \
    #             doctype == 'in_invoice':
    #         return 'TD11'
    #     elif doctype in ('out_invoice', 'in_invoice'):
    #         if invoice.amount_total >= 0:
    #             return 'TD01'
    #         else:
    #             return 'TD04'
    #     elif doctype in ('out_refund', 'in_refund'):
    #         return 'TD04'
    #     else:
    #         raise UserError(
    #             _('Error!'),
    #             _('Invalid type %s (%s) for invoice %s') % (doctype,
    #                                                         country_code,
    #                                                         invoice.number))

class CommitmentDTELine(models.Model):
    _name = 'account.vat.communication.dte.line'
    _inherit = 'account.vat.communication.line'

    # def _xml_dati_partner(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         ctx = context.copy()
    #         ctx['no_except'] = True
    #         fields = self._dati_partner(cr, uid, line.partner_id, args,
    #                                     context=ctx)
    #         result = {}
    #         for f in ('xml_IdPaese', 'xml_IdCodice', 'xml_CodiceFiscale'):
    #             if fields.get(f, ''):
    #                 result[f] = fields[f]
    #             else:
    #                 result[f] = False
    #         res[line.id] = result
    #     return res

    # def _xml_dati_line(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         res[line.id] = self._dati_line(cr, uid, line, args,
    #                                        context=context)
    #     return res

    # def _xml_tipodocumento(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         res[line.id] = self._tipodocumento(cr, uid, line.invoice_id,
    #                                            context=context)
    #     return res

    commitment_id = fields.Many2one(
        'account.vat.communication', 'VAT commitment')
    invoice_id = fields.Many2one(
        'account.invoice', 'Invoice')
    #     'tax_id': fields.Many2one(
    #         'account.tax.code', 'VAT code'),
    partner_id = fields.Many2one(
        'res.partner', 'Partner',
        readony=True)
    #     'tax_vat_id': fields.Many2one(
    #         'account.tax.code', 'VAT code',
    #         readony=True),
    #     'tax_rate': fields.float(
    #         'VAT rate',
    #         readony=True),
    #     'tax_nodet_rate': fields.float(
    #         'VAT non deductible rate',
    #         readony=True),
    #     'tax_nature': fields.char(
    #         'Non taxable nature',
    #         readony=True),
    #     'tax_payability': fields.char(
    #         'VAT payability',
    #         readony=True),
    #     'amount_total': fields.float(
    #         'Amount', digits=dp.get_precision('Account')),
    #     'amount_taxable': fields.float(
    #         'Taxable amount', digits=dp.get_precision('Account')),
    #     'amount_tax': fields.float(
    #         'Tax amount', digits=dp.get_precision('Account')),
    #     'xml_Error': fields.function(
    #         _xml_dati_partner,
    #         string="Error",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True
    #     ),
    #     'xml_IdPaese': fields.function(
    #         _xml_dati_partner,
    #         string="Country",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_IdCodice': fields.function(
    #         _xml_dati_partner,
    #         string="VAT number",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_CodiceFiscale': fields.function(
    #         _xml_dati_partner,
    #         string="Fiscalcode",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_TipoDocumento': fields.function(
    #         _xml_tipodocumento,
    #         string="Document type",
    #         help="Values: TD01=invoice, TD04=refund",
    #         type="char",
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_ImponibileImporto': fields.function(
    #         _xml_dati_line,
    #         string="Taxable",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Imposta': fields.function(
    #         _xml_dati_line,
    #         string="Tax",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Aliquota': fields.function(
    #         _xml_dati_line,
    #         string="Tax rate",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Detraibile': fields.function(
    #         _xml_dati_line,
    #         string="Tax deductible",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Natura': fields.function(
    #         _xml_dati_line,
    #         string="Tax type",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    # }

class CommitmentDTRLine(models.Model):
    _name = 'account.vat.communication.dtr.line'
    _inherit = 'account.vat.communication.line'

    # def _xml_dati_partner(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         fields = self._dati_partner(cr, uid, line.partner_id, args,
    #                                     context=context)

    #         result = {}
    #         for f in ('xml_IdPaese', 'xml_IdCodice', 'xml_CodiceFiscale'):
    #             if fields.get(f, ''):
    #                 result[f] = fields[f]
    #         res[line.id] = result
    #     return res

    # def _xml_dati_line(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         res[line.id] = self._dati_line(cr, uid, line, args,
    #                                        context=context)
    #     return res

    # def _xml_tipodocumento(self, cr, uid, ids, fname, args, context=None):
    #     res = {}
    #     for line in self.browse(cr, uid, ids, context=context):
    #         res[line.id] = self._tipodocumento(cr, uid, line.invoice_id,
    #                                            context=context)
    #     return res

    commitment_id = fields.Many2one(
        'account.vat.communication', 'VAT commitment')
    invoice_id = fields.Many2one(
        'account.invoice', 'Invoice')
    #     'tax_id': fields.Many2one(
    #         'account.tax.code', 'VAT code'),
    partner_id = fields.Many2one(
        'res.partner', 'Partner',
        readony=True)
    #     'tax_vat_id': fields.Many2one(
    #         'account.tax.code', 'VAT code',
    #         readony=True),
    #     'tax_rate': fields.float(
    #         'VAT rate',
    #         readony=True),
    #     'tax_nodet_rate': fields.float(
    #         'VAT non deductible rate',
    #         readony=True),
    #     'tax_nature': fields.char(
    #         'Non taxable nature',
    #         readony=True),
    #     'tax_payability': fields.char(
    #         'VAT payability',
    #         readony=True),
    #     'amount_total': fields.float(
    #         'Amount', digits=dp.get_precision('Account')),
    #     'amount_taxable': fields.float(
    #         'Taxable amount', digits=dp.get_precision('Account')),
    #     'amount_tax': fields.float(
    #         'Tax amount', digits=dp.get_precision('Account')),
    #     'xml_Error': fields.function(
    #         _xml_dati_partner,
    #         string="Error",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True
    #     ),
    #     'xml_IdPaese': fields.function(
    #         _xml_dati_partner,
    #         string="Country",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_IdCodice': fields.function(
    #         _xml_dati_partner,
    #         string="VAT number",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_CodiceFiscale': fields.function(
    #         _xml_dati_partner,
    #         string="Fiscalcode",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_TipoDocumento': fields.function(
    #         _xml_tipodocumento,
    #         string="Document type",
    #         help="Values: TD01=invoice, TD04=refund",
    #         type="char",
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_ImponibileImporto': fields.function(
    #         _xml_dati_line,
    #         string="Taxable",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Imposta': fields.function(
    #         _xml_dati_line,
    #         string="Tax",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Aliquota': fields.function(
    #         _xml_dati_line,
    #         string="Tax rate",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Detraibile': fields.function(
    #         _xml_dati_line,
    #         string="Tax deductible",
    #         type="float",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    #     'xml_Natura': fields.function(
    #         _xml_dati_line,
    #         string="Tax type",
    #         type="char",
    #         multi=True,
    #         store=False,
    #         select=True,
    #         readonly=True),
    # }
