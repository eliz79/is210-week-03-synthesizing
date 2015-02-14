#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {0}! I have {1} news! I won the raffle with number {2}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42

EMAIL = NEWS.format('Pat', '*amazing*', '42')

print EMAIL
