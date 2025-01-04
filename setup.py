from setuptools import setup, find_packages

setup(
    name='inp_kwargs',
    version='0.1.1',
    packages=find_packages(),
    description='A library for easy input validation with kwargs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Diego Ávila',
    author_email='thecatavila@gmail.com',
    url='https://github.com/TheCatAvila/inp_kwargs.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    keywords='input validation, kwargs, python',
)
