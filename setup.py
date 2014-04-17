from setuptools import setup

setup(name='project-cylon',
      version='0.1.1',
      description='Web automated framework with behave and selenium',
      url='https://github.com/gigapixel/project-cylon',
      author='Bridge Asia Group',
      author_email='gigapixel7@gmail.com',
      license='MIT',
      keywords='web automate test framework behave selenium',
      packages=['project_cylon'],
      install_requires=[
          'pyyaml',
          'behave',
          'selenium'
      ],
      zip_safe=False)