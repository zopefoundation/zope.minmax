##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.minmax package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    text = open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    return text

setup(
    name='zope.minmax',
    version='2.0.0dev',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description=(
        "Homogeneous values favoring maximum or minimum for ZODB "
        "conflict resolution"
        ),
    long_description=(
        read('README.txt')
        + '\n\n' +
        'Detailed Documentation\n' +
        '----------------------'
        + '\n\n' +
        read('src', 'zope', 'minmax', 'minmax.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    license='ZPL 2.1',
    keywords=('zope3 zope zodb minimum maximum conflict resolution'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    url='http://pypi.python.org/pypi/zope.minmax/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope',],
    extras_require=dict(
        test=[],    # removed zope.testing; leaving for backward compatibility
        ),
    install_requires=[
        'setuptools',
        'ZODB3',
        'zope.interface',
        ],
    include_package_data=True,
    zip_safe=False,
    )
