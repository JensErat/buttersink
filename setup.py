#! /usr/bin/python

""" Package setup for buttersink. """

from setuptools import setup


setup(
    name="buttersink",
    version="0.1",
    packages=['buttersink'],

    # metadata for upload to PyPI
    author="Ames Cornish",
    author_email="buttersink@montebellopartners.com",
    description="Buttersink is like rsync for btrfs snapshots",
    license="GPLv3",
    keywords="btrfs sync synchronize rsync snapshot subvolume buttersink",
    url="https://github.com/AmesCornish/buttersink/wiki",
    # could also include long_description, download_url, classifiers, etc.

    entry_points={
        'console_scripts': ['buttersink=buttersink.buttersink:main'],
    },

    requires=['boto', 'dev', 'psutil'],
    
    # scripts=['buttersink.py'],
    # package_dir={'buttersink': '..'},
    # include_package_data=True,

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires=['docutils>=0.3'],

)