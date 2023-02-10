from setuptools import setup
import setuptools

setup(
    name='Package_Robot',
    version='0.0.1',
    author='Perrichet Théotime',
    description='Package_Robot est un package qui permet de \
    faire bouger un robot dans une grille',
    license='GNU GLPv3', #https://www.gnu.org/licenses/gpl-3.0.en.html
    python_requires='>=3.4',
    package_dir={"": "Package_Robot"},
    packages=setuptools.find_namespace_packages(where="Maps"),
)
