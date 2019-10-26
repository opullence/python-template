from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("requirements/production.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="opulence.python-template",
    version="0.1.0",
    description="Template for creating new python projects",
    long_description=readme,
    author="Opulence",
    author_email="contact@opulence.fr",
    url="https://github.com/opullence/python-template",
    license=license,
    packages=find_namespace_packages(include=["opulence.*"]),
    entry_points={
        "console_scripts": [
            "opulence-python-template=opulence.python_template.__main__:main"
        ]
    },
    install_requires=requirements,
    python_requires=">=3.6.*, <4",
)
