# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

gh_repo = "https://github.com/weaming/math-fold"

setup(
    name="math-fold",  # Required
    version="0.1.4",  # Required
    # This is a one-line description or tagline of what your project does.
    description="back math notaion in CLI",  # Required
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional
    url=gh_repo,  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    keywords="math",  # Optional
    entry_points={
        'console_scripts': [
            'calculate=fold.__main__:main'
        ]
    },  # Optional
    project_urls={"Bug Reports": gh_repo, "Source": gh_repo},  # Optional
)
