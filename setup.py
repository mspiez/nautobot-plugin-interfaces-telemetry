from setuptools import find_packages, setup

setup(
   name='nautobot_interfaces_telemetry',
   version='0.0.1',
   description='Interfaces Status in Nautobot',
   author='Michal Spiez',
   author_email='mspiez@gmail.com',
   packages=find_packages(),
   include_package_data=True,
)
