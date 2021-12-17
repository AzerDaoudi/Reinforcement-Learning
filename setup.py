from setuptools import find_packages, setup


setup(
    name='reinforcement_learning',
    packages=find_packages(include=['reinforcement_learning']),
    version='0.0.1',
    description='basic reinforcement learning library',
    author='Azer Daoudi',
    install_requires=['numpy==1.18.5'],

)