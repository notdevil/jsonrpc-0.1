#!/usr/bin/env python

from setuptools import setup

setup(name='jsonrpc',
	version='0.1',
	description='Python JSON RPC implementation',
	author='Roland Koebler',
	author_email='rk@simple-is-better.org',
	url='http://www.simple-is-better.org/rpc/',
	py_modules=['jsonrpc', 'cbrxapi'],
	install_requires=['simplejson'],
	)
