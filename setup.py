import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playmedia",
    version="1.0.0",
    author="Satvik Virmani",
    author_email="virmanisatvik01@gmail.com",
    description="A python package to play and control media files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/satvikVirmani/playmedia",
    download_url="https://github.com/satvikvirmani/playmedia/releases",
    project_urls={
        "Bug Tracker": "https://github.com/satvikVirmani/playmedia/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=["playmedia"],
    python_requires=">=3.0",
    install_requires=[
        'python-vlc',
        'pretty-errors'
    ]
)