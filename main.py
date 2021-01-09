#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
import logging
from telegram.ext import Updater
from core.commands import index
from plugins import plugin_index
from core import handlers
from core.handlers import handlers_index

ENABLE_PLUGINS = True
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    updater = Updater("TOKEN HERE", use_context=True)
    dsp = updater.dispatcher

    index.user_command(dsp)
    index.admin_command(dsp)
    index.owner_command(dsp)
    #Plugins Section
    if ENABLE_PLUGINS == True:
        plugin_index.function_plugins(dsp)
        print("Enable Plugins")
    else:
        print("Disable Plugins")

    handlers_index.core_handlers(dsp)
    #handlers.logs.sys_loggers()

    dsp.add_error_handler(handlers.errors.error_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()