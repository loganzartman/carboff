import setuptools
import carboff

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="carboff",
    version=carboff.__version__,
    author="",
    author_email="",
    description="A REST API for determining the carbon impact of internet usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/loganzartman/carboff",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "Flask==1.1.1",
        "Flask-API==2.0"
    ],
    extras_require={
        "dev": [
            "autopep8==1.4.4"
        ]
    }
)
