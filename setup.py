#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:expandtab
# Copyright 2016, 2017 juga (juga at riseup dot net), MIT license.

"""Setup."""
import subprocess

from setuptools import find_packages, setup

import dhcpcanon


def systemd_unit_dir():
    cmd = ['pkg-config',  '--variable', 'systemdsystemunitdir', 'systemd']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    if proc.returncode != 0 or stdout is None:
        return None  # systemd not found
    if isinstance(stdout.strip(), bytes):
        return stdout.strip().decode('utf-8')
    return stdout.strip()


def systemd_tmpfiles_dir():
    # There doesn't seem to be a specific pkg-config variable for this
    cmd = ['pkg-config',  '--variable', 'prefix', 'systemd']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    (stdout, stderr) = proc.communicate()
    if proc.returncode != 0 or stdout is None:
        return None  # systemd not found
    d = stdout.strip()
    if isinstance(d, bytes):
        d = d.decode('utf-8')
    return d + '/lib/tmpfiles.d'


if systemd_unit_dir():
    data_files = [
        (systemd_unit_dir(), ['systemd/dhcpcanon.service']),
        (systemd_tmpfiles_dir(), ['tmpfiles.d/dhcpcanon.conf']),
        ('sbin', ["sbin/dhcpcanon-script"])
    ]
else:
    data_files = []

test_requirements = ['coverage', 'tox', 'pytest']

setup(
    name='dhcpcanon',
    version=dhcpcanon.__version__,
    description=dhcpcanon.__description__,
    long_description=dhcpcanon.__long_description__,
    author=dhcpcanon.__author__,
    author_email=dhcpcanon.__author_mail__,
    license='MIT',
    url=dhcpcanon.__website__,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        "attrs>=16.3",
        "dbus-python>=1.2",
        "netaddr>=0.7",
        "lockfile>=0.12",
        "pip>=8.1",
        "pyroute2>=0.3",
        'scapy-python3>=0.20',
    ],
    python_requires=">=3.5",
    extras_require={
        'dev': ['flake8'],
        'test': test_requirements,
        'doc': ['sphinx', 'sphinx-bootstrap-theme', 'pylint']
    },
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'dhcpcanon = dhcpcanon.dhcpcanon:main',
        ]
    },
    # NOTE: not installing system files as the user might want to install them
    # in a custom prefix or without systemd
    # data_files=data_files,
    zip_safe=False,
    include_package_data=True,
    keywords='python scapy dhcp RFC7844 RFC2131 anonymity',
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Environment :: Console",
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
    ],
)
