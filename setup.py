#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='matrix-py3',
    version='0.0.1',
    description='Python3 implementation of cmatrix with a timer',
    url='https://github.com/chunribu/matrix-py3',
    author='chunribu',
    author_email='chunribu@mail.sdu.edu.cn',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Intended Audience :: Researchers :: Developers',
        'Topic :: Software Development :: Interpreters',
        'Operating System :: Linux :: OS X',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='cmatrix python3 timer',
    entry_points={
        'console_scripts': [
            'matrix = matrix3:matrix'
            ]
    }
)