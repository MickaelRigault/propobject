#! /usr/bin/env python
#

DESCRIPTION = "propobject: Low level object to inherit from"
LONG_DESCRIPTION = """\
    Structure to handle the
    _proprerties, _side_properties, _derived_properties
    tricks.

    A class inheriting from BaseObject could have the following
    global-class variables:

    ```
    PROPERTIES         = ["a","b"]
    SIDE_PROPERTIES    = ["t"]
    DERIVED_PROPERTIES = ["whynot"]
    ```
    if so, object created from this class or any inheriting class
    could have access to the self._properties["a"], self._properties["b"]
    self._side_properties["t"] or self._derived_properties["whynot"]
    parameters.

    BaseObject have a basic .copy() method.
"""

DISTNAME = 'propobject'
AUTHOR = 'Mickael Rigault'
MAINTAINER = 'Mickael Rigault' 
MAINTAINER_EMAIL = 'mrigault@physik.hu-berlin.de'
URL = 'https://github.com/MickaelRigault/propobject/'
LICENSE = 'Apache 2.0'
DOWNLOAD_URL = 'https://github.com/MickaelRigault/propobject/tarball/0.1'
VERSION = '0.1.2'

try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():
   install_requires = []
   # Just make sure dependencies exist, I haven't rigorously
   # tested what the minimal versions that will work are
   # (help on that would be awesome)
   return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ['propobject']

    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=packages,
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
      )
