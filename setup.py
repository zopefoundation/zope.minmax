from setuptools import setup

setup(
    name="zope.minmax",
    version="1.0",
    license="ZPL 2.1",
    author="Zope Project",
    author_email="zope3-dev@zope.org",

    namespace_packages=["zope"],
    packages=["zope", "zope.minmax"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["setuptools", "zope.interface", "ZODB3"],
    tests_require=["zope.testing"],
    description=open('README.txt').read(),
    long_description=open("src/zope/minmax/minmax.txt").read(),
    keywords="zope zope3",
    zip_safe=False
    )
