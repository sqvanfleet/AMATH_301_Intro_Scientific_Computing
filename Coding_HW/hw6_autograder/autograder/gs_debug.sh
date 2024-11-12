#!/usr/bin/env bash

python3.10 -m pip uninstall -y gspack
git clone https://github.com/aksholokhov/gspack
cd gspack || exit
python3.10 setup.py develop
