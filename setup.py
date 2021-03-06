from setuptools import find_packages
from setuptools import setup
import os


version = '1.3.3.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'spiffform', 'test_spiffform.txt')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.spiffform',
    version=version,
    description="fanstatic spiffform jQuery.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Lugensa GmbH',
    author_email='jd@lugensa.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery',
        'js.jqueryui',
    ],
    entry_points={
        'fanstatic.libraries': [
            'js.spiffform = js.spiffform:library',
        ],
    },
)
