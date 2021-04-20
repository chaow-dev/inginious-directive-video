#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="inginious-directive-video",
    version="0.1.dev0",
    description="Plugin to add Youtube and Vimeo directives",
    packages=find_packages(),
    install_requires=["inginious>=0.6.dev0"],
    tests_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="Chao Porkaew",
    author_email="chaow.po@up.ac.th",
    license="AGPL 3",
    url="https://github.com/pchaow/inginious-directive-video"
)
