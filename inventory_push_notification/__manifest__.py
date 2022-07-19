# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Inventory Notification',
    'author': 'Altela Softwares',
    'version': '12.0.1.0.0',
    'summary': 'Get certain user notified when barcode or sales price are changed through chat',
    'license': 'OPL-1',
    'sequence': 1,
    'description': """Get certain user notified when barcode or sales price are changed through chat""",
    'category': 'Inventory',
    'website': 'https://www.altela.net',
    'depends': [
        'stock',
        'mail',
    ],
    'images': [
        'static/description/assets/banner.gif',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    # 'pre_init_hook': 'pre_init_check',
}
