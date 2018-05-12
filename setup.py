from setuptools import setup, find_packages

setup(name='tfschmuck',
      version='0.1',
      description='A package for the tfschmuck site',
      url='http://github.com/BFriedrichs/tfschmuck',
      author='Björn Friedrichs',
      author_email='bjoern@friedrichs1.de',
      license='',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'tfschmuck=tfschmuck.server.cli:cli'
          ]
      },
      zip_safe=False)
