all:
	@echo "dev_install       - Install development dependencies"
	@echo "test              - Run tests"
	@echo "typecheck         - Run static type checking only python>=3.10"
	@echo "lint              - Run static analysis for common problems"
	@echo "autoformat        - Format all code to a consistent style"
	@echo "coverage          - Run tests and check the test coverage"
	@echo "benchmark         - Run a small suite to check performance"
	@echo "ci_install        - Install dependencies needed for CI"
	@echo "fixed_install     - Install as a non-editible package like production consumers"
	@echo "clean             - Delete generated files"
	@echo "dist              - Build distribution artifacts"
	@echo "release           - Build distribution and release to PyPI."

test:
	python -m pytest -m 'not benchmark' -m 'not floats'

test_with_floats:
	python -m pytest -m 'not benchmark'

benchmark:
	python -m pytest -m benchmark tests/performance*

coverage:
	python -m pytest --cov=tuplesumfilter tests --cov-fail-under 90

typecheck:
	python -m mypy ./src ./tests

lint:
	black --check .
	prospector .

autoformat:
	black .

clean:
	rm -rf build dist src/*.egg-info .tox .pytest_cache pip-wheel-metadata .DS_Store
	find src -name '__pycache__' | xargs rm -rf
	find tests -name '__pycache__' | xargs rm -rf

dev_install:
	python -m pip install -e .[dev]

ci_install:
	python -m pip install -e .[ci]

fixed_install:
	python -m pip install -e .[ci]

dist: clean
	git diff --exit-code			# Check for unstaged changes
	git diff --exit-code --cached	# Check for uncommitted changes
	check-manifest
	python setup.py sdist bdist_wheel

release: dist
	twine upload dist/*.*

.PHONY: all autoformat benchmark ci_install clean coverage dev_install dist fixed_install test typecheck