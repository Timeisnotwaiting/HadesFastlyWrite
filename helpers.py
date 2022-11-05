from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM

class Strings:
    START_TEXT = """👋🏻 Welcome {}

💭 This bot will periodically send images to your group with text. The user who writes the word fastest possible will win coins.

🆙 Share your bot profile inline by typing <code>@{}</code> wherever you want!"""
    
    START_MARKUP = IKM(
                   [
                   [
                   IKB("➕ Add me to your group ➕", url=f"t.me/{BOT_USERNAME}?startgroup=True")
                   ],
                   [
                   IKB("help", callback_data="help")
                   IKB("credits", callback_data="credits")
                   ]
                   ]
                   )
