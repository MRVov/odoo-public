# -*- coding: utf-8 -*-

from odoo import models, fields, api

class custom_purchase_order(models.Model):
	_inherit = "purchase.order"
	#x_user_id = fields.Many2one('res.users', string='Responsible')
	x_project_id = fields.Many2one('project.project', string='Project')
	#x_partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address',   help="Delivery address for current order.")
	x_carrier_id = fields.Many2one('delivery.carrier', string="Delivery Method", help="Fill this field if you plan to invoice the shipping based on picking.")
	
	#@api.onchange('partner_id')
	#def onchange_product(self):
	#	self.x_partner_shipping_id = self.partner_id

class custom_account_invoice_line(models.Model):
	_inherit = "account.invoice.line"
	
	price_subtotal_net2 = fields.Monetary(string='Amount net',  readonly=True, compute='_compute_net')
	disc_net = fields.Monetary(string='Amount discount',  readonly=True, compute='_compute_net')
	
	@api.one
	@api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
	             'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
	             'invoice_id.date_invoice', 'invoice_id.date')
	def _compute_net(self):
		currency = self.invoice_id and self.invoice_id.currency_id or None
		price = self.price_unit
		taxes = False
		if self.invoice_line_tax_ids:
			taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id, partner=self.invoice_id.partner_id)
		self.price_subtotal_net2 = price_subtotal_signed = taxes['total_excluded'] if taxes else self.quantity * price


class custom_stock_picking(models.Model):
	_inherit = "stock.picking"
	x_user_id = fields.Many2one('res.users', string='Responsible')

	#project_id = fields.Many2one('project.project', string='Project')
	#partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address',   help="Delivery address for current order.")
	#carrier_id = fields.Many2one('delivery.carrier', string="Delivery Method", help="Fill this field if you plan to invoice the shipping based on picking.")
	
