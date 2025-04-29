import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Ensure this is correct

INSTALLED_APPS = [
    # ...existing apps...
    'apps.loans',  # Ensure this app is listed
    'banking_aggregator.apps.core',  # Add the core app here
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Ensure this path is correct
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]