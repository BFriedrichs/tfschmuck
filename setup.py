from setuptools import setup, find_packages
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        add_path = (path, [])
        for filename in filenames:
            add_path[1].append(os.path.join(path, filename))
        paths.append(add_path)
    return paths

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
      package_data={
        '': ['*.yml'],
      },
      data_files=package_files('tfschmuck/client'),
      zip_safe=False)
