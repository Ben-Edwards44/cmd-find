from setuptools import setup, find_packages


def open_file(filename):
    with open(filename, "r") as file:
        data = file.read()

    return data


setup(
    name = "cmd-find",
    author = "Ben Edwards",
    version = "0.0.1",
    description = "A CLI tool that finds Linux commands from their descriptions",
    long_description = open_file("README.md"),
    long_description_content_type = "text/markdown",
    url = "https://github.com/Ben-Edwards44/cmd_find",
    py_modules = ["main", "app"],
    packages = find_packages(exclude=["create_file"]),
    install_requires = ["numpy",
                        "sentence_transformers"],
    python_requires=">=3.8",
    entry_points = {"console_scripts" : ["cmd_find = main:main", "cmd-find = main:main"]},
    license="MIT"
)