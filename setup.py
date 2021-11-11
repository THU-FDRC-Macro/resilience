from setuptools import setup, find_packages

setup(
    name="resilience_CH",
    version="0.1dev",
    packages=find_packages(exclude=["tests"]),
    license="Apache",
    long_description=open("README.txt").read(),
)
