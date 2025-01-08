# ############################################
#
#         TrakteerDonate Package Setup
#          ~~ 2023 (c) by Realzzy ~~
#           2025 Recode by ©Lucifer
#
# ############################################


import re

from setuptools import find_packages, setup


with open("trakteer_dev/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="trakteer-dev",
    version=version,
    description="## [FORK](https://github.com/then77/trakteerdonate.git)",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jonesroot",
    author="Lucifer@Navy",
    author_email="luci@team.navy",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Indonesia🇮🇩, English🇺🇸, Javanese🇮🇩",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="trakteer api",
    project_urls={
        "Tracker": "https://github.com/team/team/issues",
        "Community": "https://t.me/DisiniNavy",
        "Source": "https://github.com/jonesroot",
    },
    python_requires=">=3.9,<=3.11.11",
    package_data={
        "trakteer_dev": ["py.typed"],
    },
    packages=find_packages(exclude=["compiler*", "tests*"]),
    zip_safe=False,
)
