#!/usr/bin/env python

from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
from os.path import abspath
from platform import system
from setuptools.command.install import install
import subprocess
import sys
from os import path
from io import open

BASH_SCRIPTS = [
    abspath('./auth0_client/setup/scripts/01_init_auth0_client_config.sh'),
    abspath('./auth0_client/setup/scripts/02_setup_autocomplete.sh'),
    abspath('./auth0_client/setup/scripts/03_update_auth0_client.sh'),
    abspath('./auth0_client/setup/scripts/04_cleanup.sh'),
    abspath('./auth0_client/setup/scripts/05_finish.sh')

]


class BashInstall(install):

    def run(self):
        install.run(self)
        if system() == 'Linux':
            for script in BASH_SCRIPTS:
                subprocess.call(script, shell=True)
        elif system() == 'Darwin':
            for script in BASH_SCRIPTS:
                subprocess.call(script, shell=True)


DESCRIPTION = ("auth0 click client.")
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()



PREFIX = '/tmp/auth-menu'
VERSION = '0.6.1'

setup_requires = (
    ['pytest-runner'] if any(x in sys.argv for x in ('pytest', 'test', 'ptr')) else []
)


setup(
    name='auth0_client',
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/rubelw/auth0_client',
    author='Will Rubel',
    author_email='willrubel@gmail.com',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=setup_requires,
    tests_require=['pytest','mock'],
    test_suite="auth0_client.tests",
    cmdclass={
        'install': BashInstall
    },
    install_requires=[
        "boto3>=1.4.3",
        "requests>=2.18",
        "Click>=6.7",
        "configparser>=3.5.0",
        "future>=0.16.0",
        "six>=1.11.0",
        "pip",
        "click-help-colors",
        "reprint",
        "tabulate",
        "click-completion"
    ],
    keywords=['auth0', 'client'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    entry_points= {
        'console_scripts': [
            'auth-client=auth0_client.command:auth0_client',
            'auth-menu=auth0_client.menu.auth_menu:main'
        ]
    },
    data_files =    [
            (PREFIX, ['auth0_client/menu/datafiles/auth-menu.yml'])
    ]
)