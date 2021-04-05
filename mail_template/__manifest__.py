# -*- coding: utf-8 -*-
{
    'name': "c4a8_mail_template",

    'summary': """
        Module for c4a8 e-mail templates""",

    'description': """
        Module for c4a8 e-mail templates
    """,

    'author': "based on Yenthe Van Ginneken",
    'website': "http://www.odoo.yenthevg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','contacts'],

    # always loaded
    'data': [
        'views/mail_template.xml',
    ],
}
