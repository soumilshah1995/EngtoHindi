from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="englisttohindi",
    version="4.1.0",
    description="""
        Convert English to Hindi with this Python Package it return String  useful for NLP Projects     
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/EngtoHindi",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["englisttohindi"],
    include_package_data=True,
    install_requires=["pandas", "bs4", "requests"]
)