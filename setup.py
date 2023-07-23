from setuptools import setup, find_packages

setup(
    name='utilsjo',
    version='1.0',
    author='Luis Alfredo Alvarado Rodríguez',
    author_email='laalvarado@ine.gob.gt',
    description='Una colección de funciones para la manipulación de fechas y muchas cosas mas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/1u1s4/utilsjo',
    keywords='development, setup, setuptools',
    python_requires='>=3.7',
    packages=find_packages(),
    py_modules=['utilsjo'],
    install_requires=['python-dateutil']
)
