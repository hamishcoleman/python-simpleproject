#!/usr/bin/env python3

"""This is a test harness.

it finds all the test scripts in this dir and in
the lib dir and runs the tests.  It optionally does a code coverage check
as well
"""

import os
import sys
import unittest

from coverage import Coverage

# Ensure that we look for any modules in our local lib dir.  This allows simple
# testing and development use.  It also does not break the case where the lib
# has been installed properly on the normal sys.path
sys.path.insert(0,
                os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'lib'))
# I would use site.addsitedir, but it does an append, not insert


def main():
    """Do the main test logic."""
    if len(sys.argv) > 1 and sys.argv[1] == 'cover':
        # FIXME - there are enough args now to need an arg parser
        cover = Coverage(branch=True, auto_data=True)
        min_percent = 0

        if len(sys.argv) > 2:
            min_percent = float(sys.argv[2])
    else:
        cover = False

    loader = unittest.defaultTestLoader
    runner = unittest.TextTestRunner(verbosity=2)

    if cover:
        cover.erase()
        cover.start()

    tests = loader.discover('.')
    tests_lib = loader.discover('lib', top_level_dir='lib')
    tests.addTests(tests_lib)
    result = runner.run(tests)

    if cover:
        cover.stop()
        # the debian coverage package didnt include jquery.debounce.min.js
        # (and additionally, that thing is not packaged for debian elsewhere)
        try:
            cover.html_report()
        except: # noqa pylint: disable=bare-except
            pass
        # TODO - reconfirm that this packaging issue is still the case
        #        if it is not, remove the try..except
        #        if it is, add the specific exception

        percent = cover.report(show_missing=True)

        if min_percent > percent:
            print("The coverage ({:.1f}% reached) fails to reach the "
                  "minimum required ({}%)\n".format(percent, min_percent))
            exit(1)

    if not result.wasSuccessful():
        exit(1)


if __name__ == '__main__':
    main()
