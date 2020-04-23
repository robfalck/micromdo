from distutils.core import setup
from setuptools import find_packages


setup(name='micromdo',
    version='0.0.1',
    description='Minimal implementation of UDE',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    install_requires=[
        'numpy>=1.14.1',
    ],
    zip_safe=False,
)
