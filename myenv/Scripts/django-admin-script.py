#!G:\django\myenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django==2.0.6','console_scripts','django-admin'
__requires__ = 'django==2.0.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('django==2.0.6', 'console_scripts', 'django-admin')()
    )
