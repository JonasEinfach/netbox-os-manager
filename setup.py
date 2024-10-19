from setuptools import find_packages, setup

setup(
    name='netbox-os-manager',
    version='0.1.0',
    description='Netbox plugin to manage operating systems on your network devices',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)