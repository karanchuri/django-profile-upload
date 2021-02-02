import os


settings_module = os.getenv('FLAVOUR', 'dev')
if settings_module == 'prod':
    from .production import *
elif settings_module == 'stag':
    from .staging import *
else:
    from .development import *
