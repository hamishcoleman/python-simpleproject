
NAME := theprogram
DESTDIR ?= installdir
INSTALLDIR := $(DESTDIR)/$(NAME)

describe := $(shell git describe --dirty)
tarfile := $(NAME)-$(describe).tar.gz

all:
	false

# python-coverage pulls in these other packages
# - libjs-jquery-hotkeys libjs-jquery-isonscreen libjs-jquery
#   libjs-jquery-tablesorter
# however, it also wants jquery.debounce, which is not packaged.. (but not
# required for functionality...)
# 
build-dep:
	apt-get install -y \
	    python3 python3-coverage \
	    flake8 \
	    isort \

install:
	mkdir -p $(INSTALLDIR)
	cp -pr lib $(INSTALLDIR)/lib
	install -p theprogram.py $(INSTALLDIR)

tar:    $(tarfile)

$(tarfile):
	$(MAKE) install
	tar -v -c -z -C $(DESTDIR) -f $(tarfile) .

test:
	./run_tests.py

cover:
	./run_tests.py cover

.PHONY: lint
lint: lint.flake8 lint.isort

# pylint is a little too opinionated to be used by default in the test target
pylint:
	pylint3 *.py lib/*

# an alternative to pylint is using flake8:
.PHONY: lint.flake8
lint.flake8:
	flake8

.PHONY: lint.isort
lint.isort:
	isort --check-only .

clean:
	rm -rf htmlcov .coverage
	find . -name '*.pyc' -print0 |xargs -0 rm
