import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playmedia",
    version="0.0.3",
    author="Satvik Virmani",
    author_email="virmanisatvik01@gmail.com",
    description="A python package to play and control media files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SatvikVirmani/playmedia",
    project_urls={
        "Bug Tracker": "https://github.com/SatvikVirmani/playmedia/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["playmedia"],
    python_requires=">=3.0",
    install_requires=[
        'python-vlc'
    ]
)