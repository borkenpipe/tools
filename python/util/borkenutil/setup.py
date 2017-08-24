from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='borkenutil',
      version=version,
      description="common logic functions for python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='util debug logic',
      author='borkenpipe',
      author_email='borkenpipe@gmail.com',
      url='borkenpipe.io',
      license='FreeBSD license',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'markdown',
          'colored',
      ],
      entry_points={
              'console_scripts': [
                      'borke=borkenutil.command_line:main'
                          ],
      },
      )
