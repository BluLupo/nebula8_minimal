#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from core.commands import public ,admin, owner
from telegram.ext import (CommandHandler as CMH,CallbackQueryHandler as CQH,MessageHandler as MH,Filters)

def user_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('start', public.start.init))
def admin_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('ban', admin.ban.init))
def owner_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('test', owner.test.init))