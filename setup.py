import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='genetic_ant-colony-optimization_transport',
    version='0.1.0',
    author='Santiago Torreglosa Diaz',
    author_email='santiagotorreglosadiaz@gmail.com',
    description='This project is a review of the ant colony optimization and genetic algorithms and their applications on transportation engineering',
    python_requires='>=3',
    license='BSD-3',
    url='',
    packages=find_packages(),
    long_description=readme(),
)