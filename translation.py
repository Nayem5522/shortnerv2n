from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi there {} 

Send me a link or post and I'll shorten it for you!

To learn more about what I can do, just type /help.
✅ If you don't know how to use it 
Then just click /tutorial_prime

I support all kinds of {}
This bot current Shortener website is: {}

Anyone who want to use any other shortner instead of Like this bot or Want to create a bot like this for your own shortener? than contact at 👉 <a href='https://t.me/Prime_Bots_Support_RoBot'> @ᴍʀ ᴘʀɪᴍᴇ ⚡</a> (all shortners support avilable.)

<blockquote> - ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ ʙʏ <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛz 🔥</a></blockquote>
"""

HELP_MESSAGE = """Hey Dear ❤️ I'm a link converter & shortener bot, here to make your work easier and help you earn more 💰.

🔹 **User Commands**  
/start – Start using the bot.  
/help – Get bot usage details.  
/about – Learn more about the bot.  
/me – View your profile info.  
/stats – Check bot & server status.  

🔹 **Customization**  
/base_site – Change URL shortener site.  
/shortener_api – Set API for short links.  
/header – Add text at the top.  
/footer – Add text at the bottom.  
/banner_image – Set a banner (Admin).  
/reset_prime – Reset settings.  

🔥 **Admin Commands**  
/batch -100xxx – Convert all posts in a channel.  
/logs – Get bot logs.  
/restart – Restart bot server.  
/ban – Ban a user.  
/unban – Unban a user.  
/info – Get user details.  

⚡ **Special Features**  
🔗 [Hyperlink](https://t.me/{username}) support 🔗
🔘 Button conversion enabled.  
📝 Custom Header & Footer.  
📎 Username replacement function.  
🖼 Banner image support.  

✅ If you don't know how to use it 
Then just click. /tutorial_prime
"""

ABOUT_TEXT = """
<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
   
‣ ᴍʏ ɴᴀᴍᴇ : ** {} **
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Prime_Nayem'>ᴍʀ.ᴘʀɪᴍᴇ</a> 
‣ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Botz'>ᴘʀɪᴍᴇ ʙᴏᴛᴢ</a> 
‣ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Prime_Movies4U'>ᴘʀɪᴍᴇ ᴍᴏᴠɪᴇs</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mdlink` - Change all the links of the post to your MDisk account first and then short to {shortener} link.

> `shortener` - Short all the links of the post to {shortener} link directly.

> `mdisk` - Save all the links of the post to your Mdisk account.
    
To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""


HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⚙️ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ ⚙️", url="https://t.me/Prime_Nayem"),
            InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ ꜱᴜᴘᴘᴏʀᴛ 👨‍💻", url="https://t.me/Prime_Bots_Support_RoBot"),
        ],
        [
            InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📢", url="https://t.me/Prime_Botz"),
        ],
        [
            InlineKeyboardButton("🤝 ѕᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🤝", url="https://t.me/Prime_Botz_Support"),
            InlineKeyboardButton("🏠 ʜᴏᴍᴇ 🏠", callback_data="start_command"),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ᴀᴅᴍɪɴ", url="https://t.me/Prime_Nayem"),
            InlineKeyboardButton("👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Prime_Bots_Support_RoBot"),
        ],
        [InlineKeyboardButton("🏠 ʜᴏᴍᴇ 🏠", callback_data="start_command")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⛑️ ʜᴇʟᴘ 👨‍🚒", callback_data="help_command"),
            InlineKeyboardButton("💁‍♂️ ᴀʙᴏᴜᴛ 😉", callback_data="about_command"),
        ],
        [
            InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/Prime_Nayem"),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "MDLINK", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
            InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 ʙᴀᴄᴋ 🔙", callback_data="help_command")]]
)

USER_ABOUT_MESSAGE = """
🔧 Here are the current settings for this bot:

- 🌐 Shortener website: {base_site}

- 🧰 Here is your: {method} Details 

- 🔌 {base_site} API: {shortener_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}
"""


MDISK_API_MESSAGE = """To add or update your Mdisk API, \n`/mdisk_api mdisk_api`
            
Ex: `/mdisk_api 6LZq851sXoPHugiKQq`
            
Others Mdisk Links will be automatically changed to the API of this Mdisk account

Get your Mdisk API from @VideoToolMoneyTreebot

Current Mdisk API: `{}`"""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

To change your Shortener Website: /base_site

Current Shortener API: `{shortener_api}`"""

HEADER_MESSAGE = """📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! 🎉"""

FOOTER_MESSAGE = """📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! 🎉"""

USERNAME_TEXT = """Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
