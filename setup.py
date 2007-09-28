from setuptools import setup

long_description = (open("src/zope/minmax/minmax.txt").read() +
                    '\n\n' +
                    open("CHANGES.txt").read())

setup(
    name="zope.minmax",
    version="1.1dev",
    license="ZPL 2.1",
    author="Zope Project",
    author_email="zope3-dev@zope.org",
    description="Homogeneous values favoring maximum or minimum for ZODB "
                "conflict resolution",
    long_description=long_description,
    keywords="zope zope3",

    namespace_packages=["zope"],
    packages=["zope", "zope.minmax"],
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["setuptools", "zope.interface", "ZODB3"],
    tests_require=["zope.testing"],
    zip_safe=False
    )
