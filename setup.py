#!/usr/bin/python3
import codecs
from setuptools import setup, find_packages

bs_socket_service_VERSION = "0.1"
bs_socket_service_DOWNLOAD = ('https://github.com/blackzspace-de-dockerizing/Socket-Communication/latest/' + bs_socket_service_VERSION)


def read_file(filename):
	"""
	Read a utf8 encoded text file and return its contents.
	"""
	with codecs.open(filename, 'r', 'utf8') as f:
		return f.read()

def read_requirements():
    with open('requirements.txt') as f: 
        return f.readlines() 


setup(
	name='bs_socket_service',
	packages=[
		'bs_socket_service',
		'bs_socket_service.mods',
		'bs_socket_service.core',
		'bs_socket_service.core.bin',
		'bs_socket_service.core.services'],
	package_data={
          'bs_socket_service.core': [
              'services/*',
          ],
      },

	version=bs_socket_service_VERSION,
	description='bs_socket_service is a high level MITM framework',
	long_description=read_file('README.md'),
	long_description_content_type='text/markdown',
    # packages = find_packages(),
    entry_points ={ 
            'console_scripts': [ 
                'bs_socket_service = bs_socket_service.bs_socket_service:loop'
            ] 
        },

	license='MIT',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/bs_socket_service/bs_socket_service',
	download_url=bs_socket_service_DOWNLOAD,
	keywords=['python3', 'bs_socket_service', 'wsf', 'MITM', 'wifi', 'arp spoof'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Natural Language :: English',
	],

	install_requires= read_requirements(),

)