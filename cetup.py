from setuptools import find_packages, setup

setup(
    name='netbox-vault',
    version='0.1',
    description='An example NetBox plugin',
    author='Arthur ASCEDU',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)