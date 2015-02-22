#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

OLD_WORD = 'Spanish' 
NEW_WORD = 'Flemish'
LEN_TO_REPLACE = len(OLD_WORD)
R_START = inquisition.SPANISH.index(OLD_WORD)
R_END = R_START + LEN_TO_REPLACE 

FLEMISH = inquisition.SPANISH[:R_START] + NEW_WORD + inquisition.SPANISH[R_END:]

print FLEMISH.replace("Spanish", "Flemish")[0:71]


