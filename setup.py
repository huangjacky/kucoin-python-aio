#!/usr/bin/env python
from setuptools import setup

setup(
    name='kucoin-python-aio',
    version='1.0.0',
    packages=['kucoin'],
    description='Kucoin API Client For V2',
    url='https://github.com/huangjacky/python-kucoin',
    author='HuangJacky',
    license='MIT',
    author_email='huangjacky@163.com',
    install_requires=['aiohttp'],
    keywords='kucoin api btc eth kcs usdt',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
