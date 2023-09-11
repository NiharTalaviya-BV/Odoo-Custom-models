{
    'name': 'custom_pos',
    'version': '16.0',
    'summary': 'Module for customizing the POS',
    'description': 'Custom Pos Module',
    'sequence': '1',
    'author': 'Nihar Talaviya',
    'category': 'Sale',
    'depends': ['base', 'point_of_sale', ],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_pos.xml',
        'views/inherit_pos_order_view.xml',
        'views/inherit_res_partner_view.xml',
        'views/sale_location.xml'
    ],

    'assets': {
        'point_of_sale.assets': [
            'custom_pos/static/src/js/**/*.js',
            'custom_pos/static/src/xml/**/*.xml',]
    },

    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}
