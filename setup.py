from setuptools import find_packages, setup
from scripts.grpc import GrpcCommand

setup(
    name = 'ns-discord',
    packages = find_packages(),
    description = 'NosenStory Discord bot',
    url = 'https://github.com/nosenstory/ns-discord',
    cmdclass = {
        'grpc': GrpcCommand
    }
)
