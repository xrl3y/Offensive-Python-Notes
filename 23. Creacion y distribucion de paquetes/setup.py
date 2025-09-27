# Estructura que se tiene que llevar al realizar la subida de cualquier paquete 

from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hack4u",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Marcelo Vázquez",
    description="Una biblioteca para consultar cursos de hack4u.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://hack4u.io",
)
