#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import plugins
from telegram.ext import (CommandHandler as CMH)

def function_plugins(dsp):
    function = dsp.add_handler
    function(CMH('google',plugins.google.init))