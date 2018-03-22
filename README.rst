========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires| |codecov| |coveralls|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/tweeder/badge/?style=flat
    :target: https://readthedocs.org/projects/tweeder
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/miroag/tweeder.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/miroag/tweeder

.. |requires| image:: https://requires.io/github/miroag/tweeder/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/miroag/tweeder/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/miroag/tweeder/coverage.svg?branch=master
    :alt: Codecov Coverage Status
    :target: https://codecov.io/github/miroag/tweeder

.. |coveralls| image:: https://coveralls.io/repos/github/miroag/tweeder/badge.svg?branch=master
    :alt: Coveralls Coverage Status
    :target: https://coveralls.io/github/miroag/tweeder?branch=master

.. |version| image:: https://img.shields.io/pypi/v/tweeder.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tweeder

.. |commits-since| image:: https://img.shields.io/github/commits-since/miroag/tweeder/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/miroag/tweeder/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/tweeder.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tweeder

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tweeder.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tweeder

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tweeder.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tweeder


.. end-badges

tweeder - набор утилит для скачивания картинок с русских модельных форумов

* Free software: MIT license

Installation
============

::

    pip install tweeder

Documentation
=============

https://tweeder.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

