from config import UPDATE_CHANNEL
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from plugins.filters import private_use


@Client.on_message(filters.private & filters.incoming)
@private_use
async def forcesub_handler(c: Client, m: Message):
    owner = c.owner
    if UPDATE_CHANNEL:
        invite_link = c.invite_link
        try:
            user = await c.get_chat_member(UPDATE_CHANNEL, m.from_user.id)
            if user.status == "kicked":
                await m.reply_text("**Hey you are banned 😜**", quote=True)
                return
        except UserNotParticipant:
            buttons = [
                [
                    InlineKeyboardButton(
                        text="✇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ✇", url=invite_link.invite_link
                    )
                ]
            ]
            buttons.append(
                [InlineKeyboardButton("🔄 ʀᴇꜰʀᴇsʜ 🔄", callback_data="sub_refresh")]
            )

            # Send image and text together
            await m.reply_photo(
                photo="https://envs.sh/XFr.jpg",
                caption=f"ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ʏᴏᴜ ᴍᴜꜱᴛ ꜰɪʀꜱᴛ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ. ᴄʟɪᴄᴋ ᴏɴ \"✇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ✇\" ʙᴜᴛᴛᴏɴ.ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ \"ʀᴇǫᴜᴇꜱᴛ ᴛᴏ ᴊᴏɪɴ\" ʙᴜᴛᴛᴏɴ. ᴀꜰᴛᴇʀ ᴊᴏɪɴɪɴɢ, ᴄʟɪᴄᴋ ᴏɴ \"ʀᴇꜰʀᴇsʜ 🔄\" ʙᴜᴛᴛᴏɴ.",
                reply_markup=InlineKeyboardMarkup(buttons),
                quote=True,
            )
            return
        except Exception as e:
            print(e)
            await m.reply_text(
                f"Something went wrong. Please try again later or contact {owner.mention(style='md')}",
                quote=True,
            )
            return
    await m.continue_propagation()
