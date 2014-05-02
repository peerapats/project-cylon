from setuptools import setup

setup(name='project-cylon',
      version='0.2.2',
      description='Web automated testing framework using behave and selenium',
      long_description=
      """
      Project Cylon framework provide easy way to create web automation test without coding skill, just focus on the test scenario.
      """,
      url='https://github.com/gigapixel/project-cylon',
      author='Pongrapee Jencharat, Kamol Chalermviriya and Peerapat Sungkasem',
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