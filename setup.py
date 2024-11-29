
from setuptools import setup, find_packages

# A requirements.txt fájl beolvasása
def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

setup(
    name='tomi-project',
    version='1.1.0',
    packages=find_packages(),
    install_requires=read_requirements(),  # Függőségek a requirements.txt fájlból
    include_package_data=True,  # Ez biztosítja, hogy a fájlok és mappák is benne legyenek a csomagban
)