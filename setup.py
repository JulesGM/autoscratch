import os
from pathlib import Path
from setuptools import setup


SCRIPT_DIR = Path(__file__).resolve().parent


setup(
    name = "autoscratch",
    version = "1.0.0",
    author = "Jules Gagnon-Marchand",
    author_email = "jules.gagnonm.alt@gmail.com",
    license = "CC0",
    python_requires=">=3.6.0",
    long_description=(SCRIPT_DIR / "README.md").read_text(),
    scripts=["autoscratch", "unautoscratch"],
    install_requires=[
        mod_name.strip() for mod_name in 
	(SCRIPT_DIR / "requirements.txt").read_text().strip().split("\n")
    ] + ["wheel"],
)
