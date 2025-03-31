from telethon import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
from personal_information import api_id, api_hash, phone

client = TelegramClient("session_name", api_id, api_hash)

async def change_avatar(image_path):
    await client.start(phone)
    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
    await client(UploadProfilePhotoRequest(
        file = await client.upload_file(image_path)
    ))
with client:
    client.loop.run_until_complete(change_avatar("Artemos_id.jpg"))