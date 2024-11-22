from setuptools import setup, find_packages

setup(
    name="pydeed",  # The name of your package
    version="0.1.0",  # The current version of your package
    author="Wenlong",  # Replace with your name
    author_email="",  # Replace with your email
    description="A web scraper for Indeed job posts with keyword filtering.",  # Short description of your package
    long_description=open("README.md").read(),  # Long description from your README file
    long_description_content_type="text/markdown",  # Assuming you're using markdown for your README
    url="https://github.com/wenlong2/pydeed",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find your package modules
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[
        "selenium>=4.7.2",
        "beautifulsoup4>=4.11.1",
        "requests>=2.28.2"
    ],  # List of dependencies
    entry_points={
        "console_scripts": [
            "pydeed=pydeed.cli:main",  # Assuming you add a CLI interface later (optional)
        ],
    },
)
