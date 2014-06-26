from setuptools import setup

setup(name='project-cylon',
      version='0.5.0',
      description='Generic Web Acceptance Testing Framework',
      long_description=
      """
      Project-Cylon framework provide easy way to create web automation test without coding skill, just focus on the test scenario.
      """,
      url='https://github.com/gigapixel/project-cylon',
      author='Pongrapee J., Kamol C. and Peerapat S.',
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
      install_requires=[
          'pyyaml',
          'behave',
          'selenium'
      ],
      zip_safe=False)
