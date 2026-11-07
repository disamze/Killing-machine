# monster_hell_bot.py
# bot curated by Sam


import asyncio, json, os, random, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging
from typing import Dict, List, Set
import concurrent.futures

# ---------------------------
# CONFIG
# ---------------------------
TOKENS = [
"9202934886:AAHuuirPg0tUX9j1e7g4OYYCjfZeJ9cFpf8",
"8856737698:AAHBTts-xXVuilnyDhXC3_AYBfTiU4phJi8",

]

OWNER_ID = 6762302256
SUDO_FILE = "0752.json"

# ---------------------------
# RAID TEXTS
# ---------------------------
RAID_TEXTS = [
    "𝑮𝑪 𝑳𝑬𝑭𝑻 𝑳𝑬 लंगड़ी ᴍᴀᴀ ᴋᴇ ʙᴀᴄʜᴇ 🤮",
    "Tmkc pe chppl hi chppl marunga !! 🔥😂🩴 ",
    "𝐂ʜʟ 𝐇ᴀʀᴍᴢᴀᴅ𝐈 𝐊ᴇ लड़के 💛🤍🩵",
    "sort nhi krunga chud tu bina ruke 🤢🔥 ",
    "काले Doraemon रोता reh 🤣🤣 ",
    "Awaz neeche rndy k bacche 🤢🔥",
    "𝙇𝙐𝙉𝘿 𝘾𝙃𝙐𝙎  🥶➿🩵 𝙈𝘼𝘿𝘼𝙍𝘾𝙃𝙊𝘿 ",
    "Sawal mt puch tery ma k bosda 😹🖕🏻",
    "Are try maa ka bosda 🤢᭄᭄᭄ 🌟 𝙇𝙐𝙉𝘿 𝘾𝙃𝙐𝙎 🤪᭄᭄",
    "fyter bnege langde madarchod 😂💥",
    "𝟏𝐱 𝐀ɴ𝐘 𝐂ʜ𝐋 𝐏ɪʟʟ𝐄 𝐍ᴏᴛ𝐈 𝐂ʟᴀɪ𝐌 𝐊ᴀ𝐑 🩷🩵🩶",
    "try maa > Mia Khalifa 🥵💯",
    "baap se fyt krega 😂😂 ?",
    "ATMKBFJ 🥀",
    "Mᴀᴀ Kᴇ Sᴀᴛʜ bhen ᗷᕼI ᥴᕼꪊ໓ ᭙ꫝꪶi 🤢🔥",
    "Teri maa ko Gachar Gachar codunga 😹❌🔥",
    "रंडीꪻ ♡︎ 🎀",
    "𝐓𝐆 𝐅𝐘𝐓𝐄𝐑 𝐁𝐍𝐄𝐆𝐀 ?? 𝐂𝐇𝐎𝐃𝐔 𝐓𝐄𝐑𝐈 𝐌𝐀𝐀 😂😂",
    "𝐓𝐎𝐓𝐋𝐄 𝐓𝐌𝐊𝐂 𝐌𝐄 𝐁𝐎𝐌𝐁 𝐅𝐄𝐊𝐃𝐔 💣💥",
    "Ｔᴏʜᴀʀ Ｍᴀɪʏᴀ Ｃʜᴀɪʏᴀ Ｃʜᴀɪʏᴀ 🤢🔥🤢🔥",
    " 𝙏𝙚𝙧𝙞 𝙢𝙖𝙖 𝙠𝙚 𝙗𝙝𝙤𝙨𝙙𝙚 𝙢𝙚 𝙡𝙖𝙩 𝙥𝙙𝙚𝙣𝙜𝙚 𝙗𝙝𝙤𝙩 𝙩𝙚𝙯 👻💥",
    "🦅🔥 Tᴇʀɪ 🦅🔥 Mᴀᴀ 🦅🔥 Rɴᴅɪ 🦅🔥",
    "कि बेहन 𝗧𝗔𝗞𝗟𝗜 💙",
    "𝗚𝗨𝗟𝗔𝗠 🥱👞",
    "ʙꪊʟʟꪗ केन्द्र ᥫ😂᭄",
    "तेरी माँ कि 𝘾ʜᴜᴛ में જ⁀➴🧨᭄",
    "𝘙𝘈𝘕𝘋 𝘽𝙃𝙀𝙀𝙆 𝙈𝘼𝙉𝙂 😹😹",
    "𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𝙇𝘼 🤲🏿",
    "Bol #Sam   ᴅꫝᴅᴅꪗ ❤‍🩹",
    "༆🤮꧂तेरी मांँ 売春婦 ᥫ😆᭄",
    "𝘽𝘼𝙐𝙉𝙀 मादरचोद ꧁🤮꧂",
    "𝐓𝐌𝐊𝐁 😹🔥😹🔥",
]

# ---------------------------
# NCEMO EMOJIS
# ---------------------------
NCEMO_EMOJIS = [
    "😋","😝","😜","🤪","😑","🤫","🤭","🥱","🤗","😡","😠","😤",
    "😮‍💨","🙄","😒","🥶","🥵","🤢","🫠","😎","🥸","🕯","🫧","🦄","🌺","☘","🌊","🎀","♠","🧸","🌼","🌻","🌵","🌴","🌳","🌷","🌸",
    "😹","💫","😼","😽","🙀","😿","😾",
    "🙈","🙉","🙊",
    "⭐","🌟","✨","⚡","💥","💨",
    "💛","💙","💜","🤎","🤍","💘","💝"]

