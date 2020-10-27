AaltoSciComp branding for Sphinx
================================

This adds a HTML favicon to the Sphinx project to brand it for
AaltoSciComp.  But, so that others can fork our repositories without
misrepresenting the origin, it detects if the project is being built
in an official location, and only brands it in that case.

It detects the official locations via:

- The environment variable ``GITHUB_REPOSITORY`` starts with
  ``AaltoSciComp``.  `GitHub does this
  <https://docs.github.com/en/free-pro-team@latest/actions/reference/environment-variables>`__.

- The environment variable ``AALTOSCICOMP`` is set.

This code has an open license (and also probably the projects that use
the code), but misrepresenting the author of a project is another
matter and not allowed!  We aim to make it easy to satisfy that.
Derivative works should cite original source and briefly explain what
is different.



See also
--------

https://github.com/AaltoSciComp/aalto-scicomp-graphics



License
-------

This package, *except* for the logo icon itself, is licensed under the
CC-BY.  Currently, no comment is made on the logo.
