{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Module for managing schools',
    'description': 'School Management module',
    'author': 'Nihar Talaviya',
    'category': 'Education',
    'depends': ['base','mail'], 
    'data': [
        'security/ir.model.access.csv',
        'views/school_views.xml',
        'views/demo_data.xml',
        'views/teacher_views.xml',

        'data/ir_sequence_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}