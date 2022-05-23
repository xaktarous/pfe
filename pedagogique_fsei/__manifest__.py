{
    'version': '0.1',
    'name': 'Pedagogique Fsei Application',
    'description': 'Manage your pedagogique system university.',
    'author': 'sebaa fodil',
    'depends': ['base',
    'pedagogique_fsei_evaluation_note',
    'pedagogique_fsei_personnel'
     ],
    'data': [
    'security/ir.model.access.csv',
    'views/departement_view.xml',
    'views/emploi_view.xml',
    'views/locospeda_view.xml',
    'views/cours_view.xml',
    'views/matiere_view.xml',
    'views/specialite_view.xml',
    'views/filiere_view.xml',
    ],
    'sequence':'1',
    'application':'true'
    
}