from setuptools import setup, find_packages

setup(
    name='macrobase',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/mbcores/macrobase',
    license='MIT',
    author='Alexey Shagaleev',
    author_email='alexey.shagaleev@yandex.ru',
    description='Macrobase framework for build mAcroservices',
    install_requires=[
        'macrobase-driver==0.0.1',
        'structlog==19.1.0'
    ]
)