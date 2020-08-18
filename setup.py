import os
import re
from setuptools import setup

re_version = re.compile(r".*__version__ = [\'\"](.*?)[\'\"]", re.S)
base_path = os.path.dirname(__file__)
base_package = "aiko_services"

init_path = os.path.join(base_path, base_package, "__init__.py")
with open(init_path, "r") as init_file:
    module_content = init_file.read()
    match = re_version.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError("Cannot find __version__ in {}".format(init_path))


setup(
    name='aiko-services',
    version=version,
    description='Asynchronous message service framework',
    author='Andy Gelme',
    author_email='info@silverpond.com.au',
    packages=[
        base_package,
    ],
    install_requires=[
        'click>=7.0',
        'paho-mqtt>=1.3'
    ],
    entry_points={
        'console_scripts': [
            'service_registrar = aiko_services.service_registrar.service_registrar:main',
#           'aiko = aiko_services.cli:main',
#           'list_services = aiko_services.list_services:main',
#           'pipeline_manager = aiko_services.pipeline_manager:main',
#           'service_manager = aiko_services.service_manager:main',
#           'task_manager = aiko_services.task_manager:main',
        ]
    }
)
