import setuptools
import os

# read requirements.txt and install them as dependencies for the project
install_requires = [
    "redis"
]  # Here we'll get: ["redis", "flask", "flask_cors"]
if os.path.isfile("requirements.txt"):
    with open("requirements.txt") as fp:
        for line in fp.read().splitlines():
            if line.startswith("scrape") or line.startswith("setuptools"): continue
            install_requires.append(line)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='scrape',
    python_requires=">=3.6",
    version='0.1.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    extras_require={
        'helpers': ["pipreqs", "pytest", "flake8"],
    },
)
