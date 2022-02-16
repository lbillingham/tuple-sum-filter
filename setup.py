from setuptools import setup, find_packages

EXTRAS_REQUIRE = {
    "ci": [
        "black==22.1.0",
        "coverage[toml]==6.3.1",
        "prospector[with_everything]==1.6.0",
        "pytest==7.0.1",
        "pytest-benchmark==3.4.1",
        "pytest-cov==3.0.0",
    ],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["ci"] + [
    "mypy",
    "twine",
    "wheel",
]

setup(
    name="tuple-sum-filter",
    description="Library to play with filtering numeric sequences by sums of their pairs, triplets, etc. With a bonus CLI demo",
    version="0.0.1",
    author="Laurence Billingham",
    author_email="laurence.billingham+wflyr@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["click>=8.0.3", "structlog>=1.5.0"],
    extras_require=EXTRAS_REQUIRE,
    entry_points={"console_scripts": ["filter_demo=tuplesumfilter.scripts:cli"]},
)
