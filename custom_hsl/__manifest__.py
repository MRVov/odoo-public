# -*- coding: utf-8 -*-
{
    'name': "custom_hsl",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Vladimir V.",
    'website': "https://odoo-freelance.blogspot.com",


    'category': 'Print Form',
    'version': '0.7',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_order_dates', 'delivery', 'web', 'sale_timesheet', 'purchase_requisition', 'purchase', 'account'],
		
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	    'reports/reports.xml',
        'views/views.xml',
        'views/templates.xml',
	    'reports/bestellung_sale.xml',
	    'reports/bestellung_purchase.xml',
	    'reports/preisanfrage_purchase.xml',
	    'reports/auftrag_sale.xml',
	    'reports/angebot_sale.xml',
	    
	    'reports/rechnung_account.xml',
	    'reports/az_rechnung_account.xml',
	    'reports/lieferschein_stock.xml',
	

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}