from telegram import ChatAction
import html
import re
import json
import random
from random import randint
from datetime import datetime
from typing import Optional, List
import pyowm
import time
import requests
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler, run_async, Filters
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from telegram.utils.helpers import escape_markdown, mention_html
from zalgo_text import zalgo    

def zal(bot: Bot, update: Update, args):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    if update.message.reply_to_message is not None:
        args = update.message.reply_to_message.text
        args = args.split(" ")
    input_text = " ".join(args).lower()
    if input_text == "":
        update.message.reply_text("Type in some text!")
        return
    zalgofied_text = zalgo.zalgo().zalgofy(input_text)
    update.message.reply_text(zalgofied_text)

dispatcher.add_handler(CommandHandler('zal', zal, pass_args=True))
