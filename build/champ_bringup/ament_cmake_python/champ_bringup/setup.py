from setuptools import find_packages
from setuptools import setup

setup(
    name='champ_bringup',
    version='0.1.0',
    packages=find_packages(
        include=('champ_bringup', 'champ_bringup.*')),
)