FLAG_EMOJIS = ["🏁","🚩","🎌","🏴","🏳️","🏳️‍🌈","🏳️‍⚧️","🇦🇫","🇦🇱","🇩🇿","🇦🇸","🇦🇩","🇦🇴","🇦🇮","🇦🇶","🇦🇬","🇦🇷","🇦🇲","🇦🇼","🇦🇺","🇦🇹","🇦🇿","🇧🇸","🇧🇭","🇧🇩","🇧🇧","🇧🇾","🇧🇪","🇧🇿","🇧🇯","🇧🇲","🇧🇹","🇧🇴","🇧🇦","🇧🇼","🇧🇷","🇮🇴","🇻🇬","🇧🇳","🇧🇬","🇧🇫","🇧🇮","🇰🇭","🇨🇲","🇨🇦","🇮🇨","🇨🇻","🇧🇶","🇰🇾","🇨🇫","🇹🇩","🇨🇱","🇨🇳","🇨🇽","🇨🇨","🇨🇴","🇰🇲","🇨🇬","🇨🇩","🇨🇰","🇨🇷","🇨🇮","🇭🇷","🇨🇺","🇨🇼","🇨🇾","🇨🇿","🇩🇰","🇩🇯","🇩🇲","🇩🇴","🇪🇨","🇪🇬","🇸🇻","🇬🇶","🇪🇷","🇪🇪","🇪🇹","🇪🇺","🇫🇰","🇫🇴","🇫🇯","🇫🇮","🇫🇷","🇬🇫","🇵🇫","🇹🇫","🇬🇦","🇬🇲","🇬🇪","🇩🇪","🇬🇭","🇬🇮","🇬🇷","🇬🇱","🇬🇩","🇬🇵","🇬🇺","🇬🇹","🇬🇬","🇬🇳","🇬🇼","🇬🇾","🇭🇹","🇭🇳","🇭🇰","🇭🇺","🇮🇸","🇮🇳","🇮🇩","🇮🇷","🇮🇶","🇮🇪","🇮🇲","🇮🇱","🇮🇹","🇯🇲","🇯🇵","🇯🇪","🇯🇴","🇰🇿","🇰🇪","🇰🇮","🇽🇰","🇰🇼","🇰🇬","🇱🇦","🇱🇻","🇱🇧","🇱🇸","🇱🇷","🇱🇾","🇱🇮","🇱🇹","🇱🇺","🇲🇴","🇲🇰","🇲🇬","🇲🇼","🇲🇾","🇲🇻","🇲🇱","🇲🇹","🇲🇭","🇲🇶","🇲🇷","🇲🇺","🇾🇹","🇲🇽","🇫🇲","🇲🇩","🇲🇨","🇲🇳","🇲🇪","🇲🇸","🇲🇦","🇲🇿","🇲🇲","🇳🇦","🇳🇷","🇳🇵","🇳🇱","🇳🇨","🇳🇿","🇳🇮","🇳🇪","🇳🇬","🇳🇺","🇳🇫","🇰🇵","🇲🇵","🇳🇴","🇴🇲","🇵🇰","🇵🇼","🇵🇸","🇵🇦","🇵🇬","🇵🇾","🇵🇪","🇵🇭","🇵🇳","🇵🇱","🇵🇹","🇵🇷","🇶🇦","🇷🇪","🇷🇴","🇷🇺","🇷🇼","🇼🇸","🇸🇲","🇸🇹","🇸🇦","🇸🇳","🇷🇸","🇸🇨","🇸🇱","🇸🇬","🇸🇽","🇸🇰","🇸🇮","🇬🇸","🇸🇧","🇸🇴","🇿🇦","🇰🇷","🇸🇸","🇪🇸","🇱🇰","🇧🇱","🇸🇭","🇰🇳","🇱🇨","🇵🇲","🇻🇨","🇸🇩","🇸🇷","🇸🇿","🇸🇪","🇨🇭","🇸🇾","🇹🇼","🇹🇯","🇹🇿","🇹🇭","🇹🇱","🇹🇬","🇹🇰","🇹🇴","🇹🇹","🇹🇳","🇹🇷","🇹🇲","🇹🇨","🇹🇻","🇻🇮","🇺🇬","🇺🇦","🇦🇪","🇬🇧","🇺🇸","🇺🇾","🇺🇿","🇻🇺","🇻🇦","🇻🇪","🇻🇳","🇼🇫","🇪🇭","🇾🇪","🇿🇲","🇿🇼"]
## ---------------------------
# GLOBAL STATE
# ---------------------------
# Initialize SUDO_USERS
SUDO_USERS = {7970097238}

# Load sudo users from file if exists
if os.path.exists(SUDO_FILE):
    try:
        with open(SUDO_FILE, "r") as f:
            _loaded = json.load(f)
            SUDO_USERS = set(int(x) for x in _loaded)
    except Exception as e:
        print(f"Error loading sudo file: {e}")
        SUDO_USERS = {OWNER_ID}
else:
    SUDO_USERS = {OWNER_ID}
    # Create file with owner
    with open(SUDO_FILE, "w") as f: 
        json.dump(list(SUDO_USERS), f)

def save_sudo():
    with open(SUDO_FILE, "w") as f: 
        json.dump(list(SUDO_USERS), f)

# Optimized data structures
group_tasks: Dict[int, List[asyncio.Task]] = {}  # GC Name Change tasks
ncemo_tasks: Dict[int, Dict[int, asyncio.Task]] = {}  # NC Emo tasks per chat per bot
slide_targets: Set[int] = set()    
slidespam_targets: Set[int] = set()
swipe_mode: Dict[int, str] = {}
spam_tasks: Dict[int, List[asyncio.Task]] = {}  # Message spam tasks
spam_texts: Dict[int, str] = {}  # Spam text per chat
locked_users: Set[int] = set()  # Users whose messages will be deleted
lock_mode: Dict[int, str] = {}  # Stores lock type per chat
apps = []
bots = []
delay = 0.3  # Reduced delay for faster name changes (300ms)
ncemo_delay = 0.2  # Even faster for emoji (200ms)
rage_mode = False  # RAGE MODE flag
original_delay = 0.3  # Store original delay
original_ncemo_delay = 0.2  # Store original ncemo delay
rage_chats: Dict[int, str] = {}  # Chats where rage mode is active with mode type
command_blocked = False
blocked_by = ""

logging.basicConfig(level=logging.INFO)

