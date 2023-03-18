from setuptools import setup, find_packages

long_desc = """
Sphinx extension which enables embedding Datacamp windows to demonstrate Python and R capabilities
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-datacamp",
    version="1.2",
    description="Sphinx datacamp extension",
    author="Arnór Pétur Marteinsson",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
