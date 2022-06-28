from os import environ

PARTICIPANT_FIELDS = ['performance', 'earnings', 'embezzle', 'cluster_number', 'corruption_level', 'participant_label_exp1', 'CHOICE', 'frompilot']



SESSION_CONFIGS = [
    dict(
        name='Public_Officials_Exp',
        display_name="Public officials CHOICE",
        num_demo_participants=80,
        app_sequence=['consent', 'welcome_PO', 'encrypt_PO', 'Choice_PO', 'survey', 'payment_info_PO'],
    ),
    dict(
        name='Public_Officials_Random_Exp',
        display_name="Public officials RANDOM",
        num_demo_participants=3,
        app_sequence=['consent', 'welcome_PO', 'encrypt_PO', 'Random_PO', 'survey', 'payment_info_PO'],
    ),
    dict(
        name='Tax_Payers_Exp_Choice',
        display_name="TaxPayers CHOICE",
        num_demo_participants=30,
        app_sequence=['consent', 'welcome_Tax_Payers', 'encrypt_TP', 'Choice_TaxPayer', 'survey', 'payment_info'],
    ),
    dict(
        name='Tax_Payers_Exp_Random',
        display_name="TaxPayers RANDOM",
        num_demo_participants=30,
        app_sequence=['consent', 'welcome_Tax_Payers_RANDOM', 'encrypt_TP', 'Random_TaxPayer', 'survey', 'payment_info'],
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = False

ROOMS = [
    dict(
        name='pjuly',
        display_name='Pilot 30Jul 2021',
    ),
    dict(
        name='PO_Choice',
        display_name='Session PO Choice May 2022',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]



ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '9981668610131'

INSTALLED_APPS = ['otree']
