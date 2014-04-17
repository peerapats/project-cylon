from setuptools import setup

setup(name='project-cylon',
      version='0.1.1',
      description='Web automated framework with behave and selenium',
      url='https://github.com/gigapixel/project-cylon',
      author='Pongrapee Jencharat, Kamol Chalermviriya and Peerapat Sungkasem',
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