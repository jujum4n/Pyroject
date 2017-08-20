#!/usr/bin/env bash
echo 'Regening UI'
pyuic5 design.ui > design.py
echo 'Creating Resource file'
pyrcc5 -o resources.py  pyroject.qrc
