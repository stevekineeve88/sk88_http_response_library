import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sk88_http_response",
    version="0.0.1",
    author="Stephen Ayre",
    author_email="stevemamajama@gmail.com",
    description="Library for consistent handling of HTTP responses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stevekineeve88/sk88_http_response_library.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.7'
)
