# -*- coding: utf-8 -*-
{
    'name': "bookstore",

    'summary': "Manage a bookstore",

    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    # always loaded
    'data': [
        'security/security_views.xml',
        'security/ir.model.access.csv',
        'views/bookstore_view.xml',
        'views/templates.xml',
        'data/crone_job.xml',
        'views/user_inheritance.xml',
        'views/wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

