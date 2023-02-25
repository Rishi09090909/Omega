from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video | filters.audio | filter.image | filter.photo | filter.text | filter.font


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio", "photo", "image", "text", "font"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    await save_file(media)
