#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text-ide-Zuap",
    version="0.0.1",
    author="Paulo Martins @ www.paulojorgepm.net",
    author_email="paulo.jorge.pm@gmail.com",
    description="NLP tools for the TextIDE project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/Paulo-Jorge/text-ide-kivy/src/master/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)