import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

version_ns = { }
exec(open('sphinx_aaltoscicomp_branding/_version.py').read(), version_ns)
version = version_ns['__version__']
del version_ns

setuptools.setup(
    name="sphinx_aaltoscicomp_branding",
    version=version,
    author="Richard Darst",
    #author_email="",
    description="HTML theme banding",
    long_description=long_description,
    url="https://github.com/AaltoSciComp/sphinx-aaltoscicomp-branding",
    packages=setuptools.find_packages(),
    package_data={
        "sphinx_aaltoscicomp_branding": ['_static/*'],
        },
    #py_modules=["minipres"],
    keywords='sphinx-extension',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Extension",
    ],
)
