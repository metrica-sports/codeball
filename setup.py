from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="codeball",
    version="0.0.1",
    author="Bruno Dagnino",
    author_email="bruno@metrica-sporst.com",
    url="https://github.com/metrica-sports/codeball",
    packages=find_packages(exclude=["tests"]),
    description="Tactical analysis of football/soccer games",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7, <4",
    install_requires=[
        "kloppy>=1.1.0",
        "pandas>=1.0.5",
    ],
    extras_require={
        "test": ["pytest"],
        "development": ["pre-commit"],
    },
)
