============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <https://github.com/miroag/tweeder/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

mfs could always use more documentation, whether as part of the official mfs docs, in docstrings,
or even on the web in blog posts, articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/miroag/mfs/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)

Development
===========

To set up `mfs` for local development:

1.  Fork `tweeder <https://github.com/miroag/tweeder>`_ (look for the "Fork" button).
2.  Clone your fork locally::

        git clone git@github.com:your_name_here/tweeder.git

3.  Install package locally (for editing).
    Run following command from clone location. Note the '.' at the end of the command line to denote the current folder::

        pip install --editable .

4.  Create a branch for local development::

        git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5.  When you're done making changes, run all the checks, doc builder and spell checker with
    `tox <http://tox.readthedocs.io/en/latest/install.html>`_ one command (you need to ``pip install tox`` first)::

        tox

   You would also need to have python environments for tox to operate. For anaconda based distribution, install them like::

        conda create -y -p C:\python35 python=3.5
        conda create -y -p C:\python36 python=3.6

   see `Stackoverflow article <https://stackoverflow.com/questions/30555943/is-it-possible-to-use-tox-with-conda-based-python-installations>`_ for some extra info

6.  Commit your changes and push your branch to GitHub::

        git add .
        git commit -m "Your detailed description of your changes."
        git push origin name-of-your-bugfix-or-feature

7.  Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run ``tox``) [1]_.
2. Update documentation when there's new API, functionality etc.
3. Add a note to ``CHANGELOG.rst`` about the changes.
4. Add yourself to ``AUTHORS.rst``.

.. [1] If you don't have all the necessary python versions available locally you can rely on Travis - it will
       `run the tests <https://travis-ci.org/miroag/tweeder/pull_requests>`_ for each change you add in the pull request.

       It will be slower though ...

Tips
----

To run a subset of tests::

    tox -e envname -- py.test -k test_myfeature

To run all the test environments in *parallel* (you need to ``pip install detox``)::

    detox

