#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: Apache 2.0 Copyright: 2017, Kovid Goyal <kovid at kovidgoyal.net>

import os
import sys
from distutils.command.build import build as Build
from itertools import chain

from setuptools import Extension, setup

self_path = os.path.abspath(__file__)
base = os.path.dirname(self_path)
sys.path.insert(0, base)
if True:
    from build import (
        SRC_DIRS, TEST_COMMAND, add_python_path, find_c_files, include_dirs, iswindows, libraries,
        library_dirs, version
    )
del sys.path[0]

src_files = tuple(chain(*map(lambda x: find_c_files(x)[0], SRC_DIRS)))
cargs = ('/O2' if iswindows else '-O3').split()
if not iswindows:
    cargs.extend('-std=c99 -fvisibility=hidden'.split())


class Test(Build):

    description = "run unit tests after in-place build"

    def run(self):
        Build.run(self)
        if self.dry_run:
            self.announce('skipping "test" (dry run)')
            return
        import subprocess
        env = add_python_path(os.environ.copy(), self.build_lib)
        print('\nrunning tests...')
        sys.stdout.flush()
        ret = subprocess.Popen([sys.executable] + TEST_COMMAND, env=env).wait()
        if ret != 0:
            raise SystemExit(ret)


setup(
    cmdclass={'test': Test},
    ext_modules=[
        Extension(
            'html5_parser.html_parser',
            include_dirs=include_dirs(),
            libraries=libraries(),
            library_dirs=library_dirs(),
            extra_compile_args=cargs,
            define_macros=[
                ('MAJOR', str(version.major)),
                ('MINOR', str(version.minor)),
                ('PATCH', str(version.patch))
            ],
            sources=list(map(str, src_files)))])
