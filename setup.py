import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typewrap",
    version="0.0.1",
    author="Austin Poor",
    author_email="author@example.com",
    description="A super small package for function input type checking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/typewrap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)