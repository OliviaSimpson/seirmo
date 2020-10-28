#
# This file is part of seirmo (https://github.com/SABS-R3-Epidemiology/seirmo/)
# which is released under the BSD 3-clause license. See accompanying LICENSE.md
# for copyright notice and full license details.
#
#
# Version information for seirmo.
#
# See: https://packaging.python.org/guides/single-sourcing-package-version/
#
# Version as a tuple (major, minor, revision)
#  - Changes to major are rare
#  - Changes to minor indicate new features, possible slight backwards
#    incompatibility
#  - Changes to revision indicate bugfixes, tiny new features
VERSION_INT = 0, 0, 1

# String version of the version number
VERSION = '.'.join([str(x) for x in VERSION_INT])
