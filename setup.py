from setuptools import setup, find_packages
setup(
    name='cl-sugar',
    package_dir = {'': 'src'},
    packages=[''],
    version='1.0',
    description='A program to log the amount of hours you code',
    author='Shai Wilson',
    author_email='sjwilson2@dons.usfca.edu',
    url='https://github.com/shaiwilson/sugar',
    entry_points={
        'console_scripts': [
            'sugar = main:main',
        ],
    },
    keywords=['productivity', 'programming'],
    classifiers=["Programming Language :: Python :: 2.7"],
)