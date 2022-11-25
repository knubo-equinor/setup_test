import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "numpy",
    "pandas",
    "requests",
    "pymc", 
    "arviz",
    "graphviz"
]

setuptools.setup(
    name="pymc environment",
    version="0.0.0",
    author="Knut Arne Borresen",
    author_email="knubo@equinor.com",
    description="Setting up for pymc analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
    python_requires='>=3.8',
    install_requires=REQUIREMENTS,
)
