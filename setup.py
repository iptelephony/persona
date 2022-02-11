from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in persona/__init__.py
from persona import __version__ as version

setup(
	name="persona",
	version=version,
	description="Allows administrator to impersonate another user.",
	author="Jireh Group",
	author_email="leo at jirehgroup dot asia",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