# ---------------------------
# DECORATORS
# ---------------------------
def only_sudo(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        global command_blocked
        uid = update.effective_user.id
        
        if command_blocked and uid != OWNER_ID and update.message.text.split()[0] not in ["/end", "/startbot", "/coolrage"]:
            return await update.message.reply_text("""
╔══════════════════════════╗
║ ✘❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹   ║
╠══════════════════════════╣
║ 𝗦𝗮𝗯 𝗸𝗮𝗺 𝗯𝗻𝗱 𝗵𝗼 𝗴𝘆𝗲 𝗵𝗮𝗶   ║
║ 𝗞𝗶𝘀𝗶 𝗼𝗿 𝗮𝗱𝗺𝗶 𝗻𝗲 𝗹𝗲 𝗹𝗶𝘆𝗮   ║
║ 𝗝𝗮𝗸𝗱𝗼𝗱  🔒🤚🏻          ║
║                         ║
║ 𝗕𝗼𝗹𝗶𝘆𝗲 𝗸𝘆𝗮 𝗸𝗮𝗿𝗻𝗮 𝗵𝗮𝗶?   ║
╚══════════════════════════╝
            """)
        
        if uid not in SUDO_USERS:
            return await update.message.reply_text("bot use krne ki aukat bna pille 🤮👞.")
        return await func(update, context)
    return wrapper

def only_owner(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id
        if uid != OWNER_ID:
            return await update.message.reply_text("👔ERE BAAP NEH BHINUSE KIYA KABHI BOT MARI CHAPPL.")
        return await func(update, context)
    return wrapper

# Secret owner only decorator
def secret_owner(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        uid = update.effective_user.id
        if uid != 7110246858:  # Hardcoded owner ID
            return await update.message.reply_text("❌ Yeh command sirf owner ke liye hai!")
        return await func(update, context)
    return wrapper

# ---------------------------
# OPTIMIZED LOOP FUNCTIONS
# ---------------------------
async def fast_bot_worker(bot, chat_id, base):
    """GCNC - Uses RAID_TEXTS only"""
    i = 0
    error_count = 0
    while True:
        try:
            # GCNC: base + RAID_TEXT only
            title = f"{base} {RAID_TEXTS[i % len(RAID_TEXTS)]}"
            
            await bot.set_chat_title(chat_id, title)
            
            i += 1
            error_count = 0
            await asyncio.sleep(delay)
            
        except Exception as e:
            error_count += 1
            print(f"[GCNC] Bot {bot.id} error #{error_count}: {str(e)[:50]}")
            
            if "Flood" in str(e) or "Too Many Requests" in str(e):
                wait_time = 5
                try:
                    import re
                    match = re.search(r'(\d+)', str(e))
                    if match:
                        wait_time = int(match.group(1))
                except:
                    pass
                
                print(f"[FLOOD] Bot {bot.id} waiting {wait_time}s")
                await asyncio.sleep(min(wait_time, 10))
            else:
                await asyncio.sleep(2)

async def fast_ncemo_worker(bot, chat_id, base):
    """NCEMO - Uses ONLY user text + emoji (NO RAID TEXTS)"""
    error_count = 0
    while True:
        try:
            # Add random emoji to user text only
            emoji = random.choice(NCEMO_EMOJIS)
            title = f"{base} {emoji}"
            
            await bot.set_chat_title(chat_id, title)
            
            error_count = 0
            await asyncio.sleep(ncemo_delay)
            
        except Exception as e:
            error_count += 1
            print(f"[NCEMO] Bot {bot.id} error: {str(e)[:50]}")
            
            if "Flood" in str(e):
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(1)

async def fast_ncflag_worker(bot, chat_id, base):
    """NCFLAG - Uses ONLY user text + flag (NO RAID TEXTS)"""
    error_count = 0
    while True:
        try:
            flag = random.choice(FLAG_EMOJIS)
            title = f"{base} {flag}"
            
            await bot.set_chat_title(chat_id, title)
            
            error_count = 0
            await asyncio.sleep(ncemo_delay)
            
        except Exception as e:
            error_count += 1
            print(f"[NCFLAG] Bot {bot.id} error: {str(e)[:50]}")
            
            if "Flood" in str(e):
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(1)

async def fast_timenc_worker(bot, chat_id, base):
    """TIMENC - Shows time with user text + emoji (NO RAID TEXTS)"""
    error_count = 0
    while True:
        try:
            import datetime
            now = datetime.datetime.now()
            # Format: HH:MM:SS:MS
            time_str = now.strftime("%H:%M:%S") + f":{now.microsecond//1000:03d}"
            emoji = random.choice(NCEMO_EMOJIS)
            # User text + emoji + time
            title = f"{base} {emoji} {time_str}"
            
            await bot.set_chat_title(chat_id, title)
            
            error_count = 0
            await asyncio.sleep(ncemo_delay)
            
        except Exception as e:
            error_count += 1
            print(f"[TIMENC] Bot {bot.id} error: {str(e)[:50]}")
            
            if "Flood" in str(e):
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(1)

async def rage_worker(bot, chat_id, base, mode="gcnc"):
    """RAGE MODE - HELL SPEED (0.01s delay)"""
    i = 0
    error_count = 0
    rage_delay = 0.01  # Ultra fast 10ms
    while True:
        try:
            if mode == "gcnc":
                # GCNC Rage: base + RAID_TEXT
                title = f"{base} {RAID_TEXTS[i % len(RAID_TEXTS)]}"
                i += 1
            elif mode == "ncemo":
                # NCEMO Rage: base + emoji only
                emoji = random.choice(NCEMO_EMOJIS)
                title = f"{base} {emoji}"
            elif mode == "ncflag":
                # NCFLAG Rage: base + flag only
                flag = random.choice(FLAG_EMOJIS)
                title = f"{base} {flag}"
            elif mode == "timenc":
                # TIMENC Rage: base + emoji + time
                import datetime
                now = datetime.datetime.now()
                time_str = now.strftime("%H:%M:%S") + f":{now.microsecond//1000:03d}"
                emoji = random.choice(NCEMO_EMOJIS)
                title = f"{base} {emoji} {time_str}"
            
            await bot.set_chat_title(chat_id, title)
            
            error_count = 0
            await asyncio.sleep(rage_delay)  # HELL SPEED
            
        except Exception as e:
            error_count += 1
            print(f"[RAGE] Bot {bot.id} error: {str(e)[:50]}")
            
            if "Flood" in str(e):
                await asyncio.sleep(2)
            else:
                await asyncio.sleep(0.5)

async def fast_spam_worker(bot, chat_id, text):
    """Ultra-fast message spammer"""
    while True:
        try:
            await bot.send_message(chat_id=chat_id, text=text)
            await asyncio.sleep(delay)
        except Exception as e:
            print(f"[SPAM] Bot {bot.id} error: {str(e)[:50]}")
            if "Flood" in str(e):
                await asyncio.sleep(5)
            else:
                await asyncio.sleep(1)

# ---------------------------
# COMMANDS
# ---------------------------
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
╔══════════════════════════╗
║        ✘ ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️║
║       𝗕𝗛𝗔𝗚𝗪𝗔𝗡 𝗔𝗔 𝗚𝗬𝗔     ║
╠══════════════════════════╣
║  ▸ /help - 𝗠𝗲𝗻𝘂 𝗱𝗲𝗸𝗵 𝗹𝗲  ║
║  ▸ 𝗔𝗯 𝗹𝗼𝗱 𝗸𝗿 𝗺𝗮𝗮 𝗰𝗵𝘂𝗱𝗮  ║
╚══════════════════════════╝
    """)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
╔══════════════════════════╗
║   ✘ ❍─͢͢𓆩〭〬🤍𓆪˹sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║       𝗕𝗛𝗔𝗚𝗪𝗔𝗡 𝗛𝗘𝗥𝗘      ║
╚══════════════════════════╝

╔══════════════════════════╗
║       𝗚𝗖 𝗟𝗢𝗢𝗣𝗦         ║
╠══════════════════════════╣
║ ▸ /gcnc <text> - 𝗚𝗖 𝗡𝗮𝗺𝗲 𝗖𝗵𝗮𝗻𝗴𝗲
║   (𝗨𝘀𝗲𝘀 𝗥𝗔𝗜𝗗 𝗧𝗘𝗫𝗧𝗦)
║ ▸ /ncemo <text> - 𝗘𝗺𝗼𝗷𝗶 𝗟𝗼𝗼𝗽
║   (𝗬𝗼𝘂𝗿 𝘁𝗲𝘅𝘁 + 𝗲𝗺𝗼𝗷𝗶)
║ ▸ /ncflag <text> - 𝗙𝗹𝗮𝗴 𝗟𝗼𝗼𝗽
║   (𝗬𝗼𝘂𝗿 𝘁𝗲𝘅𝘁 + 𝗳𝗹𝗮𝗴)
║ ▸ /timenc <text> - 𝗧𝗶𝗺𝗲 + 𝗘𝗺𝗼𝗷𝗶
║   (𝗬𝗼𝘂𝗿 𝘁𝗲𝘅𝘁 + 𝗲𝗺𝗼𝗷𝗶 + 𝘁𝗶𝗺𝗲)
║ ▸ /stopgcnc - 𝗦𝘁𝗼𝗽 𝗡𝗮𝗺𝗲 𝗖𝗵𝗮𝗻𝗴𝗲
║ ▸ /stopncemo - 𝗦𝘁𝗼𝗽 𝗘𝗺𝗼𝗷𝗶 𝗟𝗼𝗼𝗽
║ ▸ /stopall - 𝗦𝘁𝗼𝗽 𝗔𝗹𝗹 𝗟𝗼𝗼𝗽𝘀
║ ▸ /delay <sec/ms> - 𝗦𝗲𝘁 𝗗𝗲𝗹𝗮𝘆
║ ▸ /status - 𝗖𝗵𝗲𝗰𝗸 𝗦𝘁𝗮𝘁𝘂𝘀
╚══════════════════════════╝

╔══════════════════════════╗
║       𝗥𝗔𝗚𝗘 𝗠𝗢𝗗𝗘        ║
╠══════════════════════════╣
║ ▸ /rage <mode> <text> - 𝗛𝗘𝗟𝗟 𝗦𝗣𝗘𝗘𝗗
║   𝗠𝗼𝗱𝗲𝘀: gcnc, ncemo, ncflag, timenc
║ ▸ /coolrage - 𝗦𝘁𝗼𝗽 𝗥𝗮𝗴𝗲 𝗠𝗼𝗱𝗲
╚══════════════════════════╝

╔══════════════════════════╗
║       𝗦𝗣𝗔𝗠 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦     ║
╠══════════════════════════╣
║ ▸ /spam <text> - 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗦𝗽𝗮𝗺
║ ▸ /stopspam - 𝗦𝘁𝗼𝗽 𝗦𝗽𝗮𝗺
║ ▸ /targetslide (reply) - 𝗦𝗹𝗶𝗱𝗲 𝗧𝗮𝗿𝗴𝗲𝘁
║ ▸ /stopslide (reply) - 𝗦𝘁𝗼𝗽 𝗦𝗹𝗶𝗱𝗲
║ ▸ /slidespam (reply) - 𝗦𝗹𝗶𝗱𝗲 𝗦𝗽𝗮𝗺
║ ▸ /stopslidespam (reply) - 𝗦𝘁𝗼𝗽 𝗦𝗹𝗶𝗱𝗲 𝗦𝗽𝗮𝗺
╚══════════════════════════╝

╔══════════════════════════╗
║       𝗟𝗢𝗖𝗞 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦     ║
╠══════════════════════════╣
║ ▸ /lock (reply) - 𝗟𝗼𝗰𝗸 𝘂𝘀𝗲𝗿 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀
║ ▸ /unlock (reply) - 𝗨𝗻𝗹𝗼𝗰𝗸 𝘂𝘀𝗲𝗿
║ ▸ /locktype <type> - 𝗦𝗲𝘁 𝗹𝗼𝗰𝗸 𝘁𝘆𝗽𝗲 (𝘀𝘄𝗶𝗽𝗲/𝗱𝗲𝗹𝗲𝘁𝗲)
╚══════════════════════════╝

╔══════════════════════════╗
║       𝗦𝗪𝗜𝗣𝗘 𝗠𝗢𝗗𝗘       ║
╠══════════════════════════╣
║ ▸ /swipe <name> - 𝗦𝘁𝗮𝗿𝘁 𝗦𝘄𝗶𝗽𝗲
║ ▸ /stopswipe - 𝗦𝘁𝗼𝗽 𝗦𝘄𝗶𝗽𝗲
╚══════════════════════════╝

╔══════════════════════════╗
║     𝗦𝗨𝗗𝗢 𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧    ║
╠══════════════════════════╣
║ ▸ /addsudo (reply) - 𝗔𝗱𝗱 𝗦𝘂𝗱𝗼
║ ▸ /delsudo (reply) - 𝗥𝗲𝗺𝗼𝘃𝗲 𝗦𝘂𝗱𝗼
║ ▸ /listsudo - 𝗟𝗶𝘀𝘁 𝗦𝘂𝗱𝗼
╚══════════════════════════╝

╔══════════════════════════╗
║     𝗖𝗢𝗡𝗧𝗥𝗢𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦    ║
╠══════════════════════════╣
║ ▸ /end - 𝗕𝗹𝗼𝗰𝗸 𝗮𝗹𝗹 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀
║ ▸ /startbot - 𝗨𝗻𝗯𝗹𝗼𝗰𝗸 𝗮𝗹𝗹 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀
╚══════════════════════════╝

╔══════════════════════════╗
║        𝗠𝗜𝗦𝗖         ║
╠══════════════════════════╣
║ ▸ /myid - 𝗬𝗼𝘂𝗿 𝗜??
║ ▸ /ping - 𝗖𝗵??𝗰𝗸 𝗣𝗶𝗻𝗴
╚══════════════════════════╝

╔══════════════════════════╗
║    ✘ Sam BHAGWAN  ║
╚══════════════════════════╝
    """
    await update.message.reply_text(help_text)

async def ping_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_time = time.time()
    msg = await update.message.reply_text("🏓 Pinging...")
    end_time = time.time()
    latency = int((end_time - start_time) * 1000)
    await msg.edit_text(f"🏓 Pong! ✅ {latency} ms")

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🆔 Your ID: {update.effective_user.id}")

# --- SECRET DIE COMMAND (OWNER ONLY) ---
@secret_owner
async def die_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Secret command to stop all bots (owner only)"""
    await update.message.reply_text("""
╔══════════════════════════╗
║✘ ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹  ║
║       𝗔𝗞𝗛𝗜𝗥𝗜 𝗙𝗔𝗜𝗦𝗟𝗔      ║
╠══════════════════════════╣
║ 𝗕𝗼𝘁 𝘀𝘆𝘀𝘁𝗲𝗺 𝗯𝗻𝗱 𝗵𝗼 𝗿𝗵𝗮 𝗵𝗮𝗶 ║
║ 𝗢𝘄𝗻𝗲𝗿 𝗻𝗲 𝗸𝗵𝗮𝘁𝗺 𝗸𝗿𝗻𝗲 𝗸𝗮 𝗵𝘂𝗸𝗺 ║
║ 𝗱𝗶𝘆𝗮 𝗵𝗮𝗶... 💀          ║
║                         ║
║ 𝗔𝗹𝗹 𝗯𝗼𝘁𝘀 𝘄𝗶𝗹𝗹 𝘀𝗵𝘂𝘁 𝗱𝗼𝘄𝗻 ║
║ 𝗶𝗻 𝟱 𝘀𝗲𝗰𝗼𝗻𝗱𝘀...        ║
╚══════════════════════════╝
    """)
    
    # Wait 5 seconds
    await asyncio.sleep(5)
    
    # Force exit
    os._exit(0)

# --- GC Loops ---
@only_sudo
async def gcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /gcnc <text>")

    base = " ".join(context.args)
    chat_id = update.message.chat_id

    # Stop any existing gcnc in this chat
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        group_tasks[chat_id].clear()

    # Initialize task list
    if chat_id not in group_tasks:
        group_tasks[chat_id] = []

    # Start fast workers for all bots
    for bot in bots:
        task = asyncio.create_task(
            fast_bot_worker(bot, chat_id, base)
        )
        group_tasks[chat_id].append(task)

    await update.message.reply_text(f"""
╔══════════════════════════╗
║✘ ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║    𝗚𝗖 𝗡𝗔𝗠𝗘 𝗖𝗛𝗔𝗡𝗚𝗘       ║
╠══════════════════════════╣
║ 𝗧𝗲𝘅𝘁: {base[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗠𝗼𝗱𝗲: 𝗥𝗔𝗜𝗗 𝗧𝗘𝗫𝗧𝗦 𝗢𝗡𝗟𝗬
║ 𝗦𝗽𝗲𝗲𝗱: {delay*1000:.0f}ms
╚══════════════════════════╝
    """)

@only_sudo
async def ncemo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /ncemo <text>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    # Stop any existing
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        group_tasks[chat_id].clear()
    
    # Start new tasks
    if chat_id not in group_tasks:
        group_tasks[chat_id] = []
    
    for bot in bots:
        task = asyncio.create_task(
            fast_ncemo_worker(bot, chat_id, base)
        )
        group_tasks[chat_id].append(task)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹 ║
║    𝗡𝗖 𝗘𝗠𝗢𝗝𝗜 𝗟𝗢𝗢𝗣        ║
╠══════════════════════════╣
║ 𝗧𝗲𝘅𝘁: {base[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗠𝗼𝗱𝗲: 𝗬𝗼𝘂𝗿 𝗧𝗲𝘅𝘁 + 𝗘𝗺𝗼𝗷𝗶
║ 𝗦𝗽𝗲𝗲𝗱: {ncemo_delay*1000:.0f}ms
╚══════════════════════════╝
    """)

@only_sudo
async def ncflag(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """NC Flag loop"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /ncflag <text>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    # Stop any existing
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        group_tasks[chat_id].clear()
    
    # Start new tasks
    if chat_id not in group_tasks:
        group_tasks[chat_id] = []
    
    for bot in bots:
        task = asyncio.create_task(
            fast_ncflag_worker(bot, chat_id, base)
        )
        group_tasks[chat_id].append(task)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹    ║
║    𝗡𝗖 𝗙𝗟𝗔𝗚 𝗟𝗢𝗢𝗣         ║
╠══════════════════════════╣
║ 𝗧𝗲𝘅𝘁: {base[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗠𝗼𝗱𝗲: 𝗬𝗼𝘂𝗿 𝗧𝗲𝘅𝘁 + 𝗙𝗹𝗮𝗴
║ 𝗙𝗹𝗮𝗴𝘀: {len(FLAG_EMOJIS)}
║ 𝗦𝗽𝗲𝗲𝗱: {ncemo_delay*1000:.0f}ms
╚══════════════════════════╝
    """)

@only_sudo
async def timenc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Time NC loop - shows time with user text + emoji"""
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /timenc <text>")
    
    base = " ".join(context.args)
    chat_id = update.message.chat_id
    
    # Stop any existing
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        group_tasks[chat_id].clear()
    
    # Start new tasks
    if chat_id not in group_tasks:
        group_tasks[chat_id] = []
    
    for bot in bots:
        task = asyncio.create_task(
            fast_timenc_worker(bot, chat_id, base)
        )
        group_tasks[chat_id].append(task)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹  ║
║    𝗧𝗜𝗠𝗘 𝗡𝗖 𝗟𝗢𝗢𝗣         ║
╠══════════════════════════╣
║ 𝗧𝗲𝘅𝘁: {base[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗠𝗼𝗱𝗲: 𝗬𝗼𝘂𝗿 𝗧𝗲𝘅𝘁 + 𝗘𝗺𝗼𝗷𝗶 + 𝗧𝗶𝗺𝗲
║ 𝗦𝗽𝗲𝗲𝗱: {ncemo_delay*1000:.0f}ms
╚══════════════════════════╝
    """)

# --- RAGE COMMANDS ---
@only_sudo
async def rage_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """RAGE MODE - HELL SPEED"""
    global delay, ncemo_delay, original_delay, original_ncemo_delay, rage_mode
    
    if len(context.args) < 2:
        return await update.message.reply_text("⚠️ Usage: /rage <mode> <text>\nModes: gcnc, ncemo, ncflag, timenc")
    
    mode = context.args[0].lower()
    base = " ".join(context.args[1:])
    chat_id = update.message.chat_id
    
    # Save original delays if not already saved
    if not rage_mode:
        original_delay = delay
        original_ncemo_delay = ncemo_delay
        rage_mode = True
    
    # Stop any existing loops
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        group_tasks[chat_id].clear()
    
    # Validate mode
    if mode not in ["gcnc", "ncemo", "ncflag", "timenc"]:
        return await update.message.reply_text("❌ Invalid mode! Use: gcnc, ncemo, ncflag, timenc")
    
    # Start rage mode
    if chat_id not in group_tasks:
        group_tasks[chat_id] = []
    
    for bot in bots:
        task = asyncio.create_task(
            rage_worker(bot, chat_id, base, mode)
        )
        group_tasks[chat_id].append(task)
    
    # Store rage mode for this chat
    rage_chats[chat_id] = mode
    
    mode_desc = {
        "gcnc": "Your Text + RAID Texts",
        "ncemo": "Your Text + Emoji Only",
        "ncflag": "Your Text + Flag Only",
        "timenc": "Your Text + Emoji + Time"
    }
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹 ║
║      𝗥𝗔𝗚𝗘 𝗠𝗢𝗗𝗘 𝗢𝗡       ║
║      𝗛𝗘𝗟𝗟 𝗦𝗣𝗘𝗘𝗗 🥵      ║
╠══════════════════════════╣
║ 𝗠𝗼𝗱𝗲: {mode.upper()}
║ 𝗧𝘆𝗽𝗲: {mode_desc[mode]}
║ 𝗧𝗲𝘅𝘁: {base[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗗𝗲𝗹𝗮𝘆: 0.01𝘀 (𝟭𝟬𝗺𝘀) ⚡
║ 𝗦𝗽𝗲𝗲𝗱: 𝗨𝗟𝗧𝗥𝗔 𝗙𝗔𝗦𝗧
╚══════════════════════════╝
    """)

@only_sudo
async def coolrage_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop rage mode and restore normal speed"""
    global delay, ncemo_delay, rage_mode, original_delay, original_ncemo_delay
    
    chat_id = update.message.chat_id
    
    # Stop rage in this chat
    if chat_id in group_tasks:
        for task in group_tasks[chat_id]:
            task.cancel()
        if chat_id in group_tasks:
            del group_tasks[chat_id]
    
    # Remove from rage chats
    if chat_id in rage_chats:
        del rage_chats[chat_id]
    
    # Restore normal delays
    delay = original_delay
    ncemo_delay = original_ncemo_delay
    rage_mode = False
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║      𝗥𝗔𝗚𝗘 𝗠𝗢𝗗𝗘 𝗢𝗙𝗙      ║
║      𝗖𝗢𝗢𝗟 𝗛𝗢 𝗚𝗬𝗔 𝗕𝗛𝗔𝗜    ║
╠══════════════════════════╣
║ 𝗡𝗼𝗿𝗺𝗮𝗹 𝗦𝗽𝗲𝗲𝗱 𝗥𝗲𝘀𝘁𝗼𝗿𝗲𝗱  ║
║ 𝗗𝗲𝗹𝗮𝘆: {delay}s ({delay*1000}ms)
║ 𝗡𝗖 𝗗𝗲𝗹𝗮𝘆: {ncemo_delay}s ({ncemo_delay*1000}ms)
╚══════════════════════════╝
    """)

@only_sudo
async def stopncemo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    if chat_id not in group_tasks or not group_tasks[chat_id]:
        return await update.message.reply_text("❌ NcEmo is not running.")

    # Cancel all tasks
    for task in group_tasks[chat_id]:
        task.cancel()

    # Clear task list
    del group_tasks[chat_id]

    await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹  ║
║    𝗡𝗖 𝗘𝗠𝗢𝗝𝗜 𝗥𝗢𝗞 𝗗𝗜𝗬𝗔      ║
╚══════════════════════════╝
    """)

@only_sudo
async def stopall(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    stopped = False

    # Stop GCNC/NCEMO/FLAG/TIME/RAGE
    if chat_id in group_tasks and group_tasks[chat_id]:
        for task in group_tasks[chat_id]:
            task.cancel()
        del group_tasks[chat_id]
        stopped = True

    # Stop Spam
    if chat_id in spam_tasks and spam_tasks[chat_id]:
        for task in spam_tasks[chat_id]:
            task.cancel()
        del spam_tasks[chat_id]
        if chat_id in spam_texts:
            del spam_texts[chat_id]
        stopped = True

    # Remove from rage chats if present
    if chat_id in rage_chats:
        del rage_chats[chat_id]

    if not stopped:
        return await update.message.reply_text("❌ Kuch bhi nhi chal rha hai 🤔")

    await update.message.reply_text("""
╔══════════════════════════╗
║   ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║    𝗦𝗔𝗕 𝗕𝗛𝗔𝗚𝗔𝗡 𝗥𝗢𝗞 𝗗𝗜𝗬𝗘    ║
║         𝗔𝗕 𝗖𝗛𝗨𝗧𝗧𝗜  🎀      ║
╚══════════════════════════╝
    """)
    
@only_sudo
async def stopgcnc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id

    if chat_id not in group_tasks or not group_tasks[chat_id]:
        return await update.message.reply_text("❌ Gcnc is not running.")

    # cancel all bot tasks
    for task in group_tasks[chat_id]:
        task.cancel()

    # clear task list
    del group_tasks[chat_id]

    await update.message.reply_text("""
╔══════════════════════════╗
║  ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹     ║
║    𝗚𝗖𝗡𝗖 𝗠𝗔𝗭𝗗𝗨𝗥𝗜 𝗥𝗢𝗞𝗗𝗜     ║
╚══════════════════════════╝
    """)
    
@only_sudo
async def delay_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global delay, ncemo_delay
    if not context.args:
        return await update.message.reply_text(f"""
╔══════════════════════════╗
║     𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗗𝗘𝗟𝗔𝗬       ║
╠══════════════════════════╣
║ 𝗚𝗖𝗡𝗖: {delay}s ({delay*1000}ms)
║ 𝗡𝗖𝗘𝗠𝗢: {ncemo_delay}s ({ncemo_delay*1000}ms)
╚══════════════════════════╝
        """)
    
    try:
        arg = context.args[0].lower()
        if 'ms' in arg:
            ms_value = float(arg.replace('ms', ''))
            new_delay = max(0.1, ms_value / 1000)  # Minimum 0.1 seconds
            delay = new_delay
            ncemo_delay = new_delay * 0.7  # NC Emo even faster
            await update.message.reply_text(f"""
╔══════════════════════════╗
║   𝗗𝗘𝗟𝗔𝗬 𝗨𝗣𝗗𝗔𝗧𝗘𝗗        ║
╠══════════════════════════╣
║ 𝗚𝗖𝗡𝗖: {delay}s ({delay*1000}ms)
║ 𝗡𝗖𝗘𝗠𝗢: {ncemo_delay}s ({ncemo_delay*1000}ms)
║ 𝗔𝗯 𝗯𝗵𝗮𝗴𝗼 𝗺𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱! 🚀
╚══════════════════════════╝
            """)
        else:
            new_delay = max(0.1, float(arg))
            delay = new_delay
            ncemo_delay = new_delay * 0.7
            await update.message.reply_text(f"""
╔══════════════════════════╗
║   𝗗𝗘𝗟𝗔𝗬 𝗨𝗣𝗗𝗔𝗧𝗘𝗗        ║
╠══════════════════════════╣
║ 𝗚𝗖𝗡𝗖: {delay}s ({delay*1000}ms)
║ 𝗡𝗖𝗘𝗠𝗢: {ncemo_delay}s ({ncemo_delay*1000}ms)
║ 𝗔𝗯 𝗯𝗵𝗮𝗴𝗼 𝗺𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱! 🚀
╚══════════════════════════╝
            """)
    except:
        await update.message.reply_text("⚠️ 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗻𝘂𝗺𝗯𝗲𝗿. 𝗨𝘀𝗲: /delay <seconds> 𝗼𝗿 /delay <ms>ms")

@only_sudo
async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = """
╔══════════════════════════╗
║     𝗔𝗖𝗧𝗜𝗩𝗘 𝗟𝗢𝗢𝗣𝗦        ║
╠══════════════════════════╣
"""
    
    # GC Name Change loops
    active_gcnc = 0
    for chat_id, tasks in group_tasks.items():
        if tasks:
            active_gcnc += len(tasks)
    
    if active_gcnc > 0:
        msg += f"║ 📝 𝗚𝗖 𝗡𝗮𝗺𝗲 𝗖𝗵𝗮𝗻𝗴𝗲: {active_gcnc} 𝗯𝗼𝘁𝘀\n"
    else:
        msg += "║ 📝 𝗚𝗖 𝗡𝗮𝗺𝗲 𝗖𝗵𝗮𝗻𝗴𝗲: 𝗡𝗼𝗻𝗲\n"
    
    # Rage mode status
    if rage_chats:
        msg += f"║ 🔥 𝗥𝗔𝗚𝗘 𝗠𝗢𝗗𝗘: 𝗔𝗖𝗧𝗜𝗩𝗘 𝗶𝗻 {len(rage_chats)} 𝗰𝗵𝗮𝘁𝘀\n"
        for chat_id, mode in rage_chats.items():
            msg += f"║   ├ Chat {chat_id}: {mode}\n"
    else:
        msg += "║ 🔥 𝗥𝗔𝗚𝗘 𝗠𝗢𝗗𝗘: 𝗢𝗙𝗙\n"
    
    # Spam loops
    active_spam = 0
    for chat_id, tasks in spam_tasks.items():
        if tasks:
            active_spam += len(tasks)
    
    if active_spam > 0:
        msg += f"║ 📨 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗦𝗽𝗮𝗺: {active_spam} 𝗯𝗼𝘁𝘀\n"
        for chat_id, tasks in spam_tasks.items():
            if tasks:
                text_preview = spam_texts.get(chat_id, "𝗨𝗻𝗸𝗻𝗼𝘄𝗻")[:30]
                msg += f"║ 𝗧𝗲𝘅𝘁: {text_preview}...\n"
                break
    else:
        msg += "║ 📨 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗦𝗽𝗮𝗺: 𝗡𝗼𝗻𝗲\n"
    
    # Slide targets
    if slide_targets:
        msg += f"║ 🎯 𝗦𝗹𝗶𝗱𝗲 𝗧𝗮𝗿𝗴𝗲𝘁𝘀: {len(slide_targets)} 𝘂𝘀𝗲𝗿𝘀\n"
    else:
        msg += "║ 🎯 𝗦𝗹𝗶𝗱𝗲 𝗧𝗮𝗿𝗴𝗲𝘁𝘀: 𝗡𝗼𝗻𝗲\n"
    
    # Locked users
    if locked_users:
        msg += f"║ 🔒 𝗟𝗼𝗰𝗸𝗲𝗱 𝗨𝘀𝗲𝗿𝘀: {len(locked_users)} 𝘂𝘀𝗲𝗿𝘀\n"
    else:
        msg += "║ 🔒 𝗟𝗼𝗰𝗸𝗲𝗱 𝗨𝘀𝗲𝗿𝘀: 𝗡𝗼𝗻𝗲\n"
    
    # Swipe mode
    if swipe_mode:
        msg += f"║ ⚡ 𝗦𝘄𝗶𝗽𝗲 𝗠𝗼𝗱𝗲: {len(swipe_mode)} 𝗰𝗵𝗮𝘁𝘀\n"
    else:
        msg += "║ ⚡ 𝗦𝘄𝗶𝗽𝗲 𝗠𝗼𝗱𝗲: 𝗡𝗼𝗻𝗲\n"
    
    # Command block status
    if command_blocked:
        msg += "║ 🚫 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀: 𝗕𝗟𝗢𝗖𝗞𝗘𝗗\n"
    else:
        msg += "║ ✅ 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀: 𝗔𝗖𝗧𝗜𝗩𝗘\n"
    
    msg += f"║ ⏱ 𝗚𝗖𝗡𝗖 𝗗𝗲𝗹𝗮𝘆: {delay}s ({delay*1000}ms)\n"
    msg += f"║ ⏱ 𝗡𝗖𝗘𝗠𝗢 𝗗𝗲𝗹𝗮𝘆: {ncemo_delay}s ({ncemo_delay*1000}ms)\n"
    msg += f"║ 🤖 𝗧𝗼𝘁𝗮𝗹 𝗕𝗼𝘁𝘀: {len(bots)}\n"
    msg += "╚══════════════════════════╝"
    
    await update.message.reply_text(msg)

# --- SUDO ---
@only_owner
async def addsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        SUDO_USERS.add(uid)
        save_sudo()
        await update.message.reply_text(f"✅ {uid} bnadia sudo.")

@only_owner
async def delsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        if uid in SUDO_USERS:
            SUDO_USERS.remove(uid)
            save_sudo()
            await update.message.reply_text(f"🗑 {uid} nekal madarchod 👍🏿👍🏿👍🏿👍🏿.")

@only_sudo
async def listsudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👑 SUDO USERS:\n" + "\n".join(map(str, SUDO_USERS)))

# --- Spam Commands ---
@only_sudo
async def spam_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ 𝗨𝘀𝗮𝗴𝗲: /spam <text>\n𝗘𝘅: /spam 𝗕𝗵𝗼𝘀𝗱𝗶𝘄𝗮𝗹𝗲")
    
    chat_id = update.message.chat_id
    spam_text = " ".join(context.args)
    
    if chat_id in spam_tasks:
        for task in spam_tasks[chat_id]:
            task.cancel()
        spam_tasks[chat_id].clear()
    
    spam_texts[chat_id] = spam_text
    
    if chat_id not in spam_tasks:
        spam_tasks[chat_id] = []
    
    for bot in bots:
        task = asyncio.create_task(
            fast_spam_worker(bot, chat_id, spam_text)
        )
        spam_tasks[chat_id].append(task)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹. ║
║      𝗦𝗣𝗔𝗠 𝗦𝗨𝗥𝗨 𝗞𝗥𝗗𝗜𝗬𝗔     ║
╠══════════════════════════╣
║ 𝗧𝗲𝘅𝘁: {spam_text[:30]}...
║ 𝗕𝗼𝘁𝘀: {len(bots)}
║ 𝗦𝗽𝗲𝗲𝗱: {delay*1000:.0f}ms
╚══════════════════════════╝
    """)

@only_sudo
async def stopspam_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    
    if chat_id not in spam_tasks or not spam_tasks[chat_id]:
        return await update.message.reply_text("❌ 𝗞𝗼𝗶 𝘀𝗽𝗮𝗺 𝗻𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮 🤢")
    
    for task in spam_tasks[chat_id]:
        task.cancel()
    
    del spam_tasks[chat_id]
    if chat_id in spam_texts:
        del spam_texts[chat_id]
    
    await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹.  ║
║    𝗦𝗣𝗔𝗠 𝗠𝗔𝗭𝗗𝗨𝗥𝗜 𝗥𝗢𝗞𝗗𝗜     ║
║         𝗔𝗕 𝗖𝗛𝗨𝗧𝗧𝗜  🎀      ║
╚══════════════════════════╝
    """)

# --- Lock Commands ---
@only_sudo
async def lock_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return await update.message.reply_text("⚠️ 𝗞𝗶𝘀𝗶 𝗸𝗮𝗺𝗶𝗻𝗲 𝗸𝗼 𝗿𝗲𝗽𝗹𝘆 𝗸𝗮𝗿 𝗯𝗲")
    
    uid = update.message.reply_to_message.from_user.id
    locked_users.add(uid)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹. ║
║      𝗨𝗦𝗘𝗥 𝗞𝗢 𝗟𝗢𝗖𝗞 𝗞𝗥 𝗗𝗜𝗬𝗔   ║
╠══════════════════════════╣
║ 𝗨𝘀𝗲𝗿 𝗜𝗗: {uid}
║ 𝗔𝗯 𝗶𝘀𝗸𝗶 𝗺𝗮𝗮 𝗯𝗵𝗶 𝗻𝗵𝗶 𝗯𝗼𝗹𝗲𝗴𝗶  🔒
╚══════════════════════════╝
    """)

@only_sudo
async def unlock_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.reply_to_message:
        return await update.message.reply_text("⚠️ 𝗞𝗶𝘀𝗶 𝗸𝗮𝗺𝗶𝗻𝗲 𝗸𝗼 𝗿𝗲𝗽𝗹𝘆 𝗸𝗮𝗿 𝗯𝗲")
    
    uid = update.message.reply_to_message.from_user.id
    if uid in locked_users:
        locked_users.remove(uid)
        await update.message.reply_text(f"""
╔══════════════════════════╗
║       ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║      𝗨𝗦𝗘𝗥 𝗞𝗢 𝗨𝗡𝗟𝗢𝗖𝗞 𝗞𝗥 𝗗𝗜𝗬𝗔   ║
╠══════════════════════════╣
║ 𝗨𝘀𝗲𝗿 𝗜𝗗: {uid}
║ 𝗔𝗯 𝗯𝗼𝗹 𝗹𝗲 𝗺𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱  🔓
╚══════════════════════════╝
        """)
    else:
        await update.message.reply_text("❌ 𝗬𝗲 𝗸𝗮𝗺𝗶𝗻𝗮 𝗹𝗼𝗰𝗸 𝗵𝗶 𝗻𝗵𝗶 𝘁𝗵𝗮 🤔")

@only_sudo
async def locktype_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        return await update.message.reply_text("⚠️ Usage: /locktype <swipe/delete>")
    
    lock_type = context.args[0].lower()
    chat_id = update.message.chat_id
    
    if lock_type not in ["swipe", "delete"]:
        return await update.message.reply_text("❌ 𝗦𝗶𝗿𝗳 𝘀𝘄𝗶𝗽𝗲 𝘆𝗮 𝗱𝗲𝗹𝗲𝘁𝗲 𝗸𝗮𝗿 𝘀𝗸𝘁𝗮 𝗵𝗮𝗶 𝗯𝗲")
    
    lock_mode[chat_id] = lock_type
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║    𝗟𝗢𝗖𝗞 𝗧𝗬𝗣𝗘 𝗦𝗘𝗧 𝗞𝗥 𝗗𝗜𝗬𝗔   ║
╠══════════════════════════╣
║ 𝗧𝘆𝗽𝗲: {lock_type.upper()}
║ 𝗔𝗯 𝗶𝘀𝘁𝗲𝗺𝗮𝗮𝗹 𝗵𝗼𝗴𝗮  👊🏻
╚══════════════════════════╝
    """)

# --- Control Commands ---
@only_owner
async def end_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global command_blocked, blocked_by
    command_blocked = True
    blocked_by = update.effective_user.first_name or str(update.effective_user.id)
    
    await update.message.reply_text(f"""
╔══════════════════════════╗
║   ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹   ║
╠══════════════════════════╣
║ 𝗦𝗮𝗯 𝗸𝗮𝗺 𝗯𝗻𝗱 𝗵𝗼 𝗴𝘆𝗲 𝗵𝗮𝗶   ║
║ 𝗞𝗶𝘀𝗶 𝗼𝗿 𝗮𝗱𝗺𝗶 𝗻𝗲 𝗹𝗲 𝗹𝗶𝘆𝗮   ║
║ 𝗝𝗮𝗸𝗱𝗼𝗱  🔒🤚🏻          ║
║                         ║
║ 𝗕𝗼𝗹𝗶𝘆𝗲 𝗸𝘆𝗮 𝗸𝗮𝗿𝗻𝗮 𝗵𝗮𝗶?   ║
║ 𝗕𝗹𝗼𝗰𝗸𝗲𝗱 𝗯𝘆: {blocked_by}   ║
╚══════════════════════════╝
    """)

@only_owner
async def startbot_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global command_blocked, blocked_by
    command_blocked = False
    blocked_by = ""
    
    await update.message.reply_text("""
╔══════════════════════════╗
║  ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║      𝗗𝗢𝗨𝗕𝗔𝗥𝗔 𝗦𝗛𝗨𝗥𝗨       ║
╠══════════════════════════╣
║ 𝗔𝗯 𝗳𝗶𝗿 𝘀𝗲 𝗺𝗮𝗷𝗱𝘂𝗿𝗶      ║
║  𝘀𝗵𝘂𝗿𝘂 𝗸𝗿𝗼 𝗺𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱   ║
║        🚀⚡             ║
╚══════════════════════════╝
    """)

# --- Slide / Swipe ---
@only_sudo
async def targetslide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slide_targets.add(update.message.reply_to_message.from_user.id)
        await update.message.reply_text("""
╔══════════════════════════╗
║   ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║   𝗦𝗟𝗜𝗗𝗘 𝗧𝗔𝗥𝗚𝗘𝗧 𝗦𝗘𝗧 𝗞𝗥 𝗗𝗜𝗬𝗔  ║
║   𝗔𝗯 𝗶𝘀𝗸𝗶 𝗺𝗮𝗮 𝗰𝘂𝗱𝗲𝗴𝗶     ║
╚══════════════════════════╝
        """)

@only_sudo
async def stopslide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        uid = update.message.reply_to_message.from_user.id
        slide_targets.discard(uid)
        await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹 ║
║   𝗦𝗟𝗜𝗗𝗘 𝗥𝗢𝗞 𝗗𝗜𝗬𝗔         ║
║   𝗔𝗯 𝗯𝗮𝗰𝗵 𝗴𝘆𝗮 𝗯𝗲 🤢      ║
╚══════════════════════════╝
        """)

@only_sudo
async def slidespam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slidespam_targets.add(update.message.reply_to_message.from_user.id)
        await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹 ║
║   𝗦𝗟𝗜𝗗𝗘 𝗦𝗣𝗔𝗠 𝗦𝗨𝗥𝗨 𝗞𝗥 𝗗𝗜𝗬𝗔  ║
║   𝗔𝗯 𝘁𝗼 𝗯𝗲𝗰𝗵𝗮𝗿𝗲 𝗸𝗶 𝗺𝗮𝗮    ║
║   𝗰𝗵𝘂𝘁 𝗷𝗮𝘆𝗲𝗴𝗶  🤣🤣      ║
╚══════════════════════════╝
        """)

@only_sudo
async def stopslidespam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        slidespam_targets.discard(update.message.reply_to_message.from_user.id)
        await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║   𝗦𝗟𝗜𝗗𝗘 𝗦𝗣𝗔𝗠 𝗥𝗢𝗞 𝗗𝗜𝗬𝗔    ║
╚══════════════════════════╝
        """)

@only_sudo
async def swipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args: 
        return await update.message.reply_text("⚠️ Usage: /swipe <name>")
    swipe_mode[update.message.chat_id] = " ".join(context.args)
    await update.message.reply_text(f"""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║   𝗦𝗪𝗜𝗣𝗘 𝗠𝗢𝗗𝗘 𝗢𝗡 𝗞𝗥 𝗗𝗜𝗬𝗔   ║
╠══════════════════════════╣
║ 𝗡𝗮𝗺𝗲: {swipe_mode[update.message.chat_id]}
║ 𝗔𝗯 𝘀𝗮𝗯 𝗸𝗶 𝗺𝗮𝗮 𝗰𝘂𝗱𝗲𝗴𝗶  🤪
╚══════════════════════════╝
    """)

@only_sudo
async def stopswipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    swipe_mode.pop(update.message.chat_id, None)
    await update.message.reply_text("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹 ║
║   𝗦𝗪𝗜𝗣𝗘 𝗠𝗢𝗗𝗘 𝗢𝗙𝗙 𝗞𝗥 𝗗𝗜𝗬𝗔  ║
╚══════════════════════════╝
    """)

# --- Auto Replies & Message Handling ---
async def auto_replies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid, chat_id = update.message.from_user.id, update.message.chat_id
    
    # Check if user is locked
    if uid in locked_users:
        try:
            await update.message.delete()
            
            lock_type = lock_mode.get(chat_id, "delete")
            if lock_type == "swipe":
                for text in RAID_TEXTS[:3]:  # Only send 3 texts to avoid spam
                    await update.message.reply_text(f"🔒 𝗟𝗢𝗖𝗞𝗘𝗗 𝗨𝗦𝗘𝗥 🔒\n{text}")
            else:
                await update.message.reply_text("""
╔══════════════════════════╗
║   ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║      𝗟𝗢𝗖𝗞 𝗛𝗔𝗜 𝗕𝗘        ║
╠══════════════════════════╣
║ 𝗧𝗲𝗿𝗶 𝗺𝗮𝗮 𝗻𝗵𝗶 𝗯𝗼𝗹𝗻𝗲 𝗱𝗲𝗴𝗮  ║
║ 𝗖𝗵𝘂𝗽 𝗿𝗲𝗵 𝗺𝗮𝗱𝗮𝗿𝗰𝗵𝗼𝗱     ║
║        🔒🤐🔒            ║
╚══════════════════════════╝
                """)
        except Exception as e:
            print(f"Error deleting message: {e}")
    
    # Existing auto replies
    if uid in slide_targets:
        for text in RAID_TEXTS[:3]: 
            await update.message.reply_text(text)
    if uid in slidespam_targets:
        for text in RAID_TEXTS[:3]: 
            await update.message.reply_text(text)
    if chat_id in swipe_mode:
        for text in RAID_TEXTS[:3]: 
            await update.message.reply_text(f"{swipe_mode[chat_id]} {text}")

# ---------------------------
# BUILD APP & RUN
# ---------------------------
def build_app(token):
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping_cmd))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(CommandHandler("gcnc", gcnc))
    app.add_handler(CommandHandler("ncemo", ncemo))
    app.add_handler(CommandHandler("ncflag", ncflag))
    app.add_handler(CommandHandler("timenc", timenc))
    app.add_handler(CommandHandler("rage", rage_cmd))
    app.add_handler(CommandHandler("coolrage", coolrage_cmd))
    app.add_handler(CommandHandler("die", die_cmd))
    app.add_handler(CommandHandler("stopgcnc", stopgcnc))
    app.add_handler(CommandHandler("stopncemo", stopncemo))
    app.add_handler(CommandHandler("stopall", stopall))
    app.add_handler(CommandHandler("delay", delay_cmd))
    app.add_handler(CommandHandler("status", status_cmd))
    app.add_handler(CommandHandler("addsudo", addsudo))
    app.add_handler(CommandHandler("delsudo", delsudo))
    app.add_handler(CommandHandler("listsudo", listsudo))
    app.add_handler(CommandHandler("targetslide", targetslide))
    app.add_handler(CommandHandler("stopslide", stopslide))
    app.add_handler(CommandHandler("slidespam", slidespam))
    app.add_handler(CommandHandler("stopslidespam", stopslidespam))
    app.add_handler(CommandHandler("swipe", swipe))
    app.add_handler(CommandHandler("stopswipe", stopswipe))
    app.add_handler(CommandHandler("spam", spam_cmd))
    app.add_handler(CommandHandler("stopspam", stopspam_cmd))
    app.add_handler(CommandHandler("lock", lock_cmd))
    app.add_handler(CommandHandler("unlock", unlock_cmd))
    app.add_handler(CommandHandler("locktype", locktype_cmd))
    app.add_handler(CommandHandler("end", end_cmd))
    app.add_handler(CommandHandler("startbot", startbot_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_replies))
    return app

