from setuptools import setup

# get version
__version__ = None
exec(open('protobuf_serialization/version.py').read())

setup(
    name='protobuf-serialization-py',
    version=__version__,
    description="gRPC Python library",
    author='Alvin Chow',
    packages=[
        'protobuf_serialization',
        'protobuf_serialization/deserialization',
        'protobuf_serialization/serialization',
        'protobuf_serialization/test',
    ],
    package_data={},
    scripts=[],
    install_requires=[
        'python-dateutil>=2.7',
        'protobuf>=3.6.0',
    ]
)
