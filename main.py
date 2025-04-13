import json, time, schedule, asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.photos import DeletePhotosRequest, UploadProfilePhotoRequest

from moduls.personal_information import API_ID, API_HASH, phone


client = TelegramClient("session_name", API_ID, API_HASH)

def new_schedule():
    with open("schedule.json", 'r', encoding='utf-8') as f:
        timetable = json.load(f)[f"{datetime.today().day}.{datetime.today().month}.{datetime.today().year}"]
        times = timetable.keys()
    schedule.clear()
    for i in times:
        schedule.every().day.at(i).do(lambda image: client.loop.run_until_complete(change_avatar(timetable[i])))

async def change_avatar(work):
    await client.start(phone)
    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
    await client(UploadProfilePhotoRequest(
        file = await client.upload_file("img/"+work+".jpg")
    ))

async def main():
    new_schedule()
    while True:
        if datetime.today().hour < 3:
            new_schedule()
        else:               
            schedule.run_pending()
            time.sleep(1800)

if __name__ == "__main__":
    asyncio.run(main())
