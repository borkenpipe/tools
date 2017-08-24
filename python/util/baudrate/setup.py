from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='baudrate',
      version=version,
      description="Find baudrate of tty device",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='util debug',
      author='devttys0',
      author_email='devttys0@github.com',
      url='https://github.com/devttys0/baudrate',
      license='The MIT License (MIT)',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'pyserial',
      ],
      entry_points={
              'console_scripts': [
                      'baudrate=baudrate.command_line:main'
                          ],
      },
      )
