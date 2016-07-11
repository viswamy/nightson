# Project Build Commands

project := tinyurl
flake8 := flake8
TARGET ?= tinyurl/tests
TEST_ARGS ?=

pytest_args := -rxs --tb short $(TEST_ARGS) $(project) $(TARGET)
pytest := py.test $(pytest_args)

html_report := --cov-report html
test_args := --cov-report term-missing --cov-report xml --junitxml junit.xml

.DEFAULT_GOAD := test

.PHONY: bootstrap
bootstrap:
	pip install -U "setuptools>=24"
	pip install -U "pip==8.1.2"
	pip install -r requirements.txt
	pip install -r requirements-test.txt
	python setup.py develop

# Build the project when you want to create an egg file.
# For development purposes, do not build it.
# Instead, just bootstrap the project and run.

.PHONY build:
build:
	python setup.py install

.PHONY: clean
clean:
	@find $(project) "(" -name "*.pyc" -o -name "coverage.xml" -o -name "junit.xml" ")" -delete

# Example usage:
# TARGET=torando-app/tests/handlers/test_health.py::test_health make test
.PHONY: test
test: clean
	$(pytest) $(test_args)


.PHONY: testhtml
testhtml: clean
	$(pytest) $(html_report) && open htmlcov/index.html


.PHONY: serve
serve:
	tinyurl-tornado


.PHONY: lint
lint:
	$(flake8) $(project) --config .flake8


.PHONY: docs
docs:
	foober docs make


.PHONY: docsopen
docsOpen: docs
	open docs/_build/html/index.html


.PHONY: shell
shell:
	ipython