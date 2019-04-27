from distutils.core import setup
import json

with open('TestingSuite/pkg_info.json') as fp:
    _info = json.load(fp)

setup(
    version=_info['version']
    )