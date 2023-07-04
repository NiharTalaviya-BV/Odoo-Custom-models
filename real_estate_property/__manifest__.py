{
    'name': 'Real Estate Module',
    'version': '16.0',
    'category': 'Sales',
    'summary': 'Custom real estate module for managing properties',
    'author': 'Nihar Talaviya',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/country_view.xml', 
        'data/ir_sequence_data.xml',     
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}
