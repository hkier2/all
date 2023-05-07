import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "6013476307:AAF77yBWHfHNWm7wsnkoMy-KuBJv8OGEsSk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgCbjdRGKeJGoQopnSpnjK7dF1HKX0aKdmp1ICR3yYo-SRFk-JD2rjBV72sgxqcQ8nV71Ehm5Vr2XTlqfuf7FKL65BSRtBUyFt_MBlTLG-XbyG-KycLW7JIHj5HY3sDgxNTcHz3oJkmLR7g76zzQFw_-XZiUw0eMHpsqlq_TBPW8UH1D6eYTMET-cdbB1td5QEH8t0lzXtOXSL0iSJLWPTii-t3OqqL9aLRMnpPiZ3S_UK2G8IeOz1wNdJwuBk_s9c_wlVlOsBJNOXqRg9q4WF0-HJhLbO7Hok_XOHwH-Ft8k88_Ixtiqn4sXX_4iDsv1_yotqwEqKmPmBTHhnWV4ceDAAAAAWaY5PIA")
BOT_USERNAME = getenv("BOT_USERNAME", "mukvbot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1055306199").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "fq_kk")
GROUP = getenv("GROUP", "x4zxx")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


