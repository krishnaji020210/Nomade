# ============================================================
#Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/+t42KngFTf5A2YzEx
# Channel: https://t.me/l_ll_Lord_Krishna_ll_l
# YouTube: https://youtube.com/@kanhajikideewani
# License: Open-source (keep credits, no resale)
# ============================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("@l_ll_KRISHNA_ll_l_l", 0))
BOT_USERNAME = os.getenv("@The_Lord_Sasuke_assistant_bot", "NomadeHelpBot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+t42KngFTf5A2YzEx")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/l_ll_Lord_Krishna_ll_l")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/e8nobe.jpg")
