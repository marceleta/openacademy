# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Gerenciador Treinamentos""",

    'description': """
        Modulo Open Academy para gerenciamento de Treinamentos
        - cursos de formação
        - Sessões de Treinamento
        - registro de participantes
    """,

    'author': "Marcelo Rocha",
    'website': "www.nextsolucoes.net.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'teste',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
