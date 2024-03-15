#!\usr\bin\python
"""Setuptools-based installation."""
import os
from pathlib import Path
from typing import List

from setuptools import find_packages, setup

from ml_repo_ex.version import __version__

_PATH_TO_ENVS = 'envs/'
readme = (Path(__file__).parent / 'README.md').read_text()


def get_dependencies() -> List[str]:
    with Path('requirements.txt').open() as file:
        dependencies = [line.rstrip() for line in file if not line.startswith('-') and '@git' not in line]

    for file_name in os.listdir(_PATH_TO_ENVS):
        if file_name.startswith('requirements-'):
            with (Path(_PATH_TO_ENVS) / file_name).open() as file:
                dependencies.extend(
                    [line.rstrip() for line in file if not line.startswith('-') and '@git' not in line]
                )
    return dependencies


setup(
    name='ml_repo_ex',
    packages=find_packages(include=['src']),
    author='Kirill Ivanov',
    version=__version__,
    include_package_data=True,
    install_requires=get_dependencies(),
    long_description=readme,
)
