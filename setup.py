from setuptools import setup

_requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    _requirements = [line.strip() for line in f]

setup(
    name="aoc_xjules",
    packages=[
        "utils",
    ],
    author="Julius Parulek",
    install_requires=_requirements,
    author_email="parulek@gmail.com",
    description="advent of codes solution",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    url="https://github.com/xjules/AOC",
)
