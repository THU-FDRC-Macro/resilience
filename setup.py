from distutils.core import setup

setup(
    name="Haoxuan Zou",
    version="0.1dev",
    packages=[
        "economicsl@git+https://github.com/ox-inet-resilience/py-economicsl@master",
        "numpy",
    ],
    license="Apache",
    long_description=open("README.txt").read(),
)