async def run_all_bots():
    global apps, bots
    print("🚀 Starting  ✘ 𝐕 ɪ ʀ ᴜ 𝐔   BHAGWAN...")
    
    for token in TOKENS:
        if token.strip():
            try:
                app = build_app(token)
                apps.append(app)
                bots.append(app.bot)
                print(f"✅ Bot loaded: {app.bot.first_name}")
            except Exception as e:
                print(f"❌ Failed building app for token {token[:10]}...: {e}")

    print(f"\n📊 Total bots loaded: {len(bots)}")
    print("⚡ Starting polling for all bots...\n")

    for i, app in enumerate(apps):
        try:
            await app.initialize()
            await app.start()
            await app.updater.start_polling()
            print(f"✅ Bot {i+1} started polling")
        except Exception as e:
            print(f"❌ Failed starting app {i+1}: {e}")

    print("""
╔══════════════════════════╗
║    ❍─͢͢𓆩〭〬🤍𓆪˹Sam⚡⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭❤️🌹║
║       𝗕𝗛𝗔𝗚𝗪𝗔𝗡 𝗜𝗦 𝗥𝗘𝗔𝗗𝗬   ║
║         🚀⚡🔥           ║
╚══════════════════════════╝
    """)
    
    # Keep running
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_all_bots())
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
