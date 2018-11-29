import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_to_opml",
    version="0.0.1",
    author="Jair de Souza Junior",
    author_email="jairsjunior@gmail.com",
    description="A converter tool of JSON object to OPML object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jairsjunior/json-to-opml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)