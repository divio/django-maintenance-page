# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from django_maintenance_page import __version__


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]


setup(
    name='django-maintenance-page',
    version=__version__,
    description='Automatic and nice maintenance page when a server error occurs while deploy is running.',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/django-maintenance-page',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=[],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
)
