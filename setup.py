from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="scipy-stubs",
    maintainer="Microsoft",
    maintainer_email="scipy@python.org",
    description="PEP 561 type stubs for scipy",
    url="https://scipy.org/",
    license="BSD",
    version="0.0.1",
    packages=["scipy-stubs"],
    # PEP 561 requires these
    package_data=find_stubs("scipy-stubs"),
    zip_safe=False,
)
