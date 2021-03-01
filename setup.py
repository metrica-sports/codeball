from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="codeball",
    version="v0.1.3",
    author="Bruno Dagnino",
    author_email="bruno@metrica-sports.com",
    url="https://github.com/metrica-sports/codeball",
    packages=find_packages(exclude=["tests"]),
    description="Data driven tactical and video analysis of soccer games",
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
        "kloppy>=1.1.1",
        "pandas>=1.0.5",
    ],
    extras_require={
        "test": ["pytest"],
        "development": ["pre-commit"],
    },
)
