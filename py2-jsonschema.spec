### RPM external py2-jsonschema 2.6.0
## IMPORT build-with-pip

Requires: py2-functools32 py2-repoze-lru py2-argparse
%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/jsonschema

