import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = int(environ.get('API_ID', '27784435'))
API_HASH = environ.get('API_HASH', '68359277aa8d4e439bb8b98b533fbf6f')
BOT_TOKEN = environ.get('BOT_TOKEN', '6480605153:AAF4SJBEYkt4Co5wlPUwoVbRIkvI-HkiAsY')
PORT = int(environ.get('PORT', '8080'))

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', 'CAACAgIAAxkBAAEGm9hjhf69CtQmXoeQ2HidYCGBFeZ4gAACxgEAAhZCawpKI9T0ydt5RysE CAACAgIAAxkBAAEGm9pjhf7I9jCDh3PpkocMNFcPJfisvwAC0wADVp29CvUyj5fVEvk9KwQ CAACAgIAAxkBAAEGm9xjhf7SH4Yc8EP5yI4e8BTH968ClwACGAADDbbSGX671giQDJU8KwQ')).split()
PICS = (environ.get('PICS', 'https://graph.org/file/aa7f6e3c8b1307654abf3.jpg https://graph.org/file/82a53e1a92ab90a511ac8.jpg https://graph.org/file/2f617b1cad9a18ccda96a.jpg https://graph.org/file/21191dc065aff00097aa8.jpg https://graph.org/file/9b98813764d6a8c5e303e.jpg')).split()

# Bot Admins
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '5505094097').split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001857838895').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001986490303')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001532575427'))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/Seemovies_support')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/See_update')
USERNAME = environ.get('USERNAME', 'https://t.me/JNGohell')
# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "✅ I Found: <code>{query}</code>\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating} / 10</a>\n☀️ Languages: {languages}\n📀 RunTime: {runtime} Minutes\n\n🗣 Requested by: {message.from_user.mention}\n©️ Powered by: <b>{message.chat.title}</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "<i>{file_name}</i>\n\nᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "sheralinks.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "433d789f076d76614b7e8f5b0c2618059a63b679")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "Hello {mention}, Welcome to {title} group!")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/movie_funda_backup")

# stream features vars
"""Deploy this repo: https://github.com/kk9546/seebot"""
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "0"))
URL = environ.get("URL", "https://sl-bots-0db4fd13c9ad.herokuapp.com/")
                           
