import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="print-hello-to-console",
    version="0.0.2",
    author="Hedy Li",
    author_email="hedyhyry@gmail.com",
    description="Python CLI that prints Hello to the console. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hedythedev/print-hello-to-console-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
