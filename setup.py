from setuptools import setup

NAME = "b0mb3r_cli"
DESCRIPTION = "CLI for sms-bomber `b0mb3r`"
URL = "https://github.com/Moonquit/b0mb3_cli"
EMAIL = ""
AUTHOR = "Moonquit"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0"

with open("requirements.txt", encoding="utf-8") as f:
    REQUIRED = f.readlines()

try:
    with open("README.md", encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=["b0mb3r_cli"],
    entry_points={
        "console_scripts": ["b0mb3r_cli=b0mb3r_cli.cli:main", "bomber_cli=b0mb3r_cli.cli:main"]
    },
    install_requires=REQUIRED,
    extras_require={},
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Internet",
        "License :: OSI Approved :: MIT",
    ],
)