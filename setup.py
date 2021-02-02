import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysenec",
    version="0.1",
    author="Dennis Schwan",
    author_email="dennis.schwan@gmail.com",
    description="A Python API for accessing the Senec Home BMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cathiele/goecharger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    provides=[
        "pysenec"
    ],
    install_requires=[
        'requests'
    ],
    setup_requires=['wheel']
)
