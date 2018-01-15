import os

module = os.environ.get('DJANGO_RUNNING_ENVIRON')
if module is None or module == 'dev':
    from cmdb.settings_dir.dev_settings import *
elif module == 'production':
    from cmdb.settings_dir.production_settings import *
elif module == 'test':
    from cmdb.settings_dir.test_settings import *
