from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="PythTest",
    version="0.0.1",
    description="Unit Test Builder for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andrew Stoerkel",
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "pythtest=PythTest.__main__:main",
        ],
    },
)