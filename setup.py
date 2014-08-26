from setuptools import setup

setup(name='project-cylon',
      version='1.1.3',
      description='Generic Web Acceptance Testing Framework',
      long_description=
      """
      Project-Cylon framework provide easy way to create web automation test without coding skill, just focus on the test scenario.
      """,
      url='https://github.com/gigapixel/project-cylon',
      author='Peerapat S., Kamol C. and Pongrapee J.',
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
      packages=['project_cylon'],
      entry_points={
          'console_scripts': [
          'cylon=project_cylon.CLI:main', 'behook=project_cylon.behook:main'
      ]},
      install_requires=[
          'pyyaml',
          'behave',
          'selenium'
      ],
      zip_safe=False)
