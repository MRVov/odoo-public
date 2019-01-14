# -*- coding: utf-8 -*-
from odoo import http

# class CustomHsl(http.Controller):
#     @http.route('/custom_hsl/custom_hsl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_hsl/custom_hsl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_hsl.listing', {
#             'root': '/custom_hsl/custom_hsl',
#             'objects': http.request.env['custom_hsl.custom_hsl'].search([]),
#         })

#     @http.route('/custom_hsl/custom_hsl/objects/<model("custom_hsl.custom_hsl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_hsl.object', {
#             'object': obj
#         })