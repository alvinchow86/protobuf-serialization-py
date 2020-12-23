from os import path
from setuptools import setup

# get version
__version__ = None
exec(open('protobuf_serialization/version.py').read())

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='protobuf-serialization',
    version=__version__,
    description="Helpers for protobuf3 serialization and deserialization",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alvinchow86/protobuf-serialization-py',
    author='Alvin Chow',
    author_email='alvinchow86@gmail.com',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        'protobuf_serialization',
        'protobuf_serialization/deserialization',
        'protobuf_serialization/serialization',
    ],
    package_data={},
    scripts=[],
    install_requires=[
        'python-dateutil>=2.7',
        'protobuf>=3.6.0',
    ],
    python_requires='>=3.6',
)
