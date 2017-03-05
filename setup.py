# Copyright 2017 Brandon Schlueter

import os
import sys
from setuptools.command.install import install
from setuptools import setup

import yaml

class Register(install):
    YAS_CONFIG_FILE_PATH = os.path.join(sys.prefix, 'etc/yas/yas.yml')

    def run(self):

        config = None

        with open(self.YAS_CONFIG_FILE_PATH, 'r') as yas_config_file_read:
            config = yaml.load(yas_config_file_read)

        config['handler_list'].append('yas_example_clud_handler.')

        with open(self.YAS_CONFIG_FILE_PATH, 'w') as yas_config_file_write:
            yaml.dump(config, yas_config_file_write, explicit_start=True)

setup(
    cmdclass={'install': OverrideInstall},
    setup_requires=['pbr>=1.8'],
    pbr=True)
