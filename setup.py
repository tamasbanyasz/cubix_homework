
from setuptools import setup, find_packages

# Read requirements.txt 
def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

setup(
    name='tomi-project',
    version='1.1.0',
    packages=find_packages(),
    install_requires=read_requirements(),  
    include_package_data=True, 
)