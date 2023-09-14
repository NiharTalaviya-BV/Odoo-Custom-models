{
    'name': 'YourCompany Theme',
    'description': 'YourCompany website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv', 
        'views/snippets/company-leaders.xml',
        'views/snippets/explore-employees.xml',
        'views/snippets/snippets.xml',
        'views/yh_employees.xml',
    ],
    'assets':{
        'web.assets_frontend': [
            'your_company/static/src/scss/styles.scss',
            'your_company/static/src/scss/company_leaders.scss',
            'your_company/static/src/js/explore-employees.js',
        ],
        'web._assets_primary_variables': [
            "your_company/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'application':  True,
    'auto_install': True,
    'license': 'LGPL-3',
}
