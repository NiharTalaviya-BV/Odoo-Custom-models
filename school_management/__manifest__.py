{
    'name': 'School Management',
    'version': '16.0',
    'summary': 'Module for managing schools',
    'description': 'School Management module',
    'sequence': '1',
    'author': 'Nihar Talaviya',
    'category': 'Education',
    'depends': ['base','mail','report_xlsx'], 
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/email_template_data.xml',
        'data/cron_data.xml',   
        'wizard/cancel_form_view.xml',
        'views/school_views.xml',
        'views/demo_data.xml',
        'views/teacher_views.xml',    
        'views/component_view.xml',
        'views/res_config_settings_view.xml',

        'report/report_student_template.xml',
        'report/inherit_template.xml',
    ],

    
   'assets': {
      'web.assets_backend': ['school_management/static/src/components/Component.js',
                             'school_management/static/src/components/Component.xml'],
   },
  
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}