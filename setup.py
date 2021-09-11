#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='matrix-py3',
    version='0.0.4',
    description='Python3 implementation of cmatrix with a timer',
    url='https://github.com/chunribu/matrix-py3',
    author='chunribu',
    author_email='chunribu@mail.sdu.edu.cn',
    packages=find_packages(),
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pebble',
    ],
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='cmatrix python3 timer',
    entry_points={
        'console_scripts': [
            'matrix = matrix3:matrix_cmd',
            'coolmatrix = matrix3:cool_matrix_cmd',
            ]
    }
)