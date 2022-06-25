import sys
from setuptools import setup, find_packages

requires = [
    'selenium',
    'numpy'
]

setup(
    name='skyran',
    description=("Fly scraper for cheap prices."),
    version='0.1',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
         'console_scripts': ['skyran=skyran.skyran:main']
    },
    long_description=open('README.md').read(),
    keywords=['skyran', 'sky', 'fly', 'flies', 'cheap', 'scanner', 'scraper', 'scraping']
)
