from setuptools import setup, find_packages

setup(
    name='funcionesjo',
    version='0.2.6',
    author='Luis Alfredo Alvarado Rodríguez',
    author_email='laalvarado@ine.gob.gt',
    description='Una colección de funciones para la manipulación de fechas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/1u1s4/funcionesjo',
    keywords='development, setup, setuptools',
    python_requires='>=3',
    packages=find_packages(),
    py_modules=['funcionesjo'],
    install_requires=['python-dateutil']
)
