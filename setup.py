from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flappy_bird_engine", 
    version="0.0.1",
    author="Joshua Billson",
    author_email="jmbillson@outlook.com",
    description="A game engine for Flappy Bird powered by Pygame.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoshuaBillson/Flappy_Bird_Engine.git", 
    package_dir={'': 'flappy_bird'},
    packages=find_packages('flappy_bird'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
