from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="writefreely",
    version="0.0.1",
    author="cjeller1592",
    author_email="cjeller1592@github",
    description="A flexible Write Freely API Client library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cjeller1592/WriteFreely-API",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
    zip_safe=False,
)
