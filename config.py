## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBSsBAbPyipBpVTU2OtOEH45BXyrcduUFz6IOoXoGR1z4oiS9wRL-O3OJ633EDFtH2-6IsYN1MDogSxcaxc8o_diWz_Z0eoN_0VHnFzEXEKA5lpxEVrhuwlrKjPxZPuY7Y_XRCFPsabcfyrmKzosUofjSkzJJshny8Bi2wvkZ4xq_rAO46VEKdVoJCDlw3lFY2xVQ367baS9cqc-nQDMQotOq6xR5PZO6x12nGvLKinqeYIHv6hY5w4H-Es7vflVKawJQFIFZRQ86RpvijTqaP4fkaBsaH8jJVvMn9HjHU-VM0b6OnNFJ7ub1K-viv-jxSMZouFIK4Ft-ZyP-NBB4KNAAAAATPlyNUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5455184404:AAF9eVPQE0S5YMufEA0h7Z7vB54bxh9wjaA")
BOT_NAME = getenv("BOT_NAME", "🎧 𝗝𝗢𝗭 𝗠𝗨𝗦𝗜𝗖 🎧")
API_ID = int(getenv("API_ID", "13923299"))
API_HASH = getenv("API_HASH", "500ff182245a31f3f941ffa2bc81192f")
OWNER_NAME = getenv("OWNER_NAME", "JOSEF")
OWNER_USERNAME = getenv("OWNER_USERNAME", "JOSEFI0")
ALIVE_NAME = getenv("ALIVE_NAME", "JOSEF")
BOT_USERNAME = getenv("BOT_USERNAME", "jozmusic")
OWNER_ID = getenv("OWNER_ID", "399401433")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "🎧 ＪＯＳＥＦ 🎧")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/zho_josefo")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "399401433 2090788121").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
