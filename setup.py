# ############################################
#
#         TrakteerDonate Package Setup
#          ~~ 2023 (c) by Realzzy ~~
#           2025 Recode by ©Lucifer
#
# ############################################

from pathlib import Path

from setuptools import find_packages, setup

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "I'm From Indonesian, and I'm still learning."


setup(
    name="trakteer-dev",
    version="0.0.2",
    author="Navy",
    author_email="lucifer@navy.world",
    description="[Fork and try to Fixing] An easy way to listen for Trakteer donation in Python\n\n\nSourcr: [Here](https://github.com/then77/trakteer-dev.git)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/jonesroot/trakteer-dev",
    packages=find_packages(),
    package_dir={"trakteer_dev"},
    install_requires=["websockets", "rich"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">= 3.9",
)
