from telethon import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest
import schedule, time

from personal_information import api_id, api_hash, phone

timer = 0
client = TelegramClient("session_name", api_id, api_hash)

async def change_avatar(hours):
    await client.start(phone)
    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
    await client(UploadProfilePhotoRequest(
        file = await client.upload_file("img/"+str(hours)+".jpg")
    ))
    print(hours)


schedule.every(1).hours.do(lambda: client.loop.run_until_complete(change_avatar(timer)))
while True:
    if timer > 24:
        timer = 0
    schedule.run_pending()
    time.sleep(3600)
    timer += 1