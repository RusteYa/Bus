import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bus.settings')
django.setup(set_prefix=False)

from insert_data import insert_bus

if __name__ == '__main__':
    insert_bus()
