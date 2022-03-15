from os import environ

PARTICIPANT_FIELDS = ['performance', 'earnings', 'embezzle', 'cluster_number', 'corruption_level', 'participant_label_exp1']



SESSION_CONFIGS = [
    dict(
        name='encrypt_js',
        display_name="Public officials",
        num_demo_participants=3,
        app_sequence=['welcome', 'encrypt_js', 'Choice_PO', 'survey', 'payment_info'],
    ),
    dict(
        name='taxes',
        display_name="TaxPayers",
        num_demo_participants=30,
        app_sequence=['welcome_Tax_Payers', 'encrypt_js', 'Choice_TaxPayer', 'survey', 'payment_info'],
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
        display_name='Pilot 30Jul 2021)',
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
