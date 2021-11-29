import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "phishdet",
    version = "1.0",
    author = "HS Devansh Raghav",
    author_email = "indiananonymous75@gmail.com",
    license = "MIT",
    url = "https://github.com/whoamisec75/phishdet",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'requests',
        'ipwhois',
    ],
    entry_points={
        'console_scripts': [
            'phishdet = phishdet.__main__:main'
        ]
    },
)