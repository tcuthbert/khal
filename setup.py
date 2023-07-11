#!/usr/bin/env python3
import sys

from setuptools import setup

requirements = [
    'khal',
]

setup(
    name='khal-plugin',
    description='A khal event agenda plugin',
    author='khal contributors',
    author_email='khal@lostpackets.de',
    url='http://lostpackets.de/khal/',
    license='Expat/MIT',
    entry_points={
        "khal.formatter": [
            'echo = khal_plugin.plugin:echo'
        ]
    },
    install_requires=[],
    # install_requires=requirements,
    zip_safe=False,  # because of configobj loading the .spec file
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console :: Curses",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
        "Topic :: Communications",
    ],
)
