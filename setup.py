from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-plugin-template-repository-demo",
    description="Demo of simonw/datasette-plugin-template-repository",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-plugin-template-repository-demo",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-plugin-template-repository-demo/issues",
        "CI": "https://github.com/simonw/datasette-plugin-template-repository-demo/actions",
        "Changelog": "https://github.com/simonw/datasette-plugin-template-repository-demo/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_plugin_template_repository_demo"],
    entry_points={"datasette": ["plugin_template_repository_demo = datasette_plugin_template_repository_demo"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-plugin-template-repository-demo[test]"],
    python_requires=">=3.6",
)
