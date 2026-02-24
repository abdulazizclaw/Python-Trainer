from setuptools import setup, find_packages

setup(
    name="python-trainer",
    version="1.0.0",
    description="A comprehensive Python learning platform for absolute beginners",
    author="Python Trainer",
    author_email="trainer@python.local",
    url="https://github.com/abdulazizclaw/Python-Trainer",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
        "colorama>=0.4.6",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
