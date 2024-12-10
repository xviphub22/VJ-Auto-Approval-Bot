# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28703774"))
    API_HASH = getenv("API_HASH", "753e1a1a07fd474435e8534ebb33030b")
    BOT_TOKEN = getenv("BOT_TOKEN", "7820502843:AAEAJSSpE-UY0w1hTgAekQr94wi9wmKiOa0")
    FSUB = getenv("FSUB", "autoaprovejoin_requestbot")
    CHID = int(getenv("CHID", "-7820502843"))
    SUDO = list(map(int, getenv("SUDO", "1862821779").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://indiandesi491:rgW2PYgMMAxVDaYz@cluster0.wzhv7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
