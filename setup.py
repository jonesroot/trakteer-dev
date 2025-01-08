# ############################################
# 
#         TrakteerDonate Package Setup        
#          ~~ 2023 (c) by Realzzy ~~
#           2025 Recode by ©Lucifer
# 
# ############################################

from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="trakteer-dev",
    version="0.0.1",
    author="Realzzy",
    author_email="hello@therealzzy.xyz",
    description="[Fork and try to Fixing] An easy way to listen for Trakteer donation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/then77/trakteer-dev",
    packages=find_packages('trakteer-dev'),
    package_dir={'': 'trakteer-dev'},
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
    python_requires=">=3.6",
)
