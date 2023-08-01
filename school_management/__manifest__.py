{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Module for managing schools',
    'description': 'School Management module',
    'sequence': '1',
    'author': 'Nihar Talaviya',
    'category': 'Education',
    'depends': ['base','mail'], 
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/cancel_form_view.xml',
        'views/school_views.xml',
        'views/demo_data.xml',
        'views/teacher_views.xml',    
        'views/report_student_template.xml',

    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}