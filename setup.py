from setuptools import setup

setup(name='project-cylon',
      version='2.1.5',
      description='Generic Web Acceptance Testing Framework',
      long_description=
      """
      Project-Cylon framework provide easy way to create web automation test without coding skill, just focus on the test scenario.
      """,
      url='https://github.com/gigapixel/project-cylon',
      author='BridgeAsia Team',
      author_email='gigapixel7@gmail.com',
      license='MIT',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
      ],
      packages=[
        'project_cylon', 'project_cylon/api'
      ],
      package_dir={'project_cylon': 'project_cylon'},
      package_data={'project_cylon': [ 'public/*.*', 'public/css/*.*', 'public/js/*.*' ]},
      entry_points={
          'console_scripts': [
          'cylon=project_cylon.CLI:main', 'behook=project_cylon.behook:main'
      ]},
      install_requires=[
          'pyyaml',
          'behave',
          'selenium',
          'cherrypy'
      ],
      zip_safe=False)
