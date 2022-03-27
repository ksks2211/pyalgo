import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyalgo",
    version="0.0.1",
    author="pyy",
    author_email="rival15@naver.com",
    description="personal algorithm note",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kkll22/pyalgo",
    project_urls={"Bug Tracker": "https://github.com/kkll22/pyalgo/issues"},
    license="MIT",
    packages=["pyalgo"],
    install_requires=[],
)
