from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CSO7PoAABDBD7YRN3c9e7S1DlbZETkRopa5_exUAAAlcEAAL5JElUmDXkx-mFPL4gBA")
    await message.reply_text(
        f"""<b> Hey,👋 {message.from_user.first_name}!
\n Hello 👋 there! Hey there! My name is ༒ 𝓥 𝓘 𝓢 𝓐 ༒.
I can help manage your groups with useful features, feel free to add me to your groups!.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                          InlineKeyboardButton(
                               text="➕ Add ༒ 𝓥 𝓘 𝓢 𝓐 ༒ to your Group ➕", url="t.me/MissVisaBot?startgroup=true"),
                   ],
                   [
                         InlineKeyboardButton(text="Source Code 🗒️", callback_data="source_"),
                         InlineKeyboardButton(
                                 text="System Stats 💻", callback_data="stats_callback"
                       ),
                  ],
                  [
                        InlineKeyboardButton(text="🙋‍♀️ Chat Group", url=f"https://t.me/WeGetTogether"),
                        InlineKeyboardButton(
                                text="💬 Support Group", url=f"https://t.me/Visa_Support"
                       ),
                   ],
                   [
                        InlineKeyboardButton(text="❓ Commands Help ", callback_data="help_back"),
                   ],
          ]
      )
    )
