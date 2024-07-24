"""Setup module for anthropic-hass."""

import pathlib

from setuptools import find_packages, setup

VERSION = "1.0.0"


def long_description():
    """Read README.md file."""
    f = (pathlib.Path(__file__).parent / "README.md").open()
    res = f.read()
    f.close()
    return res  # noqa: R504


setup(
    name="anthropic_hass",
    version=VERSION,
    description="Home Assistant custom component for Anthropic Claude conversation agent",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Shulyaka/anthropic-hass",
    author="Denis Shulyaka",
    author_email="ds_github@shulyaka.org.ru",
    license="GNU General Public License v3.0",
    keywords="anthropic claude conversation agent ai",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.12",
    tests_require=["pytest"],
)
