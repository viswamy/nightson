#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.0.0'

setup(
	name = 'tinyurl',
	version = __version__,
	url = 'http://github.com/vswamy/tinyurl',
	packages = find_packages(),
	author_email = ['vswamy@outlook.com'],
	entry_points = {
		'console_scripts': [
			'tinyurl-tornado=tinyurl.server:serve',
		],
	},
)