#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
	name = 'nightson',
	version = __version__,
	url = 'http://github.com/vswamy/nightson',
	packages = find_packages(),
	author_email = ['vswamy@outlook.com'],
	entry_points = {
		'console_scripts': [
			'nightson-tornado=nightson.server:serve',
		],
	},
)