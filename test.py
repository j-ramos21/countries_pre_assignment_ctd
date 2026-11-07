#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 00:35:56 2026

@author: johannramos
"""

import requests
all_regions = requests.get("https://countries.dev/regions").json()
print(all_regions)