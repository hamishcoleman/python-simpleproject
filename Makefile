
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
	apt-get install python3
	apt-get install python3-coverage

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

# pylint is a little too opinionated to be used by default in the test target
lint:
	pylint3 *.py lib/*

# an alternative to pylint is using flake8:
flake8:
	flake8

clean:
	rm -rf htmlcov .coverage
	find . -name '*.pyc' -print0 |xargs -0 rm
