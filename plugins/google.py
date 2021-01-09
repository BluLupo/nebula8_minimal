#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_menu(buttons, n_cols, header_buttons=False, footer_buttons=False):
  menu=[buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

def init(update, context):
    bot = context.bot
    msg=str(update.message.text[7:]).strip()
    if msg != "":
        main_text = "Here are the results of your Google search"
        gurl = "https://www.google.com/search?&q={0}".format(msg.replace(' ','+'))
        button_list = [InlineKeyboardButton("Go to =>", url=gurl)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,text=main_text,reply_markup=reply_markup,parse_mode='HTML')
    else:
        msg = "You need to type a search criteria!\nHow to use the command: <code>/google text</code>"
        bot.send_message(update.message.chat_id,text=msg,parse_mode='HTML')