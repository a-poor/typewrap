import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typewrap",
    version="0.2.6",
    author="Austin Poor",
    author_email="austinpoor@gmail.com",
    description="A super small package for function input type checking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-poor/typewrap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
)
