"""
    Setup file for uni_electrolyte.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.5.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import os

from setuptools import setup, find_packages

if __name__ == "__main__":
    def _process_requirements():
        os.system('pip install -r requirements.txt')
        packages = open('requirements.txt').read().strip().split('\n')
        requires = []
        for pkg in packages:
            if pkg.startswith('--find-links'):
                continue
            else:
                requires.append(pkg)
        return requires


    with open('version.txt', 'r') as f:
        for version in f.readlines():
            version = version.strip()
            break

    setup(
        name='uni_electrolyte',
        version=version,
        author='Mingkang Liu',
        description="A unified framework for AI techniques in electrolyte.",
        packages=find_packages(),
        install_requires=_process_requirements()
    )







