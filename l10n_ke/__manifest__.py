# -*- coding: utf-8 -*-
{
    'name': "Kenya - Accounting",
    'support': "support@optima.co.ke",

    'description': """
Kenya Odoo localisation module necessary to run Odoo Accounting for Kenyan businesses
=====================================================================================
         - Chart of Accounts
         - Kenyan Tax Structure
         - Kenya Counties""",

    'author': "Optima ICT Services LTD",
    'website': "http://www.optima.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base_iban', 'base_vat'],

    # always loaded
    'data': [
        'data/l10n_ke_chart.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.account.tag.csv',
        'data/account.tax.template.csv',
        'data/res.country.state.csv',
        'data/account_chart_template_data.yml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
