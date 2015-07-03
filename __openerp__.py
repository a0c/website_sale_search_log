{
    'name': 'Search Query Logging for eCommerce',
    'category': 'Website',
    'summary': 'Learn What Products Users Are Interested In',
    'website': '',
    'version': '1.0',
    'description': """
Search Query Logging for OpenERP E-Commerce
===========================================

        """,
    'author': 'AVANSER LLC',
    'depends': ['website_sale'],
    'data': [
        'data/log_data.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'qweb': [],
    'installable': True,
    'auto_install': True,
}
